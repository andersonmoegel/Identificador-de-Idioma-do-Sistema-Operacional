# Operating System and Language Identifier

This script is a tool developed for enterprise use on platforms that execute scripts. It captures information about the operating system, including the Windows version and system language, and logs these details to a file.

## Features

- **Special Character Removal**: The script normalizes the system language string to remove special characters, ensuring clean data logging.
- **Information Logging**: Saves the Windows version and system language to a text file in the directory `C:\Windows\Temp\Idioma.txt`.
- **Error Handling**: Includes exception handling to deal with potential errors during file saving.

## Usage

To use the script, simply run it in a Python environment. The information will be automatically saved to the specified path.

### Reactivating the OS Name Display Feature

The feature that displays the operating system name is available but was hidden to meet specific requirements. To reactivate it, you can uncomment the corresponding line in the code:

```python
# Add this line to display the operating system name
# print(f"Operating System Name: {platform.system()}")
```

## Requirements

- Python 3.x  
- Standard libraries: `locale`, `os`, `platform`, `unicodedata`

## Execution

1. Ensure Python is installed on your machine.
2. Copy the code into a Python file (e.g., `save_language.py`).
3. Run the script using the terminal or command prompt:

   ```bash
   python idioma.py
   ```

## Contributions

Contributions are welcome! Feel free to submit pull requests or report issues.

## License

This project is free to use and has no license restrictions.
