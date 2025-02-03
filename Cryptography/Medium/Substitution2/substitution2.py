key = {

    'p' : 's',
    'i' : 'x',
    'c' : 'z',
    'o' : 'q',
    'c' : 'Z',
    't' : 'N',
    'f' : 'V',
}

with open('message.txt', 'r') as handle:
    cipherText = handle.read()

plainText = ''
for aChar in cipherText:
    if aChar.lower() in key:
        plainText += key[aChar.lower()].upper()
    else:
        plainText += aChar.lower()

with open('message.txt', 'w') as handle:
    handle.write(plainText)

print(plainText)

ct = "N6R4M_4N41Y515_15_73D10U5_8E1BF808"
print(ct.lower())