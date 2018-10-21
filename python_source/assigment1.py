
def encryption(text, key):#C[i] = P[i] + K[i]
    results = ""
    j = 0
    key_ = key.upper()
    for i in text:
            if i.isupper():
                results += chr((((ord(i) - 65) + (ord(key_[j]) - 65)) % 26) + 65)
            elif i.islower():
                results += chr((((ord(i) - 97) + (ord(key_[j]) - 97)) % 26) + 97)
            else:
                results += i

            j += 1
            if j >= len(key_)-1:
                j = 0
    return results


def decryption(text, key):
    results = ""
    j = 0
    key_ = key.upper()
    for i in text:
            if i.isupper():
                results += chr((((ord(i) - 65) - (ord(key_[j]) - 65)) % 26) + 65)
            elif i.islower():
                results += chr((((ord(i) - 97) - (ord(key_[j]) - 97)) % 26) + 97)
            else:
                results += i
            j += 1
            if j >= len(key_)-1:
                j = 0
    return results



if __name__=="__main__":
    switch = input("Which operation do you want to perform?\n Etner 'E' for encryption, or 'D' for decryption: ")
    if switch == 'E':
        plaintext = input("Enter plaintext: \n")
        key_in = input("Enter key: ")
        print(encryption(plaintext, key_in))
    elif switch == 'D':
        chipertext = input("Enter chipertext: \n")
        key_in = input("Enter key: ")
        print(decryption(chipertext, key_in))
    else:
        print("invalid value.")
