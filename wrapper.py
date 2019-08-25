import os
import argparse
from pathlib import Path
import shutil
import glob

parser = argparse.ArgumentParser()
arg = parser.add_argument
arg('--shirt_path', type=str, default='original_shirts/0.png', help='Gender whose shirt you want to generate')

args = parser.parse_args()

#get a list of handbags
handbag_list=glob.glob('handbags/*.jpg')
#print(handbag_list)

print(args.shirt_path)
#make a shirt directory
output_dump_directory= Path('.').absolute()
output_dump_directory.mkdir(exist_ok=True)

print(args.shirt_path.split('/')[1][:-4])
#create a shirt directory
(output_dump_directory /'output'/(args.shirt_path.split('/')[1][:-4])).mkdir(exist_ok=True, parents=True)

#loop over the handbags
for i,handbag_path in enumerate(handbag_list):
    print('handbag',i+1, " out of ", len(handbag_list), " being processed","shirt is",args.shirt_path)
    if os.path.exists((output_dump_directory /'output'/(args.shirt_path.split('/')[1][:-4])/handbag_path.split('/')[1][:-4])):
        print("path found, skipping this combination")
    else:
        (output_dump_directory /'output'/(args.shirt_path.split('/')[1][:-4])/handbag_path.split('/')[1][:-4]).mkdir(exist_ok=True, parents=True)
        output_dir= 'output/'+args.shirt_path.split('/')[1][:-4]+'/'+handbag_path.split('/')[1][:-4]
        #print(output_dir)
        os.system("python stylize.py --content_img={} --style_img={} --output_dir={}".format(args.shirt_path,handbag_path,output_dir))
