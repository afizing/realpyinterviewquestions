import os, shutil 
def move_files(source, destination, filetype):
    os.chdir(source)
    count = 0
    for file_name in os.listdir('.'):
        if file_name.endswith(filetype):
            shutil.move(file_name, destination)
            count +=1
    print("Total %i files moved"%count) 


source = raw_input("enter source folder complete path ++ ")
dest = raw_input("enter destination folder complate path ++ ")
filetype = raw_input("enter file type ex: .exe | .pdf |.txt ++ ") 
move_files(source, dest, filetype) 
        
    
