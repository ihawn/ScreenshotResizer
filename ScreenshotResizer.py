from PIL import Image
import PIL
from os import listdir
from os.path import isfile, join, isdir


def GetAllFilesRecursive(root):
    files = [join(root, f) for f in listdir(root) if isfile(join(root, f))]
    dirs = [d for d in listdir(root) if isdir(join(root, d))]
    for d in dirs:
        files_in_d = GetAllFilesRecursive(join(root, d))
        if files_in_d:
            for f in files_in_d:
                files.append(join(root, f))
    return files

def ScaleImage(im, resX, resY):
    w, h = im.size
    images = []

    for i in range(len(resX)):
        scaleFactor = max(float(resX[i]/w), float(resY[i]/h))
        img = im.resize((round(scaleFactor*w), round(scaleFactor*h)))
        images.append(img)

    return images

def CropImage(images, resX, resY):
    for i in range(len(images)):
        w, h = images[i].size
        left = (w - resX[i])/2
        top = (h - resY[i])/2
        right = (w + resX[i])/2
        bottom = (h + resY[i])/2

        img = images[i].crop((left, top, right, bottom))
        images[i] = img

    return images

def Main():
    readPath = 'C:/Users/Isaac/Documents/_games/SaveDave/Media/Screenshots'
    writePath = 'C:/Users/Isaac/Documents/_games/SaveDave/Media/IOS'

    resX = [1242]
    resY = [2688]

    files = GetAllFilesRecursive(readPath)

    j = 0
    for f in files:
        print(j+1, "/", len(files))
        try:
            image = Image.open(f)
            images = ScaleImage(image, resX, resY)
            images = CropImage(images, resX, resY)

            for i in range(len(images)):
                pic = images[i].save(writePath + "/" + str(resX[i]) + "_" + str(resY[i]) + "_" + str(j) + ".jpg", 'JPEG')
        except:
            print(f, "is either unreadable or not an image")
        j+=1


if __name__ == '__main__':
    Main()