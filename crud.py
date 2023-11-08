import os

# mengambil Data JSON
import json

# mengambil prettytable dari file prettytable
from prettytable import PrettyTable

# variabel untuk tujuan file yang berisi nama file data users
file_path = "users.json"

if not os.path.isfile(file_path):  #
    with open(file_path, "w") as json_file:
        admin = {"nama": "admin", "password": "admin", "role": "admin"}
        json.dump([admin], json_file, indent=4)


def load_data():
    with open(file_path) as json_file:
        return json.load(json_file)


data_users = load_data()


def save_data(json_data):
    with open(file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)


def create_data(json_data):
    data_users.append(json_data)
    save_data(data_users)


def show_data():
    table_fields = ["nama", "password", "gender", "verif", "role"]
    table = PrettyTable()
    table.padding_width = 5
    table.field_names = ["N0."] + table_fields

    for i, row in enumerate(data_users[1:], start=1):
        row_to_display = [i] + [row[col] for col in table_fields]
        table.add_row(row_to_display)

    print(table)


def update_status(index):
    data_users[index]["verif"] = True
    save_data(data_users)


def delete_user(index):
    del data_users[index]
    save_data(data_users)


def user_screening(username, password, data):
    new_data = data
    for data in data_users[1:]:
        if data["nama"] == username and data["password"] == password:
            data["riwayat"].append(new_data)
            save_data(data_users)
            break


def table_riwayat(data_riwayat, fields):
    table_fields = fields
    # inisialisasi tabel menggunakan prettytable
    table = PrettyTable()
    table.padding_width = 5
    table.field_names = ["NO"] + table_fields

    for i, row in enumerate(data_riwayat, start=1):
        row_to_display = [i] + [row[col] for col in table_fields]
        table.add_row(row_to_display)

    print(table)
