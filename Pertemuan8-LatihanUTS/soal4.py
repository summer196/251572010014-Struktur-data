basket = {'Andi', 'Budi', 'Cici', 'Deni'}
futsal = {'Budi', 'Deni', 'Eko', 'Fani'}

ikut2 = basket.intersection(futsal)
ikut1 = futsal.symmetric_difference(basket)

print(ikut2)
print(ikut1)