



#!/usr/bin/env python3

from os import urandom
from utils import listener

FLAG = b'crypto{????????????????????????????}'


class AES:
    sbox = (
        0x2a, 0x00, 0x7e, 0x54, 0x82, 0xa8, 0xd6, 0xfc, 0x61, 0x4b, 0x35, 0x1f, 0xc9, 0xe3, 0x9d, 0xb7,
        0xbc, 0x96, 0xe8, 0xc2, 0x14, 0x3e, 0x40, 0x6a, 0xf7, 0xdd, 0xa3, 0x89, 0x5f, 0x75, 0x0b, 0x21,
        0x1d, 0x37, 0x49, 0x63, 0xb5, 0x9f, 0xe1, 0xcb, 0x56, 0x7c, 0x02, 0x28, 0xfe, 0xd4, 0xaa, 0x80,
        0x8b, 0xa1, 0xdf, 0xf5, 0x23, 0x09, 0x77, 0x5d, 0xc0, 0xea, 0x94, 0xbe, 0x68, 0x42, 0x3c, 0x16,
        0x44, 0x6e, 0x10, 0x3a, 0xec, 0xc6, 0xb8, 0x92, 0x0f, 0x25, 0x5b, 0x71, 0xa7, 0x8d, 0xf3, 0xd9, 
        0xd2, 0xf8, 0x86, 0xac, 0x7a, 0x50, 0x2e, 0x04, 0x99, 0xb3, 0xcd, 0xe7, 0x31, 0x1b, 0x65, 0x4f,
        0x73, 0x59, 0x27, 0x0d, 0xdb, 0xf1, 0x8f, 0xa5, 0x38, 0x12, 0x6c, 0x46, 0x90, 0xba, 0xc4, 0xee,
        0xe5, 0xcf, 0xb1, 0x9b, 0x4d, 0x67, 0x19, 0x33, 0xae, 0x84, 0xfa, 0xd0, 0x06, 0x2c, 0x52, 0x78,
        0xf6, 0xdc, 0xa2, 0x88, 0x5e, 0x74, 0x0a, 0x20, 0xbd, 0x97, 0xe9, 0xc3, 0x15, 0x3f, 0x41, 0x6b,
        0x60, 0x4a, 0x34, 0x1e, 0xc8, 0xe2, 0x9c, 0xb6, 0x2b, 0x01, 0x7f, 0x55, 0x83, 0xa9, 0xd7, 0xfd,
        0xc1, 0xeb, 0x95, 0xbf, 0x69, 0x43, 0x3d, 0x17, 0x8a, 0xa0, 0xde, 0xf4, 0x22, 0x08, 0x76, 0x5c,
        0x57, 0x7d, 0x03, 0x29, 0xff, 0xd5, 0xab, 0x81, 0x1c, 0x36, 0x48, 0x62, 0xb4, 0x9e, 0xe0, 0xca,
        0x98, 0xb2, 0xcc, 0xe6, 0x30, 0x1a, 0x64, 0x4e, 0xd3, 0xf9, 0x87, 0xad, 0x7b, 0x51, 0x2f, 0x05,
        0x0e, 0x24, 0x5a, 0x70, 0xa6, 0x8c, 0xf2, 0xd8, 0x45, 0x6f, 0x11, 0x3b, 0xed, 0xc7, 0xb9, 0x93, 
        0xaf, 0x85, 0xfb, 0xd1, 0x07, 0x2d, 0x53, 0x79, 0xe4, 0xce, 0xb0, 0x9a, 0x4c, 0x66, 0x18, 0x32, 
        0x39, 0x13, 0x6d, 0x47, 0x91, 0xbb, 0xc5, 0xef, 0x72, 0x58, 0x26, 0x0c, 0xda, 0xf0, 0x8e, 0xa4
    )

    rcon = (0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36)

    gmul2 = (
        0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e, 
        0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e, 
        0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e, 
        0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e, 
        0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e, 
        0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe, 
        0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde, 
        0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe, 
        0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05, 
        0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25, 
        0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45, 
        0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65, 
        0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85, 
        0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5, 
        0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5, 
        0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5
    )

    gmul3 = (
        0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11, 
        0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21, 
        0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71, 
        0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41, 
        0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1, 
        0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1, 
        0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1, 
        0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81, 
        0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a, 
        0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba, 
        0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea, 
        0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda, 
        0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a, 
        0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a, 
        0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a, 
        0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a
    )

    def __init__(self, key):
        self._block_size = 16
        self._round_keys = self._expand_key([i for i in key])
        self._state = []

    def _transpose(self, m):
        return [m[4 * j + i] for i in range(4) for j in range(4)]

    def _xor(self, a, b):
        return [x ^ y for x, y in zip(a, b)]

    def _expand_key(self, key):
        round_keys = [key]

        for i in range(10):
            round_key = []
            first = round_keys[i][:4]
            last = round_keys[i][-4:]
            last = last[1:] + [last[0]]
            last = [self.sbox[i] for i in last]

            round_key.extend(self._xor(self._xor(first, last), [self.rcon[i+1], 0, 0, 0]))
            for j in range(0, 12, 4):
                round_key.extend(self._xor(round_key[j:j + 4], round_keys[i][j + 4:j + 8]))
            round_keys.append(round_key)

        for i in range(len(round_keys)):
            round_keys[i] = self._transpose(round_keys[i])

        return round_keys

    def _add_round_key(self, i):
        self._state = self._xor(self._round_keys[i], self._state)

    def _mix_columns(self):
        s = [0] * self._block_size
        for i in range(4):
            s[i] = self.gmul2[self._state[i]] ^ self.gmul3[self._state[i + 4]] ^ self._state[i + 8] ^ self._state[i + 12]
            s[i + 4] = self._state[i] ^ self.gmul2[self._state[i + 4]] ^ self.gmul3[self._state[i + 8]] ^ self._state[i + 12]
            s[i + 8] = self._state[i] ^ self._state[i + 4] ^ self.gmul2[self._state[i + 8]] ^ self.gmul3[self._state[i + 12]]
            s[i + 12] = self.gmul3[self._state[i]] ^ self._state[i + 4] ^ self._state[i + 8] ^ self.gmul2[self._state[i + 12]]
        self._state = s

    def _shift_rows(self):
        self._state = [
            self._state[0], self._state[1], self._state[2], self._state[3],
            self._state[5], self._state[6], self._state[7], self._state[4],
            self._state[10], self._state[11], self._state[8], self._state[9],
            self._state[15], self._state[12], self._state[13], self._state[14]
        ]

    def _sub_bytes(self):
        self._state = [self.sbox[i] for i in self._state]

    def _encrypt_block(self):
        self._add_round_key(0)

        for i in range(1, 10):
            self._sub_bytes()
            self._shift_rows()
            self._mix_columns()
            self._add_round_key(i)

        self._sub_bytes()
        self._shift_rows()
        self._add_round_key(10)

    def encrypt(self, plaintext):
        ciphertext = b''

        self._state = self._transpose([c for c in plaintext])
        self._encrypt_block()
        ciphertext += bytes(bytearray(self._transpose(self._state)))

        return ciphertext


class Challenge:
    def __init__(self):
        self.before_input = "Welcome to my military grade encryption service! Try it out by encrypting a message. You can even encrypt the flag, you will not be able to decrypt it anyway...\n"
        self.aes = AES(urandom(16))
        self.nb_encryptions = 0

    def challenge(self, your_input):
        if 'option' not in your_input:
            return {'error': 'You must specify an option'}

        if your_input['option'] == 'encrypt_message':
            message = bytes.fromhex(your_input['message'])
            if self.nb_encryptions > 0:
                return {'error': 'You already encrypted a message'}
            if len(message) != 16:
                return {'error': 'Message length must be exactly 16 bytes'}

            self.nb_encryptions += 1
            return {'encrypted_message': self.aes.encrypt(message).hex()}

        elif your_input['option'] == 'encrypt_flag':
            padding_length = 16 - (len(FLAG) % 16)
            padded_flag = FLAG + bytes([padding_length]) * padding_length

            encrypted_flag  = b''
            for i in range(0, len(padded_flag), 16):
                encrypted_flag += self.aes.encrypt(padded_flag[i:i + 16])

            return {'encrypted_flag': encrypted_flag.hex()}

        return {'error': 'Unknown action'}


import builtins; builtins.Challenge = Challenge # hack to enable challenge to be run locally, see https://cryptohack.org/faq/#listener
listener.start_server(port=13406)




# 2a4b2c0baa92ab5a0fa6c7a036673843
# 48bad819eb8c515ad4823fc1bfe74dc6
# e3cb2819a4e906f05f4bbf85287717f1



