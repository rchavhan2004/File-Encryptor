from cryptography.fernet import Fernet

def genrate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    with open(key_file, "wb") as file:
        file.write(key)

def load_key(key_file):
    with open(key_file, "rb") as file:
        return file.read()

def encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    key = genrate_key()
    key_file = "encryption_key.key"
    save_key(key, key_file)

    input_file = "noodles.txt"
    encrypted_file = ("encrypted_file.txt")
    decrypted_file = ("decrypted_file.txt")

    encrypt_file(input_file, encrypted_file, key)
    print("File '{input_file}' encrypted to '{encrypted_file}'")

    decrypt_file(encrypted_file, decrypted_file, key)
    print("File '{encrypted_file}' decrypted to '{decrypted_file}'")

