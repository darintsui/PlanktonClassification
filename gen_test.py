import os
import sys
import subprocess
from PIL import Image

if len(sys.argv) < 3:
    print("Usage: python gen_test.py input_folder output_folder")
    exit(1)

fi = sys.argv[1]
fo = sys.argv[2]
small_size = (48, 48)

imgs = os.listdir("C:/Users/Darin Tsui/cogs181/" + fi)


for img in imgs:
    infilename = "C:/Users/Darin Tsui/cogs181/" + fi + "\\" + img
    im = Image.open(infilename) 
    small_im = im.resize(small_size)
    outfilename = "C:/Users/Darin Tsui/cogs181/" + fo + "\\" + img
    small_im.save(outfilename,"png")
