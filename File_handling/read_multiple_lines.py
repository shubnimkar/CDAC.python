try:
    file_open=open("new_file.txt","rt")
    if (file_open):
        print(file_open.read())

    file_open.close()
except FileNotFoundError:
    ch=input("File do not exists,do you want to create a new one?(Y/y): ").lower()
    if ch=='y':
        file_create=open("new_file.txt","w")
        file_create.write("HPCSA hello how are you \nHPCSA I am doing good")
        file_create.close()