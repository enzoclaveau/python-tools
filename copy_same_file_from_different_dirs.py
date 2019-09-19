import os
import sys
import logging
import shutil



def read_arguments():

    arguments = list()

    try:
        arguments.append(str(sys.argv[1]))
    except IndexError:
        logging.error('No folder is given')
        sys.exit()

    try:
        arguments.append(str(sys.argv[2]))
    except IndexError:
        logging.error('No configuration file name given')
        sys.exit()

    return  arguments

def get_versions(path: str):

    versions = list()

    for subdir, dirs, files in os.walk(path):
        for dir_name in dirs:
            dir_path = os.path.join(subdir, dir_name)
            if os.path.isdir(dir_path):
                version = dir_name[-5:]
                versions.append(version)
        break

    return versions

def get_all_files(path: str, config_file_name: str):

    config_files = list()

    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file == config_file_name:
                config_file = os.path.join(subdir, file)
                config_files.append(config_file)

    return config_files

def copy_all_files(path: str, files):

    versions = get_versions(path)

    for i, file in enumerate(files):
        new_file_name = os.path.basename(file) + versions[i]
        dst = os.path.join(path, new_file_name)
        shutil.copyfile(file, dst)

if __name__ == "__main__":

    args = read_arguments()
    folder = args[0]
    file_name = args[1]

    files = get_all_files(folder, file_name)
    copy_all_files(folder, files)
