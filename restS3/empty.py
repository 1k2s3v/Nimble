f = open('aaaaa.txt', 'r')
mytext = f.read()

# change text into binary mode:
binarytxt = str.encode(mytext)
print(binarytxt[1])

# save the bytes object
with open('filename_bytes.txt', 'wb') as fbinary:
    fbinary.write(binarytxt)
