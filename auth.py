from services import enter_continue
from crud import data_users, create_data


def register():
    print("Register")
    username = input("Masukkan nama anda\t: ")
    password = input("Masukkan password anda\t: ")
    gender = ""
    while True:
        print("Jenis Kelamin:")
        print("[1] Laki-Laki")
        print("[2] Perempuan")
        gender = input("Masukkan jenis kelamin anda\t: ")

        if gender != "1" and gender != "2":
            print("Maaf, di dunia ini hanya memiliki 2 jenis kelamin!")
        else:
            break

    gender = "Laki-Laki" if gender == "1" else "Perempuan"
    new_user = {
        "nama": username,
        "password": password,
        "gender": gender,
        "verif": False,
        "role": "user",
        "riwayat": [],
    }

    for data in data_users:
        if data["nama"] == username and data["password"] == password:
            print("Akun sudah terdaftar, silahkan login atau register!")
            enter_continue()
            return

    create_data(new_user)
    print("Akun berhasil didaftarkan, Mohon tunggu data diverifikasi!")
    enter_continue()


def login():
    print("Login")
    username = input("Masukkan nama anda\t: ")
    password = input("Masukkan password anda\t: ")

    for data in data_users:
        if data["nama"] == username and data["password"] == password:
            return data

    return False
