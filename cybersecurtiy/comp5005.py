# from cryptography.hazmat.primitives import hashes, serialization
# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives.hmac import HMAC
# from datetime import datetime, timedelta
# import hashlib
# import time

# # Alice generates a DS or MAC with timestamp
# def create_message_with_signature(message, private_key):
#     timestamp = datetime.utcnow().isoformat()
#     combined_message = f"{timestamp}:{message}"
#     message_bytes = combined_message.encode()
    
#     # Signing with DS
#     signature = private_key.sign(
#         message_bytes,
#         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
#         hashes.SHA256()
#     )
#     return combined_message, signature

# # Bob verifies DS and timestamp
# def verify_message_with_signature(combined_message, signature, public_key):
#     timestamp_str, message = combined_message.split(":", 1)
#     timestamp = datetime.fromisoformat(timestamp_str)
#     current_time = datetime.utcnow()

#     # Check if the message timestamp is within the allowed time window (e.g., 5 minutes)
#     if current_time - timestamp > timedelta(minutes=5):
#         return "Replay Detected"

#     # Verify the signature
#     public_key.verify(
#         signature,
#         combined_message.encode(),
#         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
#         hashes.SHA256()
#     )
#     return "Verified and Fresh"

# # Key generation for DS (RSA) example
# private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
# public_key = private_key.public_key()

# # Alice's Process
# message = "Transfer $1000 to Oscar"
# combined_message, signature = create_message_with_signature(message, private_key)

# # Bob's Process
# verification_result = verify_message_with_signature(combined_message, signature, public_key)
# print(verification_result)  # Expected: "Verified and Fresh" or "Replay Detected"


# from cryptography.hazmat.primitives import hmac, hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.backends import default_backend
# import os

# # Generate a key for HMAC (simulating a shared secret key)
# def generate_hmac_key():
#     return os.urandom(32)  # 256-bit key

# # Alice's Process with MAC
# def create_message_with_mac(message, key):
#     timestamp = datetime.utcnow().isoformat()
#     combined_message = f"{timestamp}:{message}"
#     h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
#     h.update(combined_message.encode())
#     mac = h.finalize()
#     return combined_message, mac

# # Bob's Process with MAC Verification
# def verify_message_with_mac(combined_message, mac, key):
#     timestamp_str, message = combined_message.split(":", 1)
#     timestamp = datetime.fromisoformat(timestamp_str)
#     current_time = datetime.utcnow()

#     # Check time window
#     if current_time - timestamp > timedelta(minutes=5):
#         return "Replay Detected"

#     # Verify MAC
#     h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
#     h.update(combined_message.encode())
#     try:
#         h.verify(mac)
#         return "Verified and Fresh"
#     except:
#         return "Invalid MAC"
# import hmac
# import secrets

# # Shared secret key for HMAC
# shared_key = b'secret-key'

# # Bob generates a nonce
# nonce = secrets.token_hex(16)  # Generate a secure random nonce

# # Alice creates a MAC with the nonce
# def create_message_with_mac(message, nonce, key):
#     message_with_nonce = f"{nonce}:{message}".encode()
#     mac = hmac.new(key, message_with_nonce, hashlib.sha256).hexdigest()
#     return message_with_nonce, mac

# # Bob verifies the MAC and nonce
# def verify_message_with_mac(message_with_nonce, received_mac, key, known_nonces):
#     nonce, message = message_with_nonce.decode().split(":", 1)

#     # Check for replay by verifying if nonce has been used before
#     if nonce in known_nonces:
#         return "Replay Detected"

#     # Verify MAC
#     expected_mac = hmac.new(key, message_with_nonce, hashlib.sha256).hexdigest()
#     if hmac.compare_digest(expected_mac, received_mac):
#         known_nonces.add(nonce)  # Mark nonce as used
#         return "Verified and Fresh"
#     return "MAC Verification Failed"

# # Bob's known nonces set
# known_nonces = set()

# # Alice's Process
# message = "Transfer $1000 to Oscar"
# message_with_nonce, mac = create_message_with_mac(message, nonce, shared_key)

# # Bob's Process
# verification_result = verify_message_with_mac(message_with_nonce, mac, shared_key, known_nonces)
# print(verification_result)  # Expected: "Verified and Fresh" or "Replay Detected"
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime, timedelta
import secrets

# Generate a message with a timestamp or nonce
def generate_message(is_replay=False, use_nonce=False):
    message = "Transfer $1000 to Oscar"

    if use_nonce:
        # Generate a unique nonce unless simulating a replay attack
        nonce = "replay_nonce" if is_replay else secrets.token_hex(16)
        combined_message = f"{nonce}:{message}"
    else:
        # Use current timestamp, or an old timestamp if simulating replay
        timestamp = datetime.utcnow() - timedelta(minutes=10) if is_replay else datetime.utcnow()
        combined_message = f"{timestamp.isoformat()}:{message}"

    return combined_message

# Testing message generation
print("Fresh message with timestamp:", generate_message(is_replay=False))
print("Replay message with timestamp:", generate_message(is_replay=True))
print("Fresh message with nonce:", generate_message(is_replay=False, use_nonce=True))
print("Replay message with nonce:", generate_message(is_replay=True, use_nonce=True))
