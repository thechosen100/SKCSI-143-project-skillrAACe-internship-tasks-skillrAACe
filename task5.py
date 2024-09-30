from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# Generate RSA key pair (private and public)
def generate_rsa_keys():
    key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Save the private key and public key (you can simulate saving to cloud)
    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)

    print("Keys generated and saved to files (private.pem, public.pem)")
    return private_key, public_key

# Load the public key (simulate loading from cloud)
def load_public_key():
    with open("public.pem", "rb") as pub_file:
        return RSA.import_key(pub_file.read())

# Load the private key (simulate loading from cloud)
def load_private_key():
    with open("private.pem", "rb") as priv_file:
        return RSA.import_key(priv_file.read())

# Encrypt the credit card number using RSA
def encrypt_credit_card(card_number, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(card_number.encode('utf-8'))
    return b64encode(encrypted_data).decode('utf-8')  # Convert to base64 for easier storage/transmission

# Decrypt the credit card number using RSA
def decrypt_credit_card(encrypted_card_number, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decoded_data = b64decode(encrypted_card_number)
    decrypted_data = cipher.decrypt(decoded_data)
    return decrypted_data.decode('utf-8')

# Main flow to demonstrate encryption and decryption
def main():
    # Credit card number (example)
    credit_card_number = "4532294977918448"
    print("Credit Card Number: ", credit_card_number)

    # Generate RSA keys (private and public) - you can simulate storing these on the cloud
    generate_rsa_keys()

    # Load public key (simulate fetching from cloud)
    public_key = load_public_key()

    # Encrypt the credit card number
    encrypted_card_number = encrypt_credit_card(credit_card_number, public_key)
    print("Encrypted Credit Card Number: ", encrypted_card_number)

    # Load private key (simulate fetching from cloud)
    private_key = load_private_key()

    # Decrypt the encrypted credit card number
    decrypted_card_number = decrypt_credit_card(encrypted_card_number, private_key)
    print("Decrypted Credit Card Number: ", decrypted_card_number)


if __name__ == "__main__":
    main()
