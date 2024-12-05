'''
Writing File using python
'''

text = "ini adalah file yang dibuat menggunakan pyhton\nkeren kan?\njangan lupa kasih afirmasi kediri sendiri\n"
with open ('34. file.txt','w') as file:
    file.write(text)