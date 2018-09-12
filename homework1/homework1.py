import os
clip_imgdir = r'C:\Users\Afini\Desktop\homework1\data'

with open('./result.txt', 'w') as f:
    for file in os.listdir(clip_imgdir):
        num = open('./data/'+file, 'r')
        num = num.read()
        f.write(file[:-4].strip() + num + '\n')