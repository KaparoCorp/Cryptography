# Third day at your new cryptoanalyst job and you come across your toughest assignment yet. Your job is to implement a simple keyword cipher. 
#A keyword cipher is a type of monoalphabetic substitution where two parameters are provided as such (msg, keyword). 
#The msg is encrypted by taking the keyword, dropping any letters that appear more than once.
#The rest of the letters of the alphabet that aren't used are then appended to the end of the keyword.

# For example, if your msg was "hello" and your keyword was "wednesday", your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.
                                                                                                          
# To encrypt 'hello' you'd substitute as follows,

#               abcdefghijklmnopqrstuvwxyz
#   hello ==>   |||||||||||||||||||||||||| ==> bshhk
#               wednsaybcfghijklmopqrtuvxz
# hello encrypts into bshhk with the keyword wednesday. This cipher also uses lower case letters only.

# Good Luck.

#https://www.codewars.com/kata/57241cafef90082e270012d8/train/python

import re


LETTERS = 'abcdefghijklmnopqrstuvwxyz'

#encription function
def encrypt(msg, keyword):
    
    msg = msg.lower()
    keyword_new = '' # variable to hold non repeated form of keyword
    for i in range(0, len(keyword)):
        if keyword[i] not in set(keyword_new):
            keyword_new+=keyword[i]
    alphabetNotUsed =''# variable to hold letters not used in keyword
    isMatch = False
    #loop to create none repeate of keyword to letters 
    while(not isMatch):
        for i in LETTERS:
            for m in range(0, len(keyword_new)):
                if i in keyword_new:
                    isMatch = True
                    continue
                else:
                    
                     isMatch = True
                if i not in set(alphabetNotUsed):
                    alphabetNotUsed += i
    #creating cipher text
    CIPHER_LETTERS = keyword_new + alphabetNotUsed
    CIPHER_ENCODER = dict()
    for i in range(0, len(LETTERS)):
        CIPHER_ENCODER[LETTERS[i]] = CIPHER_LETTERS[i]
    print("( - ) Encoding text  " , msg)
    encoded_text = ''
    print(encoded_text)
    for i in msg:
        if i != " ":
            encoded_text += CIPHER_ENCODER[i]
            
        else:
            encoded_text += " "
                     
    return print(encoded_text)

