import os
import configargparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset',
                    required=True,
                    help='Specify train or test.')

args = parser.parse_args()
dataset = str(args.dataset)


command = 'python3 smplifyx/main.py \
                    --config cfg_files/fit_smpl.yaml \
                    --data_folder ./input/' + dataset + ' \
                    --output_folder ./output/' + dataset + ' \
                    --visualize=True \
                    --model_folder ./models \
                    --vposer_ckpt  ../vposer_v1_0 \
                    --part_segm_fn smplx_parts_segm.pkl \
                    --interpenetration False \
                    --use_face False \
                    --use_hands False \
                    --gender=female \
                '
print(command)
os.system(command)
