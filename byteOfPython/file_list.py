import os

root_path = "."


def file_list(root, depth):
    for fileA in os.listdir(root):
        file_path = root + "/" + fileA
        if fileA.startswith("."):
            print "\t"*depth+fileA
            continue
        if os.path.isdir(file_path):
            print "\t"*depth+fileA
            file_list(file_path, depth + 1)
        else:
            print "\t"*depth+fileA


file_list("/home/cc", 0)