import os
from PIL import Image

# run this file from directory which contains the input directory  

imgTypes = ('jpg', 'png', 'jpeg', 'svg')
cwd = os.getcwd()

inpDir = ''
while inpDir not in os.listdir(cwd):
    inpDir = input("Enter valid input directory: ")

outDir = input("Enter output directory: ")

if outDir not in os.listdir(cwd):
    outConfirm = input("Output directory not found. Would you like to create one? y/n").lower()
    if outConfirm == 'y':
        os.mkdir(outDir)
    else:
        exit()

imgList = [i for i in os.listdir(inpDir) if i.split('.')[-1].lower() in imgTypes]

print(f"The following images were found in {inpDir}")
for i in imgList:
    print(i)
 

left = int(input("Cropping dimensions from left: "))
top = int(input("Cropping dimensions from top: "))
right = int(input("Cropping dimensions from right: "))
bottom = int(input("Cropping dimensions from bottom: "))


for imgName in imgList:
    img = Image.open(f"{inpDir}/{imgName}")
    outImg = img.crop((left, top, right, bottom))
    
    print(f"successfully cropped {imgName}")
    
    outImgName = f"{cwd}\{outDir}\{imgList.index(imgName) + 1}.{imgName.split('.')[-1]}"
    outImg = outImg.save(f"{outImgName}")

    print(f"successfully saved {imgName} as {outImgName}\n")    
