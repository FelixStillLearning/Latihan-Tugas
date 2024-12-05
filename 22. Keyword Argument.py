#Keyword Argument = menentukan urutan argumen yang akan dikirim ke fungsi yang ada
#                       Keyword argument harus diletakkan setelah positional argument
#                       Keyword argument tidak boleh diletakkan sebelum positional argument 
#                       Keyword argument hanya boleh diletakkan sekali

def hello (first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last="Corleone", middle="Angga", first="Jokowi")