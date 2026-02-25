import os, sys

class UIManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_file(self, filename, contents):
        print(f"{filename} contents:")
        for line in contents:
            print(line)
        input("Press enter key to continue...")
    
    def display_menu(self):
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
        file = input(prompt).strip()
        if file.endswith(".txt"):
            return file
        return file + ".txt"
    
    def get_file_content(self):
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
        self.clear_console()
        filename = self.input_file_name()
        try:
            contents = self.file_manager.read_file(filename)
            self.display_file(filename, contents)
        except FileNotFoundError:
            print("file does not exist")
            input("Press enter key to continue...")
    
    def handle_create_file(self):
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
        self.clear_console()
        filename = self.input_file_name()
        
        try:
            self.file_manager.delete_file(filename)
            print("File removed successfully.")
            input("Press enter to continue...")
        except FileNotFoundError:
            print("file does not exist")
            input("Press enter key to continue...")
    
    def run(self):
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
                    self.clear_console()
                case "7":
                    self.clear_console()
                    sys.exit("bye bye")
                case _:
                    print("invalid input. try again")
                    input("Press enter to continue...")