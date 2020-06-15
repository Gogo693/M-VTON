import os

imgs = list()
keyp = list()

imgdir = './test_set_dress/images/'
keypdir = './test_set_dress/keypoints/'

for count, fname in enumerate(os.listdir(imgdir)):
    imgs.append(fname)

for count, fname in enumerate(os.listdir(keypdir)):
    split_name = fname.split('_')
    #print(type(split_name))
    split_name[0] = split_name[0].zfill(6)
    new_name = split_name[0] + '_' + split_name[1]
    os.rename(keypdir + fname, keypdir + new_name)
    keyp.append(new_name)

imgs.sort()
keyp.sort()

for i, img in enumerate(imgs):
    print(img)
    print(keyp[i])
    img = img.replace('.jpg', '')
    os.rename(keypdir + keyp[i], keypdir + img + '_keypoints.json')
