import hashlib
import base58
import os

# Generate a random key pair (private key and public key)
def generate_key_pair():
    private_key = os.urandom(32)  # 32 bytes for the private key
    public_key = private_key  # In this simplified example, we'll just use the private key as the public key.
    return private_key, public_key

# Function to compute MD5 hash
def md5_hash(data):
    if isinstance(data, str):  # Check if data is a string and encode it to bytes
        data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()

# Function to compute SHA256 hash
def sha256_hash(data):
    if isinstance(data, str):  # Check if data is a string and encode it to bytes
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()

# Function to compute RIPEMD160 hash
def ripemd160_hash(data):
    if isinstance(data, str):  # Check if data is a string and encode it to bytes
        data = data.encode('utf-8')
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(data)
    return ripemd160.hexdigest()

# Function to encode using Base58
def base58_encode(data):
    if isinstance(data, str):  # Check if data is a string and encode it to bytes
        data = data.encode('utf-8')
    return base58.b58encode(data).decode('utf-8')

def main():
    # Generate a random key pair (private and public)
    private_key, public_key = generate_key_pair()
    print("Random Key Pair Generated (Private Key, Public Key):")
    print(f"Private Key (hex): {private_key.hex()}")
    print(f"Public Key (hex): {public_key.hex()}\n")

    # Define additional variables
    data = "sample_data"
    timestamp = "2025-01-24T15:30:00Z"
    nonce = "1234567890"

    # Print timestamp, data, and nonce
    print(f"Timestamp: {timestamp}")
    print(f"Data: {data}")
    print(f"Nonce: {nonce}\n")

    # Combine all inputs into a single string
    user_input = f"{data}{timestamp}{public_key.hex()}{nonce}"

    # Compute MD5 hash
    md5_result = md5_hash(user_input)
    print(f"\nMD5 Hash: {md5_result}")

    # Compute SHA256 hash
    sha256_result = sha256_hash(md5_result)
    print(f"SHA256 Hash: {sha256_result}")

    # Compute RIPEMD160 hash
    ripemd160_result = ripemd160_hash(sha256_result)
    print(f"RIPEMD160 Hash: {ripemd160_result}")

    # Base58 encoding
    base58_result = base58_encode(ripemd160_result)
    print(f"Base58 Encoding: {base58_result}")

if __name__ == "__main__":
    main()
