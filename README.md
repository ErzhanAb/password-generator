# Password Generator

## 📌 Description
This is a simple Python program that generates secure passwords based on user-defined criteria. The user can specify the number of passwords, length, and character types to include. Additionally, the generated passwords can be saved to a file.

## 🚀 Features
- Generate multiple passwords at once
- Specify password length
- Choose which characters to include:
  - Numbers (0-9)
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Special characters (!#$%&*+-=?@^_)
- Option to save passwords to a file
- Option to generate new passwords repeatedly

## 🛠️ Requirements
- Python 3.x

## 🔧 Installation
No installation required. Just download the script and run it using Python.

## 🔄 Deployment
1. **Clone the repository**  
   ```bash
   git clone https://github.com/ErzhanAb/password-generator.git
   ```
2. **Navigate to the project folder**  
   ```bash
   cd password-generator
   ```

## ▶️ Usage
1. Run the script:
   ```bash
   python app.py
   ```
2. Follow the on-screen prompts:
   - Enter the number of passwords to generate.
   - Specify the length of each password.
   - Choose character types to include (yes/no inputs).
   - Choose whether to save the passwords to a file.
3. View the generated passwords.
4. If chosen, passwords will be saved in `passwords.txt`.
5. Repeat the process if needed.

## 📷 Example Output
```
Welcome to the password generator!
==================================================
Enter the number of passwords to generate: 3
Enter the password length (number of characters): 10
Should the password contain the numbers 0123456789? yes
Should the password contain uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? yes
Should the password contain lowercase letters abcdefghijklmnopqrstuvwxyz? yes
Should the password contain the characters !#$%&*+-=?@^_? no
Do you want to save passwords to a file? yes

==================================================
Generated passwords: 3
P3dL5z7YxQ
B2aM8wT9cX
Y6tP4rV7bN

Passwords have been saved to passwords.txt
==================================================
Generate passwords again? (Yes/No): no
==================================================
The program has successfully finished. See you next time!
```

## 📜 License
This project is free to use and modify.

## 💡 Notes
- If no character types are selected, the program will prompt the user to try again.
- The password length must be a positive integer.
- If the user chooses to save passwords, they will be stored in `passwords.txt` in the script directory.

Enjoy secure password generation! 🔒