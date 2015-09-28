import os
import shutil


def change_name(path):
    files = os.listdir(path)
    for file_name in files:
        strs = file_name.split('_')
        if len(strs) == 2:
            shutil.move(file_name, strs[1])


if __name__ == '__main__':
    change_name('./')
