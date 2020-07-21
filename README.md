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

Download the dataset divided into the input folder and make sure to have 

Sample results can be found in directory:

```
/smpl/output/images/
```

To play the demo be sure to download smpl models and put them in directory:

```
/smpl/models/
```

and just launch the demo.py script when in smpl folder:

```
cd smpl
python3 ./demo.py
```
An example here:

![Original image](https://github.com/Gogo693/FashionGAN/blob/master/smpl/input/images/000010_0.jpg)
![Smpl model](https://github.com/Gogo693/FashionGAN/blob/master/smpl/output/images/000010_0/000/output.png)
