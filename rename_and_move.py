import os
from shutil import copyfile
from shutil import rmtree
import sys


def create_dir_if_not_exists(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Dir already exists")
    else:
        print("successfully created dir {}".format(path))


def remove_file_if_exists(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            rmtree(path)
        else:
            os.remove(path)


def get_dst(path):
    if "large" in path:
        return "large"
    elif "small" in path:
        return "small"
    else:
        return ""


def rename_file(path):
    parts = path.split(".")
    names = parts[0].split("_")

    new_name = ""
    for i in range(len(names) - 2):
        new_name += names[i] + "_"

    return new_name[:len(new_name) - 1] + "." + parts[1]


def create_small_and_large_dirs():
    remove_file_if_exists("small")
    create_dir_if_not_exists("small")
    remove_file_if_exists("large")
    create_dir_if_not_exists("large")

    files = os.listdir("test_files_1")
    for f in files:
        dst = get_dst(f)
        if len(dst) > 0:
            copyfile(f'test_files_1/{f}', f'{dst}/{rename_file(f)}')


def move_files():
    pass


# args = sys.argv
# if len(args) == 1:
#     print("Please provide the path to the reader_app")
# else:
create_small_and_large_dirs()
