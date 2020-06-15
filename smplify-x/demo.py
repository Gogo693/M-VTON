import os

os.system('python3 smplifyx/main.py \
                    --config cfg_files/fit_smpl.yaml \
                    --data_folder ./input/ \
                    --output_folder ./output \
                    --visualize=True \
                    --model_folder ./models \
                    --vposer_ckpt  ../vposer_v1_0 \
                    --part_segm_fn smplx_parts_segm.pkl \
                    --interpenetration False \
                    --use_face False \
                    --use_hands False \
                    --gender=female \
                ')