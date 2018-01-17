import os
import shutil
from PIL import Image

def createFolder(user):
    """
    Desc: This function looks at the desktop and creates a folder to store the hidden windows wallpapers
    :param user: The name of the user. It's writen so it can be run on any computer
    :return: Nothing
    """
    if not os.path.exists("C:" + os.path.sep + "Users" + os.path.sep + user + "\Desktop" + os.path.sep + "Windows Background Photos"):
        os.makedirs("C:" + os.path.sep + "Users" + os.path.sep + user + "\Desktop" + os.path.sep + "Windows Background Photos")
        print("Made Windows hidden files folder")
    else:
        print("The file existed already")

def copyFiles(src, dest):
    """
    Desc: This function will take in 2 locations and copy the files in the src to the dest
    :param src: The location the files are to be copied
    :param dest: The location the files will be copied
    :return: Nothing
    """
    src_files = os.listdir(src)

    # this function is what copies the files to the destination
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dest)

def convertFilesToJPGs(filePath):
    """
    Desc: This changes the name of the files in the location and adds .jpg at the end so it converts it to a jpg
    :param filePath: the location of the files to be converted
    :return: Nothing
    """
    lst = os.listdir(filePath)
    fileList = []
    for number in range(1, len(lst)+1):
        fileList.append("test"+str(number)+".jpg")

    os.chdir(filePath)
    for num in range(len(lst)):
        os.renames(lst[num], fileList[num])

    print("The files have been converted")

def removePictures( dest ):
    """
    Desc: This function deletes the annoying pictures that are really small or aren't pictures at all.
    :param dest: the location of the folder where the images are stored
    :return: Nothing
    """
    lst = os.listdir(dest)
    remove = []
    for num in range(len(lst)):
        try:
            image = lst[num]
            im = Image.open(image)
            Width = im.width
            if Width < 1200:
                print("small photo")
                remove.append(dest + os.path.sep + lst[num])
        except IOError:
            print("not an image")
            remove.append(dest + os.path.sep + lst[num])
            im.close()
    for photo in range(len(remove)):
        print("deleted")
        os.remove(remove[photo])


def removeDuplicates(wallpaperFolder, dest):
    hiddenPhotolst = os.listdir(dest)
    wallpaperFolderLst = os.listdir(wallpaperFolder)
    remove = []
    for hiddenPhotoNum in range(len(hiddenPhotolst)):
        for wallpaperPhotoNum in range(len(wallpaperFolderLst)):

            try:
                image = lst[num]
                im = Image.open(image)
                imgWidth = im.width
                if imgWidth < 1200:
                    print("small photo")
                    remove.append(dest + os.path.sep + lst[num])
            except IOError:
                print("not an image")
                remove.append(dest + os.path.sep + lst[num])
                im.close()



        for photo in range(len(remove)):
            print("deleted")
            os.remove(remove[photo])





def main():
    user = str(os.getlogin()) #this gets the user name and checks to see if the dest folder exists already
    src = os.path.abspath("C:" + os.path.sep + "Users" + os.path.sep + user+"\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets") # hidden file location
    dest = os.path.abspath("C:" + os.path.sep + "Users" + os.path.sep + user + "\Desktop" + os.path.sep + "Windows Background Photos")

    wallpaperFolder = os.path.abspath("C:" + os.path.sep + "Users" + os.path.sep + user + "\OneDrive" + os.path.sep + "wallpapers")

    createFolder(user)
    copyFiles(src, dest)
    convertFilesToJPGs(dest)
    removePictures(dest)

    
    removeDuplicates(wallpaperFolder, dest)



main()