import os
import shutil
import glob
import ctypes
import itertools
import string
import platform
sourceDirectoryPath = ""  # Enter directory name for source, make sure to add a backslash at the end
exelfilename = ""
def get_available_drives():
    if 'Windows' not in platform.system():
        return []
    drive_bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    return list(itertools.compress(string.ascii_uppercase,
               map(lambda x:ord(x) - ord('0'), bin(drive_bitmask)[:1:-1])))

###  Program starts here
def createLocalVersion(sourceDirectoryFiles, destinationLocation):
    for sourceFile in sourceDirectoryFiles:
        fileToCp = os.path.join(sourceDirectoryPath, sourceFile) 
        copyToDes(fileToCp, destinationLocation)

# The Copy function
def copyToDes(src, dest):
    try:
        shutil.copy(src, dest)
    except OSError:
        print("OsError PAssed")

def getSrcFiles(sourceDirectory):
    return glob.glob(sourceDirectory+"*")

def makeDestination():
    maindrive = get_available_drives()
    for i in maindrive:
        if os.access(i + r":\\", os.W_OK):
            maindrive = i+r":\\DataTest"
            print("The {0} path was acessible".format(maindrive))
            break
    if not os.path.isdir(maindrive):
        os.mkdir(maindrive)
        print("New Directory Made.")
    else:
        print("Files will be copied and destination files will be overwritten.")
        pass
    return maindrive

def main():
    destDir = makeDestination()
    createLocalVersion(getSrcFiles(sourceDirectoryPath), destDir)
    os.startfile(os.path.join(destDir, exelfilename))
    print("It has been moved and copied.")


main()
