f  = open( 'secret.jpg'  , 'rb' )

k = f.read()

f.close()

lis = []

for i in k:
    lis.append(int(i))

bytes_array = bytearray( lis )
print(max(lis))
f = open('new.jpg','wb')

f.write(bytes_array)

f.close()
