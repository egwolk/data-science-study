import os, sys

class UIManager:
    """UIManager
    A class that holds all user interface fucntions."""
    def __init__(self, file_manager):
        self.file_manager = file_manager
    
    def clear_console(self):
        """clear_console
        A function that uses os.system to clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_file(self, filename, contents):
        """display_file
        A function that uses a for loop to display the contents of a txt file, line-by-line."""
        print(f"{filename} contents:")
        for line in contents:
            print(line)
        input("Press enter key to continue...")
    
    def display_menu(self):
        """display_menu
        A function that uses print to display the main menu."""
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
    
    def input_file_name(self, prompt="Enter txt file name: "):
        """input_file_name
        A function that propmts the user to input their file name and uses an if statement to check if the user includes .txt at the end of their input."""
        file = input(prompt).strip()
        if file.endswith(".txt"):
            return file
        return file + ".txt"
    
    def get_file_content(self):
        """get_file_content
        A function that stores user input into a list to allow multi-line inputs when writing/appending to txt files."""
        content = []
        self.clear_console()
        print("Start writing your file content [press enter twice to finish]:")
        while True:
            line = input()
            if line:
                content.append(line + "\n")
            else:
                break
        return content
    
    def confirm_overwrite(self, filename):
        """confirm_owverite
        A function that asks the user if they want to overwrite an existing file that matches the file name they inputed when they choose to write a new file."""
        while True:
            self.clear_console()
            print(f"File with name {filename} already exists.\nOverwrite file?")
            yn = input("Y|N: ").lower().strip()
            match yn:
                case "y":
                    return True
                case "n":
                    print("operation cancelled")
                    input("Press enter key to continue...")
                    return False
                case _:
                    print("invalid input. Try again")
                    input("Press enter key to continue...")
    
    def handle_read_file(self):
        """handle_read_fiel
        A function that calls functions related to reading files."""
        self.clear_console()
        filename = self.input_file_name()
        try:
            contents = self.file_manager.read_file(filename)
            self.display_file(filename, contents)
        except FileNotFoundError:
            print("file does not exist")
            input("Press enter key to continue...")
    
    def handle_create_file(self):
        """handle_create_file
        A function that calls functions related to writing files."""
        self.clear_console()
        filename = self.input_file_name()
        
        if self.file_manager.file_exists(filename):
            if not self.confirm_overwrite(filename):
                return
        
        content = self.get_file_content()
        self.file_manager.write_file(filename, content)
        self.clear_console()
        contents = self.file_manager.read_file(filename)
        self.display_file(filename, contents)
    
    def handle_append_file(self):
        """handle_append_file
        A function that calls functions related to appending files."""
        self.clear_console()
        filename = self.input_file_name()
        
        try:
            contents = self.file_manager.read_file(filename)
            self.display_file(filename, contents)
            
            content = self.get_file_content()
            self.file_manager.append_to_file(filename, content)
            
            self.clear_console()
            print(f"{filename} with appended data:\n")
            contents = self.file_manager.read_file(filename)
            self.display_file(filename, contents)
        except FileNotFoundError:
            print("file does not exist")
            input("Press enter key to continue...")
    
    def handle_rename_file(self):
        """handle_rename_files
        A function that calls functions related to renaminng files."""
        self.clear_console()
        old_filename = self.input_file_name()
        
        try:
            new_filename = self.input_file_name(prompt="Enter new file name: ")
            self.file_manager.rename_file(old_filename, new_filename)
            print("File renamed successfully.")
            input("Press enter to continue...")
        except FileNotFoundError:
            print("file does not exist")
            input("Press enter key to continue...")
    
    def handle_delete_file(self):
        """handle_delete_file
        A function that calls funcions related to deleting files."""
        self.clear_console()
        filename = self.input_file_name()
        
        try:
            self.file_manager.delete_file(filename)
            print("File removed successfully.")
            input("Press enter to continue...")
        except FileNotFoundError:
            print("file does not exist")
            input("Press enter key to continue...")

    def docs(self):
        """docs
        A fucntion that displays the program documentation."""
        self.clear_console()
        print("""Program Documentation
              This program was built to study and understant file management in python.""")
        print(f"""
{self.file_manager.__doc__}
{self.file_manager.read_file.__doc__}
{self.file_manager.write_file.__doc__}
{self.file_manager.append_to_file.__doc__}
{self.file_manager.rename_file.__doc__}
{self.file_manager.delete_file.__doc__}
{self.file_manager.file_exists.__doc__}

{self.__doc__}
{self.clear_console.__doc__}
{self.display_file.__doc__}
{self.display_menu.__doc__}
{self.input_file_name.__doc__}
{self.get_file_content.__doc__}
{self.confirm_overwrite.__doc__}
{self.handle_read_file.__doc__}
{self.handle_create_file.__doc__}
{self.handle_append_file.__doc__}
{self.handle_rename_file.__doc__}
{self.handle_delete_file.__doc__}
{self.docs.__doc__}
{self.run.__doc__}
""") 
        input("Press enter key to continue...")
    
    def run(self):
        """run
        A function that uses a while loop to allow the program to run until the user explicitly chooses to exit."""
        while True:
            self.clear_console()
            self.display_menu()
            
            user_input = input("Your choice: ")
            match user_input:
                case "1":
                    self.handle_read_file()
                case "2":
                    self.handle_create_file()
                case "3":
                    self.handle_append_file()
                case "4":
                    self.handle_rename_file()
                case "5":
                    self.handle_delete_file()
                case "6":
                    self.docs()
                case "7":
                    self.clear_console()
                    sys.exit("bye bye")
                case _:
                    print("invalid input. try again")
                    input("Press enter to continue...")
