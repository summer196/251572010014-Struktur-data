'''symmetric_difference_update()'''
#Memperbarui set dengan selisih simetris antara set ini dan set lainnya

set_a = {1,2,4,5,6,7,8}
set_b = {6,7,8,9,10,11,12}
set_a.symmetric_difference_update(set_b)
print("perbandingan set b:", set_a )