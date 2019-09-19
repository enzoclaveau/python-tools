# python-tools
Some easy reusable code to automate stuff


## Delete all the \_\_pycache\_\_ folders from project
In case you want to delete all the generated \_\_pychache\_\_ folders from your local project run this file:

    python delete_pycache.py [folder_name]

## Copy all files with the same name from different directories
In case you want to compare files from different directories (let's say the configuration files across different versions of your program) then you can use this script to copy them all to the same directory:
Place all the directories you want to compare in the same directory and run:

    python copy_same_file_from_different_dirs.py [directory_name] [file_name]

It will go through all the directories in [directory_name] and look for files with the name [file_name] and copy them to the [directory_name]. To avoid name conflicts the last five characters of each directory in [directory_name] are taken and put behind the file name (the last five, because in my case these were the version number x.y.z placed at the end of each directory name). 
