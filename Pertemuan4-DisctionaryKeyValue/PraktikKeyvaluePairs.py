#Bikin dictionary
user = {
    "nama": "Kiara",
    "age": 27,
    "role": 'Jungler'
}

#mengakses value berdasarkan key
print("nama:", user["nama"])
print("usia", user['age'])
print("role:", user["role"])

#menambah keyvalue baru
user["email"] = "MizunhiichiAkiira@gmail.com"
#mehgubah Value
user["age"] = 29

#Hasil Akhir
print(user)