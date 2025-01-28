

# pt = "crypto{12345678}crypto{12345678}"
# pt = pt1 + pt2 = 63727970746f7b31323334353637387d + 63727970746f7b31323334353637387d
# pt = 63727970746f7b31323334353637387d63727970746f7b31323334353637387d

# Encrypt(pt) = c9477d5c4e0998ceebc8ab99686df324747a4f2a4b4621cdd2319850ceb5ff09
# Encrypt(pt) = ct1 + ct2

# ct1 = Enc(pt1 ^ KEY) = c9477d5c4e0998ceebc8ab99686df324
# ct2 = Enc(pt2 ^ ct1) = 747a4f2a4b4621cdd2319850ceb5ff09

# Decrypt(ct2) = AES_decrypt(ct2) ^ KEY
# Decrypt(ct2) = 50973529a7282d137f5eacb571bd1535
# Decrypt(ct2) = AES_decrypt(Enc(pt2 ^ ct1)) ^ KEY
# Decrypt(ct2) = pt2 ^ ct1 ^ KEY
# KEY = Decrypt(ct2) ^ pt2 ^ ct1
# KEY = 50973529a7282d137f5eacb571bd1535 ^ 63727970746f7b31323334353637387d ^ c9477d5c4e0998ceebc8ab99686df324
# KEY = 33e54c59d34756224d6d9880478a2d48 ^ c9477d5c4e0998ceebc8ab99686df324
# KEY = faa231059d4eceeca6a533192fe7de6c


# submit the key and we get the flag:
# crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}



