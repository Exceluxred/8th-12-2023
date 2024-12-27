from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Alice's process: Sign message with timestamp
def sign_message_with_timestamp(message, private_key):
    timestamp = datetime.utcnow().isoformat()  # Current timestamp in ISO format
    message_with_timestamp = f"{timestamp}:{message}"  # Combine timestamp with message
    signature = private_key.sign(
        message_with_timestamp.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return message_with_timestamp, signature

from datetime import datetime, timedelta

# Bob's Verifying the message and checking timestamp
def verify_message_with_timestamp(message_with_timestamp, signature, public_key):
    timestamp_str, msg = message_with_timestamp.split(":", 1)  # Split timestamp and message
    timestamp = datetime.fromisoformat(timestamp_str)  # Parse timestamp
    
    # Check to see if timestamp is within the allowed freshness window (5 minutes)
    if datetime.utcnow() - timestamp > timedelta(minutes=5):
        return "Replay Detected"  # Reject message if too old
    
    # Verify the given digital signature
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

# Alice sends the message to Bob
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

message = "Transfer $1000 to Oscar"
message_with_timestamp, signature = sign_message_with_timestamp(message, private_key)

# Bob receiving and verifies the message
print("verification:", message_with_timestamp, verify_message_with_timestamp(message_with_timestamp, signature, public_key))  # Expected: "Verified and Fresh"

# Simulating replay: Oscar sends the message 100 times (within a short time)
for i in range(1, 6):  # Limited to 5 for demonstration
    print(f"Replay simulation {i}:", message_with_timestamp, verify_message_with_timestamp(message_with_timestamp, signature, public_key))  # Expected: "Verified and Fresh"

import hmac
import hashlib
import os

# Creating MAC with a nonce
def create_mac_with_nonce(message, key):
    nonce = os.urandom(16).hex()  # Generate a random nonce
    message_with_nonce = f"{nonce}:{message}"  # Combine nonce with message
    mac = hmac.new(key, message_with_nonce.encode(), hashlib.sha256).hexdigest()
    return message_with_nonce, mac, nonce
# Bob's process: Verify the MAC and check nonce
used_nonces = set()  # Set to store used nonces

def verify_mac_with_nonce(message_with_nonce, mac, key):
    nonce, msg = message_with_nonce.split(":", 1)  # Split nonce and message
    
    # Check if nonce has already been used (replay detected)
    if nonce in used_nonces:
        return "Replay Detected"  # Reject message if nonce has been used before
    
    # Add nonce to used set
    used_nonces.add(nonce)
    
    # Verify the MAC
    expected_mac = hmac.new(key, message_with_nonce.encode(), hashlib.sha256).hexdigest()
    if hmac.compare_digest(mac, expected_mac):
        return " Verified and Fresh"
    else:
        return " Verification Failed"
#  Alice sends a message to Bob
shared_secret = b'supersecretkey'  # Shared key known to Alice and Bob
message = "Transfer $1000 to Oscar"
message_with_nonce, mac, nonce = create_mac_with_nonce(message, shared_secret)

# Bob receives and verifies the message
print("First message verification:",nonce, verify_mac_with_nonce(message_with_nonce, mac, shared_secret))  # Expected: "MAC Verified and Fresh"
# Simulating replay by Oscar with the same nonce
print("Replay Simulation:",nonce, verify_mac_with_nonce(message_with_nonce, mac, shared_secret))  # Expected: "Replay Detected not verified / "
