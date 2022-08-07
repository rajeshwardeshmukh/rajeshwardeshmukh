import os


def creat_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except Exception as error:
        print(error)

def main():
    folder_name = input("Enter Name of Folder : ")
    creat_folder(folder_name=folder_name)
    
if __name__ == "__main__":
    main()
    print("RAJESHWAR")
    print("BABURAO")
    print("DESHMUKH")
