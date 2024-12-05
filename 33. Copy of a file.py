''' 
copy of a file

copyfile() = copies content of a file
copy() = copyfile() + permission mode + destination file
copy2() = copy() + copies metadata (file's creation and modification times)

'''
import shutil    #importing the shul

shutil.copy ('32a.file.txt','33a.file.txt')
shutil.copy2 ('32a.file.txt','C:\\Users\\Felix Corleone\\Documents')
