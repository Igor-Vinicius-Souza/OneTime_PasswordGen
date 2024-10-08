# One Time Password Generator

This is a simple One Time Password Generator application built using Python and Tkinter. It generates random passwords based on user-defined criteria and allows users to save their generated passwords securely using encryption.

## Features

- **Generate Passwords**: Create random passwords with user-specified lengths and options to include special characters.
- **Save Passwords**: Store generated passwords securely in an encrypted file.
- **View Saved Passwords**: Open a separate window to view saved passwords, which are decrypted and displayed.
- **Clipboard Functionality**: Automatically copy the generated password to the clipboard for easy use.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `cryptography` library

## Installation

1. **Clone the repository**:
```bash
   git clone https://github.com/Igor-Vinicius-Souza/OneTime_PasswordGen.git
   cd OneTimePasswordGenerator
```
2. **Install the required library**:

```bash
    pip install cryptography
```

## Usage

1. Run the application:

```bash
    python passgen.py
```

2. Enter the desired app name and password length.

3. Choose whether to include special characters in the generated password.

4. Click "Generate Password" to create a password.

5. The generated password will be displayed in a dialog and copied to your clipboard.

6. Click "View Saved Passwords" to open a window displaying all previously saved passwords.

## File Structure

```bash
    OneTimePasswordGenerator/
    │
    ├── passgen_upd.py          # Main application code
    ├── passwords.enc           # Encrypted file containing saved passwords
    └── secret.key              # Encryption key for password encryption
```
## Security Considerations

- Passwords are encrypted before being saved to ensure they cannot be easily accessed by unauthorized users.
- The encryption key is stored in a separate file, which should be kept secure.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements.

