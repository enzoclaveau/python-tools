import os
import sys
import shutil
import logging

def delete_pychache_from_all_sub_dirs_in_folder(path: str):
    for subdir, dirs, files in os.walk(path):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.abspath(os.path.join(subdir, dir_name))
                try:
                    shutil.rmtree(dir_path)
                except Error as error:
                    logging.error('Could not delete: ' + dir_path + 'Because: ' + error)


if __name__ == "__main__":

    try:
        folder = str(sys.argv[1])
    except IndexError:
        logging.error('No folder is given')
        sys.exit()

    if os.path.exists(folder):
        delete_pychache_from_all_sub_dirs_in_folder(folder)
    else:
        logging.error(f'{folder} doesn\'t exist')
