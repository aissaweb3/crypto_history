import requests

BASE_URL = "https://aes.cryptohack.org/ecb_oracle/encrypt/"

def ecb_encrypt(plaintext):
    # Ensure plaintext is properly encoded in hexadecimal
    plaintext_hex = plaintext.encode("utf-8").hex()
    response = requests.get(f"{BASE_URL}{plaintext_hex}/")
    return response.json()["ciphertext"]

last_result = ""

def recover_byte(padding):
    global last_result
    # Encrypt a block of 16 'A' characters to get the reference ciphertext for alignment
    reference_ciphertext = ecb_encrypt(padding)[:32]  # encrypt(padding + flag[0])

    bruteforced = 0
    while True:
        # Construct plaintext for brute-forcing
        test_plaintext = padding + last_result + chr(bruteforced)  # 15 'A's + brute-forced character
        result = ecb_encrypt(test_plaintext)

        # Compare the first block of the ciphertext with the reference
        if result[:32] == reference_ciphertext:
            print(f"Found matching byte: {chr(bruteforced)}")
            return chr(bruteforced)
            break

        bruteforced += 1
        if bruteforced > 255:  # Avoid infinite loops
            print("Brute force failed. Check logic.")
            return


def recover_flag(padding):
    global last_result
    last_result += recover_byte(padding)
    print(last_result)
    recover_flag(padding[:-1]) # Removes the last character

recover_flag("AAAAAAAAAAAAAAA")

