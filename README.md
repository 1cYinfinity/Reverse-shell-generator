# Reverse Shell Script Generator

This Python script generates various types of reverse shell scripts based on user input. It supports generating reverse shell scripts in several languages, including Bash, Python, PHP, Perl, PowerShell, Ruby, JavaScript (Node.js), Java, Lua, Netcat (nc), Shellcode, ASP, and C#.

## Features

- **Generate Reverse Shell Scripts:** Create reverse shell scripts in multiple languages.
- **Obfuscation Options:** Optionally obfuscate PowerShell scripts for added stealth.
- **Netcat Listener:** Start a Netcat listener for immediate testing if Netcat is selected.

## Prerequisites

- Python 3.x
- Netcat (for Netcat reverse shell and listener)

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/1cYinfinity/reverse-shell-generator.git
   ```
2. **Navigate to the project directory:**
   ```
   cd reverse-shell-generator
   ```
## Usage
1. **Run the script:**
   ```
   python generate_reverse_shell.py
   ```
2. **Follow the prompts:**

   ~ Select the type of reverse shell you want to generate. </br>
   ~ Specify the IP address and port for the reverse shell connection (default values are provided).</br>
   ~ Choose whether to add obfuscation (only applicable for PowerShell reverse shells).</br>
   
3. Check the generated script file in the current directory. The file will be named according to the selected reverse shell type.</br>
 
4. (Optional) If you selected Netcat (nc) as the reverse shell type, you will be prompted to start a Netcat listener to receive connections.</br>

## Example
Here's an example of generating a Python reverse shell:
  ```
  python generate_reverse_shell.py
  ```
    ~ Select option: 2 (Python) 
    ~ Enter IP address: 192.168.1.10 
    ~ Enter port: 5555 
    ~ Add obfuscation? no 
This will generate a Python reverse shell script saved as reverse_shell_python_reverse_shell.py.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This script is intended for educational purposes and ethical hacking scenarios only. Unauthorized use of this script can result in severe legal consequences. Always ensure you have proper authorization before using it.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## Contact
For any questions or support, please reach out to [baraiprince0111@gmail.com].
