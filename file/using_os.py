import os

try:
    os.mkdir("file/log")
except FileExistsError as e :
    print("Already created")