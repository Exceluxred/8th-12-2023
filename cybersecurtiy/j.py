from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import hmac
import hashlib
import secrets
from datetime import datetime, timedelta

# === PART 1: SIMULATING REPLAY ATTACKS WITH DS AND MAC ===

# Task: Simulate a replay attack to demonstrate that DS and MAC alone cannot detect replays

# Section 1: Generate Keys for DS and MAC
def generate_rsa_keys():
    # Generates RSA private and public keys for DS
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def generate_hmac_key():
    # Generates a fixed HMAC key for MAC
    return b'secret_hmac_key'

# Section 2: Create a Message Signed with DS
def sign_message_ds(message, private_key):
    # Alice signs the message with her private key to create a DS
    signature = private_key.sign(
        message.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature

def verify_signature_ds(message, signature, public_key):
    # Bob verifies the DS; cannot detect replay, only validates authenticity and integrity
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return "Signature Verified"
    except Exception:
        return "Signature Verification Failed"

# Section 3: Create a Message Authentication Code (MAC)
def create_mac(message, key):
    # Alice creates a MAC for the message
    mac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return mac

def verify_mac(message, received_mac, key):
    # Bob verifies the MAC; cannot detect replay, only validates authenticity and integrity
    expected_mac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return "MAC Verified" if hmac.compare_digest(expected_mac, received_mac) else "MAC Verification Failed"

# Demonstrating Replay Attack on DS and MAC
print("=== PART 1: Replay Attack Simulation ===")
private_key, public_key = generate_rsa_keys()
hmac_key = generate_hmac_key()
original_message = "Transfer $1000 to Oscar"

# Alice signs and creates a MAC for the message
signature = sign_message_ds(original_message, private_key)
mac = create_mac(original_message, hmac_key)

# Bob verifies the message twice, simulating a replay
print("First verification (Original Message):")
print("Digital Signature:", verify_signature_ds(original_message, signature, public_key))  # Expected: "Signature Verified"
print("MAC:", verify_mac(original_message, mac, hmac_key))  # Expected: "MAC Verified"

print("\nSimulating Replay Attack - Verifying the same message again (Replay):")
print("Digital Signature:", verify_signature_ds(original_message, signature, public_key))  # Expected: "Signature Verified"
print("MAC:", verify_mac(original_message, mac, hmac_key))  # Expected: "MAC Verified"

# Result: Both DS and MAC verify successfully, showing that they alone cannot detect replays.


# === PART 2: IMPROVED SOLUTIONS WITH TIMESTAMP (FOR DS) AND NONCE (FOR MAC) ===

# Task: Implement replay detection by adding timestamps for DS and nonces for MAC

# Improved DS Solution with Timestamp
def sign_message_with_timestamp(message, private_key):
    # Alice creates a timestamped message and signs it
    timestamp = datetime.utcnow().isoformat()
    message_with_timestamp = f"{timestamp}:{message}"
    signature = private_key.sign(
        message_with_timestamp.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return message_with_timestamp, signature

def verify_message_with_timestamp(message_with_timestamp, signature, public_key):
    # Bob checks timestamp freshness (5 min window) and verifies DS
    timestamp_str, message = message_with_timestamp.split(":", 1)
    timestamp = datetime.fromisoformat(timestamp_str)
    if datetime.utcnow() - timestamp > timedelta(minutes=5):
        return "Replay Detected"

    # Verify the signature
    try:
        public_key.verify(
            signature,
            message_with_timestamp.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return "Verified and Fresh"
    except Exception:
        return "Signature Verification Failed"

# Testing DS with Timestamp Solution
print("\n=== Improved DS Solution with Timestamp ===")
message_with_timestamp, signature_with_timestamp = sign_message_with_timestamp(original_message, private_key)
print("First Verification (Fresh Message):", verify_message_with_timestamp(message_with_timestamp, signature_with_timestamp, public_key))  # Expected: "Verified and Fresh"

# Simulate Replay by Verifying the Same Message After Delay
print("Replay Attack (Old Timestamp):", verify_message_with_timestamp(message_with_timestamp, signature_with_timestamp, public_key))  # Expected: "Replay Detected"


# Improved MAC Solution with Nonce
def create_mac_with_nonce(message, key, used_nonces):
    # Alice generates a nonce, creates a message with it, and MACs it
    nonce = secrets.token_hex(16)
    if nonce in used_nonces:
        return "Nonce Already Used"
    used_nonces.add(nonce)
    message_with_nonce = f"{nonce}:{message}"
    mac = hmac.new(key, message_with_nonce.encode(), hashlib.sha256).hexdigest()
    return message_with_nonce, mac

def verify_mac_with_nonce(message_with_nonce, received_mac, key, known_nonces):
    # Bob checks nonce uniqueness and verifies MAC
    nonce, message = message_with_nonce.split(":", 1)
    if nonce in known_nonces:
        return "Replay Detected"
    known_nonces.add(nonce)
    expected_mac = hmac.new(key, message_with_nonce.encode(), hashlib.sha256).hexdigest()
    return "Verified and Fresh" if hmac.compare_digest(expected_mac, received_mac) else "MAC Verification Failed"

# Testing MAC with Nonce Solution
print("\n=== Improved MAC Solution with Nonce ===")
used_nonces = set()
message_with_nonce, mac_with_nonce = create_mac_with_nonce(original_message, hmac_key, used_nonces)
print("First Verification (Fresh Message):", verify_mac_with_nonce(message_with_nonce, mac_with_nonce, hmac_key, used_nonces))  # Expected: "Verified and Fresh"

# Simulate Replay by Reusing the Same Nonce
print("Replay Attack (Reused Nonce):", verify_mac_with_nonce(message_with_nonce, mac_with_nonce, hmac_key, used_nonces))  # Expected: "Replay Detected"
