import pathlib


files_folder = pathlib.Path("E:\LARPy - RPG\Zew Cthulhu")
print(files_folder)

#
# for f in list(files_folder.iterdir()):
#     print(f)

print("Folders:")
[print(f) for f in list(files_folder.iterdir()) if f.is_dir()]
print('*' * 20)
print('Files directly in:')
[print(f) for f in list(files_folder.iterdir()) if f.is_file()]
