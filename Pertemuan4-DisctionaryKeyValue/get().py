'''get'''

kontak = {'Kiara': '82114352867', 'Rere': '081290967867', 'Michel': '081295908579'}
print('Nomor Kiara:', kontak.get('Kiara'))
print('Nomor yang tidak ada', kontak.get('Ahmad', 'Ahmad Saha????'))