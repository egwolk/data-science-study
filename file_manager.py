import os

class FileManager:
    """FileManager
    A class that holds all file manipulation functions."""
    def read_file(self, filename):
        """read_file
            A function that uses open() r operation to read txt file contents."""
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    
    def write_file(self, filename, content):
        """write_file
        A function that uses open() w operation which then calles writelines() to allow writing of multiple lines into a new txt file."""
        with open(filename, "w") as file:
            file.writelines(content)
    
    def append_to_file(self, filename, content):
        """append_to_file
        A function that uses open() a operation which also uses writelines() to append data to an already exixting txt file."""
        with open(filename, "a") as file:
            file.writelines(content)
    
    def rename_file(self, old_name, new_name):
        """rename_file
        A function that uses os.rename to rename existing txt files."""
        os.rename(old_name, new_name)
    
    def delete_file(self, filename):
        """delete_file
        A function that uses os.remove to delete existing txt files."""
        os.remove(filename)
    
    def file_exists(self, filename):
        """file_exists
        A function that uses os.path.exists to check if the text file exisist."""
        return os.path.exists(filename)