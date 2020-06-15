import os
import configargparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--chunkn',
                    required=True,
                    type=int,
                    help='The number of the chunk to be processed')

args = parser.parse_args()
chunk_n = str(args.chunkn).zfill(3) + '_chunk/'


command = 'python3 smplifyx/main.py \
                    --config cfg_files/fit_smpl.yaml \
                    --data_folder ./input/' + chunk_n + ' \
                    --output_folder ./output/' + chunk_n + ' \
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
