# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import subprocess
import shutil
import json
def is_it_exception(path, exception):
    for e in exception:
        if e in path:
            return True
    return False
def switch_drive(source, destination,copy_existing, destination_onedrive,exception):
    # Use a breakpoint in the code line below to debug your script.
    # Iterate through directory
    for root, dirs, files in os.walk(source):
        for name in files:

            path = os.path.join(root, name)
            path_modified = path.replace(source, destination)
            if not copy_existing:
                if os.path.exists(path_modified):
                    continue
            dir_name = os.path.dirname(path_modified)
            try:
                os.makedirs(dir_name, exist_ok=True)
                shutil.copy(path, path_modified)

                if not is_it_exception(dir_name, exception):
                    subprocess.run('attrib +U -P "' + path + '"')
                if destination_onedrive:
                    subprocess.run('attrib +U -P "' + path_modified + '"')
            except Exception as e:
                with open("exception.txt", "a", encoding="utf-8") as f:
                    f.write("Exception au fichier : "+path+"\n")
def read_config():
    f = open("config.json", "r", encoding="utf-8")
    file = json.load(f)
    source = file["source"]
    destination = file["destination"]
    copy_existing = file["copy_existing"]
    destination_onedrive = file["destination_onedrive"]
    exception = file["exception"]

    return source, destination,copy_existing, destination_onedrive,exception

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    source, dest,copy_existing,destination_onedrive,exception = read_config()
    switch_drive(source, dest,copy_existing,destination_onedrive, exception)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
