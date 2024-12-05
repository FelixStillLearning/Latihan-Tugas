#**Kwargs = parameter that will pack all arguments into a dictionary
#         useful so that a function can accept a varying amount of keyword arguments

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "felix", lname = "angga")  

def x(**kwargs):
    print("My name is " + kwargs["nama_depan"] + " " + kwargs["nama_tengah"] + " " + kwargs["nama_belakang"])

x(nama_depan="felix", nama_tengah="angga", nama_belakang="resky")

def perpustakaan (**rak_1): 
    for rak in rak_1.items():
        print ("ini buku ada di rak " + rak[0] + " " + rak[1])

perpustakaan (rak_1="buku 1", rak_2="buku 2", rak_3="buku 3", rak_4="buku 4")

def dictionary (**kamus):
    for kata in kamus.items():
        print ("ini kata ada di kamus " + kata[0] + " " + " : "+ kata[1])

dictionary (bab_1="saya", bab_2="lahir", bab_3="jalan", bab_4="makan")

def borrow_books(**library):
    # Check if the required books are available in the library
    book_1 = library.get("buku_1")
    book_2 = library.get("buku_2")
    
    if book_1 and book_2:
        print(f"Saya pinjam buku {book_1} dan pinjam buku {book_2}.")
    else:
        print("Salah satu atau kedua buku tidak tersedia.")

# Example usage
borrow_books(buku_1="Harry Potter", buku_2="Lord of the Rings")
