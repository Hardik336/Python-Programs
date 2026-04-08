import zipfile

def zipFile():
    pass

# 10) Write a program to zip and unzip particular files.

import zipfile

# ZIP
files=r"Unit 2\Practice2_9.py"

with zipfile.ZipFile("zipfile.zip","w") as z:
    z.write(files)

print("Zip Successfully")

# UNZIP
import zipfile

with zipfile.ZipFile("zipfile.zip","r") as z:
    z.extractall("Unit2")
    
print("ZIP exctracted")