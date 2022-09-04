import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertOneResult

if __name__ == '__main__':
    client: MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")  # conecta no endereco enviado
    db: Database = client["db_test"]  # seleciona a database

    collection_name: str = "collection"
    collection: Collection
    if collection_name not in db.list_collection_names():
        collection = db.create_collection(collection_name)  # cria e retorna a collection
    else:
        collection = db.get_collection(collection_name)

    try:
        nome: str = str(input("Digite o nome do bicho: "))
        idade: int = int(input("Digite a idade do bicho: "))

        obj: dict = {"nome": nome, "idade": idade}
        returned_obj: InsertOneResult = collection.insert_one(obj)
        print(f"Guardou com sucesso. Id do bicho: {returned_obj.inserted_id}")
    except ValueError:
        print("Deu pau parabéns")
