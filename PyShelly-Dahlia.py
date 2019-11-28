# Camden Bruce
# Noah Cain
import os
import shutil
# import /system/zircon.py

def Delete():          #Deleting a File
    path=input("Enter the location of file to be written or created")
    if os.path.exists(path):      # checks if the file exists
        print('File Found')     #For existing file
        os.remove(path)          #os.remove(file path) is used to delete
        print('File has been deleted')
    else:
        print('File Does not exist')    #Is no file exist

def Dirlist():      #Listing files in a directory
    path=input("Enter the Directory location to list:")
    sortlist=sorted(os.listdir(path))       #Sorting and listing files
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1
        

def Move():        #For moving or renameing file
    path1=input('Enter the location of File to move or rename:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the resulting location with resulting file name:')
        shutil.move(path1,path2)
        print('File renamed')
    if mr==2:
        path2=input('Enter the location to move:')
        shutil.move(path1,path2)
        print('File moved')

def Copy():       #For copying
    path1=input('Enter the location of File to copy or rename:')
    path2=input('Enter the location to copy:')
    shutil.copy(path1,path2)
    print('File copied')

def Makedir():            #For creating directory
    path=input("Enter the directory name with location to make \neg. /zircon/system/bin/newdir \nWhere newdir is new directory:")
    os.makedirs(path) 
    print('Directory Created')

def Removedir():             #For removing Directory
    path=input('Enter the location of Directory:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()

def Help():
    print('''
move (move files)

copy (copy files)

delete (delete files)

Dirlist (list files in a directory)

bash (use bash shell) (if supported)

sh (use sh shell) (if supported)

python3 (open a python3 shell)

exit (exit this shell)

pm (zircon ProcessManager)
''')

while True:
    ans = input('''
PyShelly - ENV Dahlia

type help for more information

$ ''')
    if ans == 'help':
        Help()
        
    if ans == 'exit':
        exit()
        
    if ans == 'move':
        Move()
        
    if ans == 'copy':
        Copy()

    if ans == 'delete':
        Delete()

    if ans == 'Dirlist':
        Dirlist()

    if ans == 'makedir':
        Makedir()

    if ans == 'removedir':
        Removedir()

    if ans == 'bash':
        os.system("bash")

    if ans == 'sh':
        os.system("sh")

    if ans == 'python3':
        os.system("python3")

    if ans == 'pm reboot':
        os.system("pm reboot")

    if ans == 'fxutils':
        os.system("fxutils")
        
    if ans == 'pm shutdown':
        os.system("pm shutdown")
