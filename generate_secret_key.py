import secrets

def generate_secret_key():
    """Generate a secure secret key for Flask."""
    secret_key = secrets.token_hex(16)  # Generate a random hexadecimal string of length 16
    return secret_key

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Generated Secret Key:", secret_key)
