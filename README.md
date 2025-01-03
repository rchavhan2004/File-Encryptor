# 🔐 File Encryptor Project

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2917/2917995.png" alt="Encryption Icon" width="120">
</p>

<p align="center">
  <strong>🔒 A Secure Way to Encrypt and Decrypt Your Files</strong>
</p>

---

## ⚡ Overview

The **File Encryptor** project is a Python-based tool that leverages the `cryptography` library to securely encrypt and decrypt files. It ensures that sensitive data is protected with strong encryption algorithms, making it ideal for personal and professional use.

### ✨ Features:
- 🔑 **Key Generation**: Creates a unique encryption key.
- 💾 **Save & Load Keys**: Easily store and retrieve keys.
- 🔐 **File Encryption**: Encrypts any file into a secure format.
- 🔓 **File Decryption**: Restores encrypted files to their original state.

---

## 🛠 Technologies Used

- 🐍 **Python**
- 🛡 **Cryptography Library**

---

## 🧩 How It Works

1. **Generate Key**:
   - Creates a unique encryption key using `Fernet.generate_key()`.

2. **Save and Load Key**:
   - Saves the key to a file (`encryption_key.key`) and retrieves it as needed.

3. **Encrypt File**:
   - Reads the file, encrypts its contents, and saves the result as `encrypted_file.txt`.

4. **Decrypt File**:
   - Reverts the encrypted data back to its original state and saves it as `decrypted_file.txt`.

---

## 🎨 Example Use Case

### Encrypting a File:
1. Place your target file (e.g., `noodles.txt`) in the same directory as the script.
2. Run the script to generate the encrypted file (`encrypted_file.txt`).

### Decrypting the File:
1. Use the saved encryption key.
2. Run the script to decrypt the file back to its original form (`decrypted_file.txt`).

---

<p align="center">
  <strong>🔒 Encrypt. Secure. Protect. 🔓</strong>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/04211271-83ef-4cb3-b5bc-1cc0b1609331" alt="Secure Icon" width="80">
</p>
