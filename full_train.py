import os
import configargparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name',
                    required=True,
                    help='Experiment name')

args = parser.parse_args()
name = str(args.name)

# Train GMM
command = 'python train.py \
                    --name ' + name + ' \
                    --stage GMM \
                    --workers 4 \
                    --save_count 50000 \
                    --shuffle
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

# Move warping results
command = 'cp ./results/ \
                '
print(command)
os.system(command)

# Train TOM
command = 'python train.py \
                    --name ' + name + ' \
                    --stage TOM \
                    --workers 4 \
                    --save_count 50000 \
                    --shuffle
                '
print(command)
os.system(command)

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

# Test TOM
command = 'python test.py \
                    --name ' + name + ' \
                    --stage TOM \
                    --workers 4 \
                    --datamode test \
                    --data_list test_pairs.txt \
                    --checkpoint checkpoints/' + name + '/tom_final.pth \
                '
print(command)
os.system(command)

# Move results to results folder
command = 'python3 smplifyx/main.py \
                    --gender=female \
                '
print(command)
os.system(command)