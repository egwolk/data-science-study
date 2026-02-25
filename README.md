# Data Science: TXT File Management System

A simple Python-based file management system built to study, understand, and demonstrate text file manipulation in Python. This educational project provides an interactive command-line interface for creating, reading, updating, and deleting `.txt` files.

## Description

This project was developed for educational purposes to demonstrate fundamental file operations in Python. It features a clean separation of concerns with a [`FileManager`](file_manager.py) class handling file I/O operations and a [`UIManager`](ui_manager.py) class managing the user interface.

## Features

- **Read files**: View the contents of existing `.txt` files
- **Create files**: Write new text files with multi-line content
- **Append data**: Add content to existing files
- **Rename files**: Change file names
- **Delete files**: Remove files from the system
- **Built-in documentation**: View program documentation directly from the interface

## Technologies Used

- **Python 3.10+** (uses `match-case` statements)
- **PyInstaller** - For building standalone executables

## Installation & Usage

### Running from Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/egwolk/python-txt-file-management.git
   cd data-science-study
   ```

2. **Run the program**:
   ```bash
   python main.py
   ```

   The program will start and display an interactive menu where you can select options 1-7.

### Building an Executable with PyInstaller

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**:
   ```bash
   pyinstaller --onefile --name "Text File Manager" main.py
   ```

   The executable will be created in the `dist/` directory.

   **Alternative**: Use the existing spec file:
   ```bash
   pyinstaller "Text File Manager.spec"
   ```

3. **Run the executable**:
   ```cmd
   dist\Text File Manager.exe
   ```

### Installing Pre-built Executable (Windows)

1. Go to the [Releases](https://github.com/egwolk/python-txt-file-management/releases) page
2. Download `Text File Manager.exe`
3. Double-click to run, or open Command Prompt and run:
   ```cmd
   "Text File Manager.exe"
   ```

## Project Structure

```
data-science-study/
├── main.py                    # Entry point of the application
├── file_manager.py            # File operations class
├── ui_manager.py              # User interface class
├── Text File Manager.spec     # PyInstaller configuration
├── README.md                  # Project documentation
├── build/                     # PyInstaller build files
└── dist/                      # Compiled executables
```

## How to Use

1. Run the program using one of the methods above
2. Select an option from the menu (1-7):
   - **[1]** Read a file - View contents of an existing file
   - **[2]** Create a new file - Write content to a new file
   - **[3]** Add data to a file - Append content to an existing file
   - **[4]** Rename a file - Change the name of an existing file
   - **[5]** Delete a file - Remove a file
   - **[6]** Read program docs - View built-in documentation
   - **[7]** Exit - Close the program

3. Follow the on-screen prompts for each operation
4. File names without `.txt` extension will automatically have it added

## Requirements

- **Windows 10 or later** (for pre-built executable)
- **Python 3.10 or higher** (for running from source - uses `match-case` syntax)
- No external dependencies for running from source
- PyInstaller required only for building executables

---
## License

This project is for educational purposes.

## Author

made with 💗 [@egwolk](https://github.com/egwolk)
