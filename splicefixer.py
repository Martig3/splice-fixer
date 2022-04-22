import os
import shutil

directory = f'./Samples/Splice'
if not os.path.isdir(directory):
    print('Splice directory does not exist for this project')
    exit(0)
print(f'Copying files from \'{os.path.normpath(directory)}\'')
allDirectory = f'{directory}/_All'
if not os.path.isdir(allDirectory):
    os.mkdir(allDirectory)

filesCopied = 0
existingFilesFound = 0

for r, d, f in os.walk(directory):
    if len(f) > 0:
        for file in f:
            normPath = os.path.normpath(os.path.join(r, file))
            if normPath.count('_All') == 0:
                if not os.path.isfile(os.path.normpath(os.path.join(allDirectory, file))):
                    shutil.copy(normPath, os.path.normpath(os.path.join(allDirectory, file)))
                    filesCopied += 1
                else:
                    existingFilesFound += 1

print(f'Copied {filesCopied} files, found {existingFilesFound} existing files in \'_All\' folder')
