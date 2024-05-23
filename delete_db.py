import os

def delete_database():
    database_file = 'database.db'
    if os.path.exists(database_file):
        os.remove(database_file)
        print("Banco de dados deletado com sucesso.")
    else:
        print("O banco de dados não existe.")

if __name__ == "__main__":
    delete_database()