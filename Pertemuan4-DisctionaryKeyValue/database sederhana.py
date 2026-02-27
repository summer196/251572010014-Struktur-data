#Database pengguna sehedernahsna
users = {
    "Kirara": "PW5273",
    "Habibi": "atmindatang",
    "owo": "sawitforlife123"
}

#login check
username = input("Masukan USERNAMENYA WI:")
password = input("Masukan PASSWORDNYA WOK:")

if username in users and users[username] == password:
    print("SUKSES JIERR")
else:
    print("Kurang amal kayanya")

# Daftar login yang ingin dicek
login_attempts = [
("Kirara", "PW5273"),
( "Habibi", "atmindatang"),
("owo", "sawitforlife123"),
]

# Cek semua login
for username, password in login_attempts:
    if username in users and users[username] == password:
        print(f"Login {username}: BERHASIL")
    else:
        print(f"Login {username}: GAGAL - Username atau password salah")