from mega import Mega
import os

mega = Mega()
mega.login('email','password')

print("Successful")

def absoluteFilePaths(directory):
     for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

directory = 'path/to/folder' #change it with the folder in your local
file_path_generator = absoluteFilePaths(directory)

Folder = mega.find('your_folder') #change it with the folder in your mega
for file_path in file_path_generator:
    mega.upload(file_path, Folder[0])