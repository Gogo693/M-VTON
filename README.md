# M-VTON

## Requirements
For the mesh generation part be sure to follow smpl-x original repository for installation instructions of smpl:
[SMPL-X](https://github.com/vchoutas/smplify-x)

Install dependences for the try-on part:

```
pip install -r ./m-vton/requirements.txt
```

## Mesh Generation
In this phase we generate the mesh image of the person by using SMPL-X, starting from the dataset provided by CP-VTON.

Download the dataset divided into the input folder and make sure to have the input divided into two folders: 'images' and 'keypoints'.
Run the script for fitting all the images:

```
python3 ./smplify-x/fit_full.py --dataset train
python3 ./smplify-x/rename.py
```
The 'dataset' option is used to specify train or test dataset folder.
The 'rename.py' command is used to keep name consistency betweeen input and generated data, make sure to select the right folder.

Sample results can be found in directory:

```
/smplify-x/output/images/
```

To play the demo be sure to download smpl models and put them in directory:

```
/smplify-x/models/
```

and just launch the demo.py script when in smpl folder:

```
cd smplify-x
python3 ./demo.py
```
An example here:

![Original image](https://github.com/Gogo693/M-VTON/blob/master/examples/input.jpg)
![Smpl model](https://github.com/Gogo693/M-VTON/blob/master/examples/output.png)

## Try-On Part
In this phase we generate the final image.

Prepare the data by exctracting the original dataset and copying the generated meshes into './m-vton/data/train/meshim/'.

You can run the full experiment by running the command:

```
cd m-vton
python3 ./full_train.py --name experimentname
```
which runs the different parts of the algorithm composed of:

1. gmm train on train set
2. gmm test on train set (to get the warped cloth for the vton part)
3. vton train on train set
4. gmm test on test set
5. vton test on test set

An example of the final result:
![Final results](https://github.com/Gogo693/M-VTON/blob/master/examples/input.jpg)
