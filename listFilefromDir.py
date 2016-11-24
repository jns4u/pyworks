import os

def listCurDirfile():
    #function considers current directory to list contents
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print f
    
def list_files(path):
    # returns a list of names (with extension, without full path) of all files in folder path    
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            print name    

listCurDirfile()
list_files("enter_dir_name_here")
