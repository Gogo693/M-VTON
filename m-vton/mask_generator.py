#coding=utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F

import argparse
import os
import time
from cp_dataset import CPDataset, CPDataLoader
from networks import GMM, UnetGenerator, VGGLoss, load_checkpoint, save_checkpoint

from tensorboardX import SummaryWriter
from visualization import board_add_image, board_add_images
from visualization import board_add_image, board_add_images, save_images


def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default = "GMM")
    parser.add_argument("--gpu_ids", default = "")
    parser.add_argument('-j', '--workers', type=int, default=1)
    parser.add_argument('-b', '--batch-size', type=int, default=4)
    
    parser.add_argument("--dataroot", default = "data_2000")
    parser.add_argument("--datamode", default = "train")
    parser.add_argument("--stage", default = "GMM")
    parser.add_argument("--data_list", default = "train_pairs.txt")
    parser.add_argument("--fine_width", type=int, default = 192)
    parser.add_argument("--fine_height", type=int, default = 256)
    parser.add_argument("--radius", type=int, default = 5)
    parser.add_argument("--grid_size", type=int, default = 5)
    parser.add_argument('--lr', type=float, default=0.0001, help='initial learning rate for adam')
    parser.add_argument('--tensorboard_dir', type=str, default='tensorboard', help='save tensorboard infos')
    parser.add_argument('--checkpoint_dir', type=str, default='checkpoints', help='save checkpoint infos')
    parser.add_argument('--checkpoint', type=str, default='', help='model checkpoint for initialization')
    parser.add_argument("--display_count", type=int, default = 20)
    parser.add_argument("--save_count", type=int, default = 100)
    parser.add_argument("--keep_step", type=int, default = 100000)
    parser.add_argument("--decay_step", type=int, default = 100000)
    parser.add_argument("--shuffle", action='store_true', help='shuffle input data')

    opt = parser.parse_args()
    return opt

def train_mask_gen(opt, train_loader, model):
    model.cuda()
    model.train()
    
    # criterion
    criterionL1 = nn.L1Loss()
    
    # optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=opt.lr, betas=(0.5, 0.999))
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda = lambda step: 1.0 -
            max(0, step - opt.keep_step) / float(opt.decay_step + 1))
    
    for step in range(opt.keep_step + opt.decay_step):
        iter_start_time = time.time()
        inputs = train_loader.next_batch()
            
        c = inputs['cloth'].cuda()

        mesh = inputs['mesh'].cuda()
        pose_map = inputs['pose_map'].cuda()
        person_parse = inputs['person_parse'].cuda()
        
        outputs = model(torch.cat([mesh, pose_map, c], 1))
        #p_rendered, m_composite = torch.split(outputs, 3,1)
        #p_rendered = F.tanh(p_rendered)
        m_composite = F.sigmoid(outputs)
        #p_tryon = c * m_composite + p_rendered * (1 - m_composite)
            
        loss_l1 = criterionL1(m_composite, person_parse)

        loss = loss_l1
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
            
        if (step+1) % opt.display_count == 0:

            t = time.time() - iter_start_time
            print('step: %8d, time: %.3f, loss: %.4f' 
                    % (step+1, t, loss.item()), flush=True)

        if (step+1) % opt.save_count == 0:
            save_checkpoint(model, os.path.join('./mask_gen/', 'model_', 'step_%06d.pth' % (step+1)))
    
    print('Finished in ' + str(time.time() - start_time))

def test_mask_gen(opt, test_loader, model):
    model.cuda()
    model.eval()
    
    base_name = os.path.basename(opt.checkpoint)
    save_dir = os.path.join('./mask_gen/', base_name, opt.datamode)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    try_on_dir = os.path.join(save_dir, 'try-on')
    if not os.path.exists(try_on_dir):
        os.makedirs(try_on_dir)

    
    for step, inputs in enumerate(test_loader.data_loader):
        iter_start_time = time.time()
        inputs = test_loader.next_batch()

        im_names = inputs['im_name']
        c = inputs['cloth'].cuda()

        mesh = inputs['mesh'].cuda()
        pose_map = inputs['pose_map'].cuda()
        person_parse = inputs['person_parse'].cuda()
        
        outputs = model(torch.cat([mesh, pose_map, c], 1))
        m_composite = F.sigmoid(outputs)
            
        save_images(m_composite, im_names, try_on_dir) 

        if (step+1) % opt.display_count == 0:
            t = time.time() - iter_start_time
            print('step: %8d, time: %.3f' % (step+1, t), flush=True)
    
    print('Finished in ' + str(time.time() - start_time))

def main(): 
    opt = get_opt()
    print(opt)
    print("Start to train stage: %s, named: %s!" % (opt.stage, opt.name))

    # create dataset 
    train_dataset = CPDataset(opt)

    # create dataloader
    train_loader = CPDataLoader(opt, train_dataset)

    model = UnetGenerator(22, 1, 6, ngf=64, norm_layer=nn.InstanceNorm2d)

    load_checkpoint(model, opt.checkpoint)
    with torch.no_grad():
        test_mask_gen(opt, train_loader, model)

    #train_mask_gen(opt, train_loader, model)


if __name__ == "__main__":
    main()