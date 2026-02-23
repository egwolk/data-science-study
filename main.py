import os, sys

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except:
        print("file does not exist")

def input_file_name():
    file = input("Enter file name: ")
    return file + ".txt"

def write_file():
    pass
def append_file():
    pass
def rename_file():
    pass
def delete_file():
    pass


print("""
What would you like to do?
[1] Read a file
[2] Create a new file
[3] Add data to a file
[4] Rename a file 
[5] Delete a file
[6] Exit
""")
while True:
    user_input = input("Your choice: ")
    match user_input:
        case "1":
            file = input_file_name()
            read_file(file)
            break
        case "2":
            break
        case "3":
            break
        case "4":
            break
        case "5":
            break
        case "6":
            sys.exit("bye bye")
        case _:
            print("invalid input. try again")

print(f"You picked {user_input}")