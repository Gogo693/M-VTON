import os
import shutil


chunk_n = 19

source_img_dir = './train_full/images/'
source_keyp_dir = './train_full/keypoints/'

root = './' + str(chunk_n).zfill(3) + '_chunk/'
imdir = root + 'images/'
kdir = root + 'keypoints/'

os.mkdir(root)
os.mkdir(imdir)
os.mkdir(kdir)

imgs = list()

for count, fname in enumerate(os.listdir(source_img_dir)):
    imgs.append(fname)

imgs.sort()

for i in range(chunk_n * 100, (chunk_n + 1) * 100):
    img = imgs[i]
    keyp = img.replace('.jpg', '') + '_keypoints.json'

    shutil.copy(source_img_dir + img, imdir + img)
    shutil.copy(source_keyp_dir + keyp, kdir + keyp)



