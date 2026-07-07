import os
import glob

directory = "/Users/nadiairina/Desktop/adil móveis/tecidoss"
folders = os.listdir(directory)

for folder in sorted(folders):
    path = os.path.join(directory, folder)
    if os.path.isdir(path):
        files = sorted(os.listdir(path))
        print(f"{folder}: {files}")
