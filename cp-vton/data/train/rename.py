import os

imgs = list()
keyp = list()

keypdir = './openpose_keyp/'

for count, fname in enumerate(os.listdir('./image/')):
    imgs.append(fname)

for count, fname in enumerate(os.listdir(keypdir)):
    keyp.append(fname)

imgs.sort()
keyp.sort()

for i, img in enumerate(imgs):
    print(img)
    print(keyp[i])
    img = img.replace('.jpg', '')
    os.rename(keypdir + keyp[i], keypdir + img + '_keypoints.json')
