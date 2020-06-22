import os
import shutil
import configargparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dim',
                    required=True,
                    type=int,
                    help='The number of images for the subdataset')

args = parser.parse_args()
dim = args.dim

dir_name_list = ['cloth', 'cloth-mask', 'image', 'image-parse', 'meshim', 'pose']

root = 'data_' + str(dim)

if not os.path.isdir(root):
    for dir_name in dir_name_list:
        os.makedirs(root + '/train/' + dir_name)

train_pairs_f = open('./data/train_pairs.txt')
train_pairs = train_pairs_f.read()

train_pairs = train_pairs.split('\n')
new_pairs = train_pairs[:2000]

new_pairs_f = open(root + '/train_pairs.txt', 'w')
new_pairs_f.write('\n'.join(new_pairs))
new_pairs_f.close()

train_pairs_f = open(root + '/train_pairs.txt')
train_pairs = train_pairs_f.read()

train_pairs = train_pairs.replace('\n', ' ')
train_pairs = train_pairs.split(' ')

people_im_list = [x for x in train_pairs if '_1' not in x]

for people_im in people_im_list:
    print(people_im)
    cloth_im = people_im.replace('_0', '_1')
    people_parse = people_im.replace('.jpg', '.png')
    keyp = people_im.replace('.jpg', '_keypoints.json')

    shutil.copy('./data/train/image/' + people_im, root + '/train/image/' + people_im)
    shutil.copy('./data/train/image-parse/' + people_parse, root + '/train/image-parse/' + people_parse)

    shutil.copy('./data/train/cloth/' + cloth_im, root + '/train/cloth/' + cloth_im)
    shutil.copy('./data/train/cloth-mask/' + cloth_im, root + '/train/cloth-mask/' + cloth_im)

    shutil.copy('./data/train/pose/' + keyp, root + '/train/pose/' + keyp)