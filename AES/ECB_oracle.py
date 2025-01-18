





# cipher = "




# 6b71db5ff6873cc0c0d1248151c12411      "16 bytes"
# 6b71db5ff6873cc0c0d1248151c12411      "16 bytes"
# 6b71db5ff6873cc0c0d1248151c12411      "16 bytes"
# 6b71db5ff6873cc0c0d1248151c12411      "16 bytes"


# 09219778bd0d7fceca1c2f9ac4588074f4975bf364df0dd7709231952b39ce923376f0233f1d68ca83b3569e5c5c2d10"       # "48 bytes"



# flag = 58bytes

# ffffffffffff # 6 bytes



# state2 = 666d43ab928dd36432e37d87c529ff17;



# # 64    96



# def encrypt(plaintext):

#     padded = pad(plaintext + FLAG, 16)


#     cipher = AES.new(KEY, AES.MODE_ECB)
#     try:
#         encrypted = cipher.encrypt(padded)
#     except ValueError as e:
#         return {"error": str(e)}

#     return {"ciphertext": encrypted.hex()}



# plaintext
#    |
#    |
#    |
# ------crypto{***        ***************}
#                         bab6f279542c13dff434916116dc251d
#         |                    |
#         |                    |
#         |                    |
#        KEY                  KEY




# plaintext
#    |
#    |
#    |
# -crypto{********        **********}=====
#                         666d43ab928dd36432e37d87c529ff17
#         |                    |
#         |                    |
#         |                    |
#        KEY                  KEY





# plaintext
#    |
#    |
#    |
# 00c        rypto{**********        ********}=====
#                         666d43ab928dd36432e37d87c529ff17
#         |                    |
#         |                    |
#         |                    |
#        KEY                  KEY








