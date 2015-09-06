import os


def get_file_list(dir, fileList):
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            new_dir = os.path.join(dir, s)
            get_file_list(new_dir, fileList);
    return fileList

import tarfile
tar = tarfile.open("E:/a.tar.gz")
tar.extractall()
tar.close()
