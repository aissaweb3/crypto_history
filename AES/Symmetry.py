from Crypto.Cipher import AES


KEY = ?
FLAG = ?


@chal.route('/symmetry/encrypt/<plaintext>/<iv>/')
def encrypt(plaintext, iv):
    plaintext = bytes.fromhex(plaintext)
    iv = bytes.fromhex(iv)
    if len(iv) != 16:
        return {"error": "IV length must be 16"}

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(plaintext)
    ciphertext = encrypted.hex()

    return {"ciphertext": ciphertext}


@chal.route('/symmetry/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_OFB, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()

    return {"ciphertext": ciphertext}





# IV
# e32ca505547966604925cd54a28f0baa
# cipher text
# 3869e49c771162d4bd17fdb5d0a75e93      {first state}
# 870b1020840cbff0ccd6ddf41e80bbd9      {second state}
# bb                                    {third state}


# IV encrypted ---> 0865d0644f3d93fcf52b2d8aa2352938

# crypto{0fb_15_5y = CT1 ^ encrypt(IV)

# this is the first state of the flag
# CT1 is the first the state of the cipher text (first 16 bytes)


# you can calculate encrypt(IV) like this :
# encrypt(IV) = encrypt("00000000000000000000000000000000",iv)
# the encrypted IV is XORed with a string of 0s bytes so its doesnt change, and that what we want


# mm37r1c4l_!!!11! = CT2 ^ encrypt(encrypt(IV))
# CT2 is the second the state of the cipher text
# just like this we get the second state of the flag, now we get the third state in the same manner

# c6855dade931b98cf358a110f4f6dc68 = encrypt(encrypt(encrypt(IV)))

# third_state = CT3 ^ encrypt(encrypt(encrypt(IV)))
# CT3 is the third the state of the cipher text
# but because the third state of the flag is just "bb" then we know the flag has one byte left 
# and because we know the furmula of the flag, we know the last byte is "}"


# in the end we get the flag:

# crypto{0fb_15_5ymm37r1c4l_!!!11!}

# OFB is symmetrical !!!ii!
