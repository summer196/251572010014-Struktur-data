'''difference_update'''
#Menghapus item dalam set yang juga ada pada set lain yang ditentukan

set_a = {1, 2, 3, 4, 7}
set_b = {4, 5, 6, 7, 8}
set_b.difference_update(set_a)
print("difference_update(set_b):", set_b)