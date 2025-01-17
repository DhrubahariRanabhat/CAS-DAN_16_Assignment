import string

def encrypt_text(file_path, output_path, n, m):
    def encrypt_char(c, n, m):
        if c.islower():
            return chr((ord(c) - ord('a') + n * m) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') + n * m) % 26 + ord('A'))
        else:
            return c

    try:
        with open(file_path, 'r') as file:
            raw_text = file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return

    encrypted_text = ''.join(encrypt_char(c, n, m) for c in raw_text)

    try:
        with open(output_path, 'w') as file:
            file.write(encrypted_text)
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        return

def decrypt_text(input_path, output_path, n, m):
    def decrypt_char(c, n, m):
        if c.islower():
            return chr((ord(c) - ord('a') - n * m) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') - n * m) % 26 + ord('A'))
        else:
            return c

    try:
        with open(input_path, 'r') as file:
            encrypted_text = file.read()
    except FileNotFoundError:
        print(f"Error: The file {input_path} does not exist.")
        return

    decrypted_text = ''.join(decrypt_char(c, n, m) for c in encrypted_text)

    try:
        with open(output_path, 'w') as file:
            file.write(decrypted_text)
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        return

def check_correctness(original_file, decrypted_file):
    try:
        with open(original_file, 'r') as orig_file:
            original_text = orig_file.read()

        with open(decrypted_file, 'r') as dec_file:
            decrypted_text = dec_file.read()

        return original_text == decrypted_text
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # User inputs for n and m
    try:
        n = int(input("Enter the value of n: "))
        m = int(input("Enter the value of m: "))
    except ValueError:
        print("Error: Both n and m must be integers.")
        exit(1)

    raw_file = "raw_text.txt"
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"

    # Encryption
    encrypt_text(raw_file, encrypted_file, n, m)
    print("Encryption complete. Encrypted text written to", encrypted_file)

    # Decryption
    decrypt_text(encrypted_file, decrypted_file, n, m)
    print("Decryption complete. Decrypted text written to", decrypted_file)

    # Check correctness
    if check_correctness(raw_file, decrypted_file):
        print("Success: Decrypted text matches the original text!")
    else:
        print("Error: Decrypted text does not match the original text.")