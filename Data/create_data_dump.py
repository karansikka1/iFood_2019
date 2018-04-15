# Code to create data dump (dumping images from downloaded data in a folder)

import ipdb
import os
import glob

src = '../../Data/food-321-ini/'
dest = 'sample_images/'
file_class_names = './food-classes-ngrams-pass2_200.txt'

class_names = []
for i, lines in enumerate(open(file_class_names)):
    if i > 217:
        break
    tmp = lines.strip().split(',')[0]
    #if len(tmp.split(' ')) > 1:
    #    tmp = tmp.split(' ')[0] + '_' + tmp.split(' ')[1]
    #if len(tmp.split(' ')) > 2:
    #    tmp = tmp.split(' ')[0] + '_' + tmp.split(' ')[1] + '_' + tmp.split('\
    #                                                                        ')[2]
    tmp = '_'.join(tmp.split(' '))
    if len(tmp.split('_')[-1]) <= 1:
        tmp = tmp.split('_')[0]
    class_names.append(tmp)

N = 0
if __name__ == "__main__":
    for class_name in class_names:
        list_files = glob.glob(src + class_name + '/*')
        if len(list_files) == 0:
            print 'skipping %s' %(class_name)
            continue
        #if os.path.isdir('./sample_images_old/' + class_name):
        #    if len(os.listdir('./sample_images_old/' + class_name)) > 0:
        #        continue
        if not os.path.isdir(dest + class_name):
            os.mkdir(dest + class_name)
        print 'Running for class %s' %(class_name)
        for i,f in enumerate(list_files):
            os.system('cp %s %s/%s/' %(f, dest, class_name))
        N += 1

        #if not os.path.isdir(src + class_name):
        #    print 'skipping %s' %(class_name)
        #    continue
        #else:
        #    os.system('cp -r %s/%s %s' %(src, class_name, dest))
    print N
