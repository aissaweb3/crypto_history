




#             IV                                          encrypted padded(16) cookies
#              |                                                  |
#              |                                                  |
#              |                                                  |
# 2881a0375f6ca5514e3a3dd576f54b32        bc7ea69a6c39b0ebf3b9fe10df120f8e   2fdb7024c171bde08a8968d1a5a0a03a




from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta

expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
cookie = f"admin=False;expiry={expires_at}".encode()

state1 = "admin=False;expi"

# AES(state1 ^ iv) = "bc7ea69a6c39b0ebf3b9fe10df120f8e"


"False" ^ 0x121319165e = "True;"



padded = pad("test", 16)

print(padded)

print(cookie)



# simply we get the a the cookie and the random iv and put them back in the first function,
# but instead of the real iv we got "2881a0375f6ca5514e3a3dd576f54b32"
# we exploit it with the string 0x121319165e that converts us the word "Flase" to the word "True;"

# like this : 2881a0375f6c a5514e3a3d       d576f54b32
#            "a d m i n = "
#                          a5514e3a3d ^ 121319165e = b742572c63


# so the final iv we have to submit is 2881a0375f6cb742572c63d576f54b32
#                                                      |
#                                                      |
#                                                      |
#                                   (2881a0375f6c  b742572c63  d576f54b32)

# crypto{4u7h3n71c4710n_15_3553n714l}


# authentication is essential hahahaha
