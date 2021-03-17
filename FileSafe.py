
# TODO:
# (done) create encryptor feature
# (done) Create feature to save password with file
# create unlock feature
# create feature that detects colons in the file name


from tkinter import *
# from tkinter.filedialog import askdirectory
from tkinter import filedialog
# import os
# from PIL import Image, ImageTk
import cryptography
from cryptography.fernet import Fernet

root = Tk()
path = ""
key = 'TJVxHBrFD6Clmecsek6ZANrxwrLpDamj0yT7qP4PNSg='

e = Entry(root, width=35, borderwidth=5)
l = Label(root, text = "Type in your password (up to 128 characters): ", padx = 30, pady = 20)

def removeScreenElements():
    global l2
    global b

    l2.grid_remove()
    b.grid_remove()
    return

l2 = Label(root, text = "Your file has been successfully encrypted ", padx = 30, pady = 20)
b = Button(root, text = "OK", command = removeScreenElements, padx = 30, pady = 20)

def browseFiles():
    global path
    global e
    global l
    path = filedialog.askopenfilename(title='Select File to be Encrypted')
    print('path:', path)
    l.grid(row = 6, column = 1)
    e.grid(row = 6, column = 2)


def encrypt():
    # declare global variables
    global path
    global e
    global key
    global l
    global l2
    global b
    
    # gets user password from input box
    password = e.get()
    # makes new key with combination of pre-generated key and user password
    new_key = password + key[len(password):]
    # makes Fernet encryptor object
    f = Fernet(bytes(new_key, 'utf-8'))
    
    # reads in file to be encrypted
    with open(path, 'rb') as original_file:
        original = original_file.read()
    
    #encrypts file
    encrypted = f.encrypt(original)

    # manipulates path variable for password storage/recovery
    arr = path.split('/')
    arr[-1] = 'e_' + arr[-1]
    path = ''

    for item in arr:
        if item == '':
            continue
        path = path + '/' + item
    
    # writes encrypted file out to same directory as original file was
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


    # with open('keys.key', 'a') as mykey:
    #     mykey.write(path + ':' + str(new_key) + '\n')
    
    e.grid_remove()
    l.grid_remove()
    l2.grid(row = 10, column = 1)
    b.grid(row = 11, column = 1)

    return

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
root.title('File Encryptor')
# root.geometry(str(screen_width) + 'x' + str(screen_height))

root.geometry('1000x650')

label_file_explorer1 = Label(root, text = "File Encryptor", padx = 30, pady = 20)
label_file_explorer2 = Label(root, text = "Directions:", padx = 30, pady = 20)
label_file_explorer3 = Label(root, text = "Use the \"Browse Files\" button below to choose a file", padx = 30, pady = 20)
label_file_explorer4 = Label(root, text = "Right after you choose it, click \"Encrypt!\" to encrypt the file.", padx = 30, pady = 20)

button_explore = Button(root, text = "Choose a file", command = browseFiles, padx = 30, pady = 20)


button_encrypt = Button(root, text = "Encrypt!", command = encrypt, padx = 30, pady = 20)

label_file_explorer1.grid(column = 1, row = 1)
label_file_explorer2.grid(column = 1, row = 2)
label_file_explorer3.grid(column = 1, row = 3)
label_file_explorer4.grid(column = 1, row = 4)

button_explore.grid(column = 1, row = 5)
button_encrypt.grid(column = 1, row = 7)


root.mainloop()
