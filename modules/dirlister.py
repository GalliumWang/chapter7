import os

def run(**args):
    print("dirlister running..")
    files=os.listdir(".")
    return str(files)