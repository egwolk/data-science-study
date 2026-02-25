import os, sys

def read_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def display_file(filename, contents):
    print(f"{filename} contents:")
    for line in contents:
        print(line)
    input("Press enter key to continue...")

def input_file_name(prompt="Enter txt file name: "):
    file = input(prompt).strip()
    if file.endswith(".txt"):
        return file
    return file + ".txt"

def write_file(filename):
    if os.path.exists(filename):
        print(f"File with name {filename} already exists.\nOverwrite file?")
        while True:
            yn = input("Y|N: ").lower().strip()
            match yn:
                case "y":
                    file_writer(filename)
                    break
                case "n":
                    print("operation cancelled")
                    input("Press enter key to continue...")
                    break
                case _:
                    print("invalid input. Try again")
    else: file_writer(filename)

def file_content():
    content = []
    clear_console()
    print("Start writing your file content [press enter twice to finish]:")
    while True:
        line = input()
        if line:
            content.append(line + "\n")
        else: break
    return content

def file_writer(filename):
    content = file_content()
    with open(filename, "w") as file:
        file.writelines(content)
    clear_console()
    contents = read_file(filename)
    display_file(filename, contents)          
    

def append_file(filename):
    clear_console()
    read_file(filename)
    content = file_content()
    with open(filename, "a") as file:
        file.writelines(content)
    clear_console()
    print(f"{filename} with appended data:\n")
    contents = read_file(filename)
    display_file(filename, contents)

def file_checker(choice, filename):
    try:
        match choice:
            case "1": 
                contents = read_file(filename)
                display_file(filename, contents)
            case "3": append_file(filename)
            case "4": rename_file(filename)
            case "5":delete_file(filename)
    except:
        print("file does not exist")
        input("Press enter key to continue...")

def rename_file(filename):
    os.rename(filename, input_file_name(prompt="Enter new file name: "))
    print("File renamed successfully.")
    input("Press enter to continue...")

def delete_file(filename):
    os.remove(filename)
    print("File removed successfully.")
    input("Press enter to continue...")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("""
What would you like to do?
[1] Read a file
[2] Create a new file
[3] Add data to a file
[4] Rename a file 
[5] Delete a file
[6] Read program docs
[7] Exit
""")

def user_operation():
    while True:
        user_input = input("Your choice: ")
        match user_input:
            case "1":
                clear_console()
                file = input_file_name()
                file_checker(user_input, file)
                break
            case "2":
                clear_console()
                file = input_file_name()
                write_file(file)
                break
            case "3":
                clear_console()
                file = input_file_name()
                file_checker(user_input, file)
                break
            case "4":
                clear_console()
                file = input_file_name()
                file_checker(user_input, file)
                break
            case "5":
                clear_console()
                file = input_file_name()
                file_checker(user_input, file)
                break
            case "6":
                clear_console()
                break
            case "7":
                clear_console()
                sys.exit("bye bye")
            case _:
                print("invalid input. try again")

while True:
    clear_console()
    display_menu()
    user_operation()

    
        
