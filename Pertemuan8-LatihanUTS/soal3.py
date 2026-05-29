kalimat = 'apel jeruk apel mangga jeruk apel'
list_kata = kalimat.split()

freq = {}

for kata in list_kata:
    if kata in freq:
        freq[kata] += 1
    else:
        freq[kata] = 1

print(freq)