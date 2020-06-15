import os 
import shutil

for dirname in os.listdir('./'):
    if 'chunk' in dirname:
        #print(dirname)
        for source in os.listdir(dirname + '/meshim/'):
            dest = './extracted_output/' + source + '/000/'
            source = './' + dirname + '/meshim/' + source + '/000/'
            #print(source)
            #print(dest)
            shutil.copytree(source, dest)