from datetime import datetime, timedelta
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generating RSA key for Digital Signature
def generate_rsa_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Alice Sign's message with timestamps against replay 
def sign_message_with_timestamp(message, private_key):
    timestamp = datetime.utcnow().isoformat()  # Generate current timestamp
    message_with_timestamp = f"{timestamp}:{message}"
    signature = private_key.sign(
        message_with_timestamp.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return message_with_timestamp, signature

# Bob Verify DS to detect replay using timestamp
def verify_message_with_timestamp(message_with_timestamp, signature, public_key):
    timestamp_str, msg = message_with_timestamp.split(":", 1)
    timestamp = datetime.fromisoformat(timestamp_str)
    current_time = datetime.utcnow()

    # Displaying message verification
    print("\nVerifying Message:", msg)

    # Checking freshness in 5-minute window
    if current_time - timestamp > timedelta(minutes=5):
        return "Replay Detected"

    #DS
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


# Generatin Alice and Bob's key
private_key, public_key = generate_rsa_keys()

#original message from Alice
message = "Transfer $1000 to Oscar"
# Alice signs the message with a timestamp
message_with_timestamp, signature = sign_message_with_timestamp(message, private_key)
print("Original Message:", message_with_timestamp)
print(verify_message_with_timestamp(message_with_timestamp, signature, public_key))
#simulating replay
for i in range(1, 100):
    result = verify_message_with_timestamp(message_with_timestamp, signature, public_key)
    print(f"Replay Attempt {i}: {result}")  