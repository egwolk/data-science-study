import os

class FileManager:
    def read_file(self, filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    
    def write_file(self, filename, content):
        with open(filename, "w") as file:
            file.writelines(content)
    
    def append_to_file(self, filename, content):
        with open(filename, "a") as file:
            file.writelines(content)
    
    def rename_file(self, old_name, new_name):
        os.rename(old_name, new_name)
    
    def delete_file(self, filename):
        os.remove(filename)
    
    def file_exists(self, filename):
        return os.path.exists(filename)