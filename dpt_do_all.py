#!/usr/bin/env python3

import glob
import os

image_DB = "/home/sgoering/work/sophoappeal/images/*/"  # absolute path required

images = "input"

os.system("mkdir -p maps/depths")
os.system("mkdir -p maps/segmentation")

def system(cmd):
    os.system(cmd)


for folder in glob.glob(image_DB):
    db_name = os.path.basename(os.path.dirname(folder))
    print(folder, db_name)
    # copy images to image folder
    system(f"rm -rf {images} && mkdir -p {images} && cp {folder}images/* {images}")
    print("copy images")
    system("python3 run_monodepth.py")
    system(f"mkdir -p maps/depths/{db_name} && mv output_monodepth/* maps/depths/{db_name}/ && rm -rf output_monodepth/*")
    system("python3 run_segmentation.py")
    system(f"mkdir -p maps/segmentation/{db_name} && mv output_semseg/* maps/segmentation/{db_name}/ && rm -rf output_semseg/*")


    system(f"rm -rf {images}")

