# # # from cryptography.hazmat.primitives import hashes, serialization
# # # from cryptography.hazmat.primitives.asymmetric import rsa, padding
# # # from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# # # from cryptography.hazmat.primitives.hmac import HMAC
# # # from datetime import datetime, timedelta
# # # import hashlib
# # # import time

# # # # Alice generates a DS or MAC with timestamp
# # # def create_message_with_signature(message, private_key):
# # #     timestamp = datetime.utcnow().isoformat()
# # #     combined_message = f"{timestamp}:{message}"
# # #     message_bytes = combined_message.encode()
    
# # #     # Signing with DS
# # #     signature = private_key.sign(
# # #         message_bytes,
# # #         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
# # #         hashes.SHA256()
# # #     )
# # #     return combined_message, signature

# # # # Bob verifies DS and timestamp
# # # def verify_message_with_signature(combined_message, signature, public_key):
# # #     timestamp_str, message = combined_message.split(":", 1)
# # #     timestamp = datetime.fromisoformat(timestamp_str)
# # #     current_time = datetime.utcnow()

# # #     # Check if the message timestamp is within the allowed time window (e.g., 5 minutes)
# # #     if current_time - timestamp > timedelta(minutes=5):
# # #         return "Replay Detected"

# # #     # Verify the signature
# # #     public_key.verify(
# # #         signature,
# # #         combined_message.encode(),
# # #         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
# # #         hashes.SHA256()
# # #     )
# # #     return "Verified and Fresh"

# # # # Key generation for DS (RSA) example
# # # private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
# # # public_key = private_key.public_key()

# # # # Alice's Process
# # # message = "Transfer $1000 to Oscar"
# # # combined_message, signature = create_message_with_signature(message, private_key)

# # # # Bob's Process
# # # verification_result = verify_message_with_signature(combined_message, signature, public_key)
# # # print(verification_result)  # Expected: "Verified and Fresh" or "Replay Detected"


# # # from cryptography.hazmat.primitives import hmac, hashes
# # # from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# # # from cryptography.hazmat.backends import default_backend
# # # import os

# # # # Generate a key for HMAC (simulating a shared secret key)
# # # def generate_hmac_key():
# # #     return os.urandom(32)  # 256-bit key

# # # # Alice's Process with MAC
# # # def create_message_with_mac(message, key):
# # #     timestamp = datetime.utcnow().isoformat()
# # #     combined_message = f"{timestamp}:{message}"
# # #     h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
# # #     h.update(combined_message.encode())
# # #     mac = h.finalize()
# # #     return combined_message, mac

# # # # Bob's Process with MAC Verification
# # # def verify_message_with_mac(combined_message, mac, key):
# # #     timestamp_str, message = combined_message.split(":", 1)
# # #     timestamp = datetime.fromisoformat(timestamp_str)
# # #     current_time = datetime.utcnow()

# # #     # Check time window
# # #     if current_time - timestamp > timedelta(minutes=5):
# # #         return "Replay Detected"

# # #     # Verify MAC
# # #     h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
# # #     h.update(combined_message.encode())
# # #     try:
# # #         h.verify(mac)
# # #         return "Verified and Fresh"
# # #     except:
# # #         return "Invalid MAC"
# # # import hmac
# # # import secrets

# # # # Shared secret key for HMAC
# # # shared_key = b'secret-key'

# # # # Bob generates a nonce
# # # nonce = secrets.token_hex(16)  # Generate a secure random nonce

# # # # Alice creates a MAC with the nonce
# # # def create_message_with_mac(message, nonce, key):
# # #     message_with_nonce = f"{nonce}:{message}".encode()
# # #     mac = hmac.new(key, message_with_nonce, hashlib.sha256).hexdigest()
# # #     return message_with_nonce, mac

# # # # Bob verifies the MAC and nonce
# # # def verify_message_with_mac(message_with_nonce, received_mac, key, known_nonces):
# # #     nonce, message = message_with_nonce.decode().split(":", 1)

# # #     # Check for replay by verifying if nonce has been used before
# # #     if nonce in known_nonces:
# # #         return "Replay Detected"

# # #     # Verify MAC
# # #     expected_mac = hmac.new(key, message_with_nonce, hashlib.sha256).hexdigest()
# # #     if hmac.compare_digest(expected_mac, received_mac):
# # #         known_nonces.add(nonce)  # Mark nonce as used
# # #         return "Verified and Fresh"
# # #     return "MAC Verification Failed"

# # # # Bob's known nonces set
# # # known_nonces = set()

# # # # Alice's Process
# # # message = "Transfer $1000 to Oscar"
# # # message_with_nonce, mac = create_message_with_mac(message, nonce, shared_key)

# # # # Bob's Process
# # # verification_result = verify_message_with_mac(message_with_nonce, mac, shared_key, known_nonces)
# # # print(verification_result)  # Expected: "Verified and Fresh" or "Replay Detected"
# # # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # from cryptography.hazmat.primitives import hashes, serialization
# # from cryptography.hazmat.primitives.asymmetric import rsa, padding
# # from cryptography.hazmat.primitives.hmac import HMAC
# # from datetime import datetime, timedelta
# # import hashlib
# # import os
# # import hmac
# # import secrets

# # # === Digital Signature (DS) with Timestamp Implementation ===

# # # Step 1: Generate RSA key pair for Digital Signature
# # def generate_rsa_keys():
# #     private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
# #     public_key = private_key.public_key()
# #     return private_key, public_key

# # # Step 2: Alice creates a message with a timestamp and signs it
# # def create_signed_message(message, private_key):
# #     timestamp = datetime.utcnow().isoformat()
# #     combined_message = f"{timestamp}:{message}"
# #     message_bytes = combined_message.encode()

# #     # Signing with DS
# #     signature = private_key.sign(
# #         message_bytes,
# #         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
# #         hashes.SHA256()
# #     )
# #     return combined_message, signature

# # # Step 3: Bob verifies DS and checks the timestamp for replay detection
# # def verify_signed_message(combined_message, signature, public_key):
# #     timestamp_str, message = combined_message.split(":", 1)
# #     timestamp = datetime.fromisoformat(timestamp_str)
# #     current_time = datetime.utcnow()

# #     # Check if the message timestamp is within the allowed time window (e.g., 5 minutes)
# #     if current_time - timestamp > timedelta(minutes=5):
# #         return "Replay Detected"

# #     # Verify the signature
# #     try:
# #         public_key.verify(
# #             signature,
# #             combined_message.encode(),
# #             padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
# #             hashes.SHA256()
# #         )
# #         return "Verified and Fresh"
# #     except Exception as e:
# #         return "Signature Verification Failed"

# # # DS Implementation Demo
# # private_key, public_key = generate_rsa_keys()
# # message = "Transfer $1000 to Oscar"

# # # Alice's Process
# # signed_message, signature = create_signed_message(message, private_key)

# # # Bob's Process
# # verification_result = verify_signed_message(signed_message, signature, public_key)
# # print(f"Digital Signature Verification Result: {verification_result}")  # Expected: "Verified and Fresh" or "Replay Detected"


# # # === Message Authentication Code (MAC) with Nonce Implementation ===

# # # Step 1: Generate a shared HMAC key (simulating a shared secret key)
# # def generate_hmac_key():
# #     return os.urandom(32)  # 256-bit key

# # # Step 2: Alice's Process with MAC and Nonce
# # def create_message_with_mac_and_nonce(message, key):
# #     nonce = secrets.token_hex(16)  # Generate a secure random nonce
# #     combined_message = f"{nonce}:{message}".encode()
    
# #     # Generate MAC
# #     mac = hmac.new(key, combined_message, hashlib.sha256).hexdigest()
# #     return combined_message, mac, nonce

# # # Step 3: Bob verifies the MAC, checks nonce to prevent replay attacks
# # def verify_message_with_mac_and_nonce(combined_message, received_mac, key, known_nonces):
# #     nonce, message = combined_message.decode().split(":", 1)

# #     # Check for replay by verifying if nonce has been used before
# #     if nonce in known_nonces:
# #         return "Replay Detected"

# #     # Verify MAC
# #     expected_mac = hmac.new(key, combined_message, hashlib.sha256).hexdigest()
# #     if hmac.compare_digest(expected_mac, received_mac):
# #         known_nonces.add(nonce)  # Mark nonce as used
# #         return "Verified and Fresh"
# #     else:
# #         return "MAC Verification Failed"

# # # MAC with Nonce Implementation Demo
# # hmac_key = generate_hmac_key()
# # known_nonces = set()  # Set to store known nonces to detect replays

# # # Alice's Process
# # message_with_nonce, mac, nonce = create_message_with_mac_and_nonce("Transfer $1000 to Oscar", hmac_key)

# # # Bob's Process
# # verification_result = verify_message_with_mac_and_nonce(message_with_nonce, mac, hmac_key, known_nonces)
# # print(f"HMAC with Nonce Verification Result: {verification_result}")  # Expected: "Verified and Fresh" or "Replay Detected"
# # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from cryptography.hazmat.primitives import hashes, serialization
# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from datetime import datetime, timedelta
# import hashlib
# import os
# import hmac
# import secrets

# # === Setup Functions for Testing ===
# # Generate RSA keys for DS and HMAC shared key for MAC
# def generate_rsa_keys():
#     private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
#     public_key = private_key.public_key()
#     return private_key, public_key

# def generate_hmac_key():
#     return os.urandom(32)  # 256-bit key

# # === Digital Signature with Timestamp Solution ===
# def create_signed_message(message, private_key, add_delay=False):
#     # Optional delay to simulate replay attack by modifying timestamp
#     timestamp = datetime.utcnow() - timedelta(minutes=10) if add_delay else datetime.utcnow()
#     combined_message = f"{timestamp.isoformat()}:{message}"
#     message_bytes = combined_message.encode()

#     # Signing with DS
#     signature = private_key.sign(
#         message_bytes,
#         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
#         hashes.SHA256()
#     )
#     return combined_message, signature

# def verify_signed_message(combined_message, signature, public_key):
#     timestamp_str, message = combined_message.split(":", 1)
#     timestamp = datetime.fromisoformat(timestamp_str)
#     current_time = datetime.utcnow()

#     # Check if the message timestamp is within the allowed time window (e.g., 5 minutes)
#     if current_time - timestamp > timedelta(minutes=5):
#         return "Replay Detected"

#     # Verify the signature
#     try:
#         public_key.verify(
#             signature,
#             combined_message.encode(),
#             padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
#             hashes.SHA256()
#         )
#         return "Verified and Fresh"
#     except Exception:
#         return "Signature Verification Failed"

# # === HMAC with Nonce Solution ===
# def create_message_with_mac_and_nonce(message, key, reuse_nonce=False, known_nonce=None):
#     nonce = known_nonce if reuse_nonce else secrets.token_hex(16)  # New nonce unless simulating replay
#     combined_message = f"{nonce}:{message}".encode()

#     # Generate MAC
#     mac = hmac.new(key, combined_message, hashlib.sha256).hexdigest()
#     return combined_message, mac, nonce

# def verify_message_with_mac_and_nonce(combined_message, received_mac, key, known_nonces):
#     nonce, message = combined_message.decode().split(":", 1)

#     # Check for replay by verifying if nonce has been used before
#     if nonce in known_nonces:
#         return "Replay Detected"

#     # Verify MAC
#     expected_mac = hmac.new(key, combined_message, hashlib.sha256).hexdigest()
#     if hmac.compare_digest(expected_mac, received_mac):
#         known_nonces.add(nonce)  # Mark nonce as used
#         return "Verified and Fresh"
#     else:
#         return "MAC Verification Failed"

# # === Test Modes ===
# def run_test(test_mode="ds", simulate_replay=False):
#     if test_mode == "ds":
#         # Digital Signature with Timestamp Test
#         print("Running Digital Signature with Timestamp Test...")
#         private_key, public_key = generate_rsa_keys()
#         # Add delay if simulating replay
#         signed_message, signature = create_signed_message("Transfer $1000 to Oscar", private_key, add_delay=simulate_replay)
#         result = verify_signed_message(signed_message, signature, public_key)
#         print(f"Digital Signature Verification Result: {result}")

#     elif test_mode == "mac":
#         # HMAC with Nonce Test
#         print("Running HMAC with Nonce Test...")
#         hmac_key = generate_hmac_key()
#         known_nonces = set()
#         # Reuse nonce if simulating replay
#         combined_message, mac, nonce = create_message_with_mac_and_nonce("Transfer $1000 to Oscar", hmac_key, reuse_nonce=simulate_replay, known_nonce="replay_nonce" if simulate_replay else None)
#         result = verify_message_with_mac_and_nonce(combined_message, mac, hmac_key, known_nonces)
#         print(f"HMAC with Nonce Verification Result: {result}")

# # === Run Tests ===
# # To test Digital Signature with Replay Detection, set test_mode="ds"
# # To test HMAC with Nonce Replay Detection, set test_mode="mac"
# # Set simulate_replay=True to simulate a replay attack

# run_test(test_mode="ds", simulate_replay=False)  # Expected: "Verified and Fresh"
# run_test(test_mode="ds", simulate_replay=True)   # Expected: "Replay Detected"

# run_test(test_mode="mac", simulate_replay=False) # Expected: "Verified and Fresh"
# run_test(test_mode="mac", simulate_replay=True)  # Expected: "Replay Detected"
# ================================================================================================================================================================================================================================================================================================

# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from cryptography.hazmat.primitives import hashes

# # RSA keys Generation
# def generate_rsa_keys():
#     private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
#     public_key = private_key.public_key()
#     return private_key, public_key
# # Alice Sign the message 
# def sign_message(message, private_key):
#     signature = private_key.sign(
#         message.encode(),
#         padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
#         hashes.SHA256()
#     )
#     return signature
# # signature Verification for Bob
# def verify_signature(message, signature, public_key):
#     try:
#         public_key.verify(
#             signature,
#             message.encode(),
#             padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
#             hashes.SHA256()
#         )
#         return "Signature Verified"
#     except Exception:
#         return "Signature Verification Failed"

# # message sent from Alice to Bob
# private_key, public_key = generate_rsa_keys()
# message = "Transfer $1000 to Oscar"
# signature = sign_message(message, private_key)

# # Bob receives and verifies the message
# print("First verification:", verify_signature(message, signature, public_key)) 

# # Simulating replay attack form Oscar sending the message 100 times
# for i in range(1, 6):  # Limited to 5 for demonstration
#     print(f"Replay verification {i}:", verify_signature(message, signature, public_key)) 


# ======================================================================================================================================================================================================================================================================================================================================================

import hmac
import hashlib

# Generate a shared HMAC key
def generate_hmac_key():
    return b'secret_shared_key'

# Alice's process: Create MAC for the message
def create_mac(message, key):
    mac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return mac

# Bob's process: Verify the MAC
def verify_mac(message, received_mac, key):
    expected_mac = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return "MAC Verified" if hmac.compare_digest(expected_mac, received_mac) else "MAC Verification Failed"

# Example Scenario: Alice sends a message to Bob
hmac_key = generate_hmac_key()
message = "Transfer $1000 to Oscar"
mac = create_mac(message, hmac_key)

# Bob receives and verifies the message
print("First verification:", verify_mac(message, mac, hmac_key))  # Expected: "MAC Verified"

# Simulating replay: Oscar sends the message 100 times
for i in range(1, 6):  # Limited to 5 for demonstration
    print(f"Replay verification {i}:", verify_mac(message, mac, hmac_key))  # Expected: "MAC Verified"
