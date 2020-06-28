#!/bin/bash
cd checkpoints/
rm -r *
cd ..

cd result/
rm -r *
cd ..

cd Full_results/
rm -r *
cd ..

cd tensorboard/
rm -r *
cd ..

cd data/train
rm -r warp*
cd ../test
rm -r warp*
cd ../../
