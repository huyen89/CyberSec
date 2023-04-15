# CyberSec

# AES Algorithm
This repository contains various implementations of the Advanced Encryption Standard (AES) algorithm using different modes of operation. The AES algorithm is a symmetric encryption algorithm widely used for data protection and confidentiality.

# Modes of Operation
ECB (Electronic Codebook): This mode encrypts each block of data independently using the same key. It is a simple and fast mode but not secure, as identical plaintext blocks will result in identical ciphertext blocks.

CBC (Cipher Block Chaining): This mode uses the previous block's ciphertext as an additional input to the encryption of the current block, making it more secure than ECB. However, it requires an initialization vector (IV) and is slower than ECB.

CFB (Cipher Feedback): This mode turns a block cipher into a stream cipher. It encrypts the previous ciphertext block and uses it to encrypt the next plaintext block. It is faster than CBC, but it requires synchronization and is not suitable for random access.

OFB (Output Feedback): This mode turns a block cipher into a stream cipher as well. It generates a keystream independently of the plaintext and encrypts it to produce the ciphertext. It is faster than CBC and CFB, and it can be used for random access.

CTR (Counter): This mode converts a block cipher into a stream cipher using a counter. It generates a unique counter value for each block, which is encrypted and used to produce the keystream. It is faster than CBC and CFB, and it is suitable for random access.
