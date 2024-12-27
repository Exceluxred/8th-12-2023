import hmac
import hashlib
import secrets

# Generate MAC with a nonce to prevent replay
def create_mac_with_nonce(message, nonce, key):
    message_with_nonce = f"{nonce}:{message}"  # Include nonce in the message
    mac = hmac.new(key, message_with_nonce.encode(), hashlib.sha256).hexdigest()
    return message_with_nonce, mac

# Bob Verifying MAC by checking nonce uniqueness
def verify_mac_with_nonce(message_with_nonce, received_mac, key, known_nonces):
    nonce, msg = message_with_nonce.split(":", 1)

    # Checking if nonce is already used
    if nonce in known_nonces:
        return "Replay Detected"

    known_nonces.add(nonce)  # Marking known nonce as already used

    # Verify MAC
    expected_mac = hmac.new(key, message_with_nonce.encode(), hashlib.sha256).hexdigest()
    return "Verified and Fresh" if hmac.compare_digest(expected_mac, received_mac) else "MAC Verification Failed"

# Shared keys
hmac_key = b'secret_shared_key'

# message
message = "Transfer $1000 to Oscar"

# Nonce storage against replay detection
known_nonces = set()

# generating nonce for the message
nonce = secrets.token_hex(16)
print("Generated Nonce:", nonce)

# creating a MAC with the nonce
message_with_nonce, mac = create_mac_with_nonce(message, nonce, hmac_key)
print("MAC:", mac)

# verifing message to detects replays
print(f"\n message :\n {message_with_nonce} ",verify_mac_with_nonce(message_with_nonce, mac, hmac_key, known_nonces))

#simulating replay
for i in range(1, 100):
    result = verify_mac_with_nonce(message_with_nonce, mac, hmac_key, known_nonces)
    print(f"Replay Attempt {i}:\n {message_with_nonce} {result} ") 
