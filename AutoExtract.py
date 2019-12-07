#!python3

from pathlib import Path
from zipfile import ZipFile
import os

print("start")

download_folder = str(Path.home()) + "\\Downloads\\"
files = os.listdir(download_folder)
print("download folder: ", download_folder)

files[:] = [f for f in files if f.endswith(".zip")] # only keeps .zip files
print("files: ", len(files))
print("files: ", files)

test_file = download_folder + files[2]
print("test obj: ", test_file)

for file in files:
    zippy = download_folder + file
    zf = ZipFile(zippy, "r")
    zf.extractall(download_folder)  # extract to download folder
zf.close()

# delete all .nfo files
new_files = os.listdir(download_folder)
for file in new_files:
    if file.endswith(".nfo"):
        os.remove(download_folder + file)

# TODO:
# maybe put extracted files in folders
# maybe put .srt files in special folder for quick access
# dont extract files that are already extracted
# auto delete old .zips
# let user chose if not to delete useless .nfo files
