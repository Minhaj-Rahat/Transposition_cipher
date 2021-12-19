#Copyright (c) 2021 Minhajul-Alam-Rahat

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import math


def cipherMat(plaintext, key):
    key = str(key)  # int to str casting
    length = len(key)  # length of column
    ciphertextList = plaintext.split(" ")  # removing the space in the text
    plaintextC = ""                        # hold the text without space
    for i in range(len(ciphertextList)):
        plaintextC += ciphertextList[i]

    rows, cols = (math.ceil(len(plaintextC) / length), length)
    ciphertextMat = [[0 for i in range(cols)] for j in range(rows)]
    countWord = 1

    for row in range(rows):

        for count in range(cols):
            if countWord>len(plaintextC):
                ciphertextMat[row][count] = "X"            #constant bit to pad
            ciphertextMat[row][count] = plaintextC[count + row * length]

    return ciphertextMat


def cipherText(cipherMat, key):
    ciphertext = ""
    key = str(key)
    length = len(key)
    keyDict = {}
    for i in range(len(key)):
        keyDict[key[i]] = i

    keys = sorted(key)
    cols = len(cipherMat[0])
    rows = len(cipherMat)

    for count in range(cols):
        for row in range(rows):
            ciphertext += cipherMat[row][keyDict[keys[count]]]

    return ciphertext


def dechiperMat(cipherText, key):
    key = str(key)  # int to str casting
    length = len(key)  # length of column
    rows, cols = (math.ceil(len(cipherText) / length), length)
    deciphertextMat = [[0 for i in range(cols)] for j in range(rows)]
    keyDict = {}                                         # the dictionary to hold the column numbers for respective keys

    for i in range(len(key)):
        keyDict[key[i]] = i

    keys = sorted(key)
    pointer = 0
    for count in range(cols):
        for row in range(rows):
            deciphertextMat[row][keyDict[keys[count]]] = cipherText[pointer]
            pointer += 1

    return deciphertextMat


def decipherText(decipherMat, key):
    deciphertext = ""
    key = str(key)
    length = len(key)
    rows, cols = (len(decipherMat), length)
    for row in range(rows):
        for col in range(cols):
            deciphertext += decipherMat[row][col]

    return deciphertext


key = 4213                               # given key
text = "Thank You"                       # given plain text
print("The plaintext is \"Thank You\"")
print("The Cipher Matrix is:")
cipher_mat = cipherMat(text, key)
print(cipher_mat)
cipher_text = cipherText(cipher_mat,key)
print("The Cipher Text is: " + cipher_text)
print("The Decipher Matrix is")
decipher_mat = dechiperMat(cipher_text, key)
print(decipher_mat)
decipher_text = decipherText(decipher_mat, key)
print("The Deciphered Text is")
print(decipher_text)

