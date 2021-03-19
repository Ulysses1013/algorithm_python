import string
#シーザー暗号
def caesar_cipher(text:str,shift:int) -> str:
    result = ''
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue

        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]
    return result

if __name__ == '__main__':
    print(caesar_cipher('FDW', -3))
    print(caesar_cipher('CAT', 3))




