import os
import configargparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name',
                    required=True,
                    help='Experiment name')

args = parser.parse_args()
name = str(args.name)


# TRAINING PHASE

# Train GMM
command = 'python train.py \
                    --name ' + name + ' \
                    --stage GMM \
                    --workers 4 \
                    --save_count 50000 \
                    --shuffle \
		    --keep_step 20 \
		    --decay_step 20 \
                '
print(command)
os.system(command)

# Test GMM on Training set for TOM input
command = 'python test.py \
                    --name ' + name + ' \
                    --stage GMM \
                    --workers 4 \
                    --datamode train \
                    --data_list train_pairs.txt \
                    --checkpoint checkpoints/' + name + '/gmm_final.pth \
                '
print(command)
os.system(command)

# Move Train warping results
command = 'cp -r ./result/gmm_final.pth/train/warp-cloth/ ./data/train/warp-cloth'
print(command)
os.system(command)

command = 'cp -r ./result/gmm_final.pth/train/warp-mask/ ./data/train/warp-mask'
print(command)
os.system(command)

# Train TOM
command = 'python train.py \
                    --name ' + name + ' \
                    --stage TOM \
                    --workers 4 \
                    --save_count 50000 \
                    --shuffle \
		    --keep_step 20 \
		    --decay_step 20 \
                '
print(command)
os.system(command)


# TEST PHASE

# Test GMM on Test set
command = 'python test.py \
                    --name ' + name + ' \
                    --stage GMM \
                    --workers 4 \
                    --datamode test \
                    --data_list test_pairs.txt \
                    --checkpoint checkpoints/' + name + '/gmm_final.pth \
                '
print(command)
os.system(command)

# Move Train warping results
command = 'cp -r ./result/gmm_final.pth/test/warp-cloth/ ./data/train/warp-cloth'
print(command)
os.system(command)

command = 'cp -r ./result/gmm_final.pth/test/warp-mask/ ./data/train/warp-mask'
print(command)
os.system(command)

# Test TOM
command = 'python test.py \
                    --name ' + name + ' \
                    --stage TOM \
                    --workers 4 \
                    --datamode test \
                    --data_list test_pairs.txt \
                    --checkpoint checkpoints/' + name + '/step_200000.pth \
                '
print(command)
os.system(command)

# Move results to results folder
command = 'cp -r ./result/step_200000.pth/test/try-on/ ./data/Full_results/' + name
print(command)
os.system(command)

command = 'cp -r ./result/step_200000.pth/test/try-on/ ./data/Full_results/' + name
print(command)
os.system(command)
