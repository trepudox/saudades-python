import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertOneResult, UpdateResult
from bson.objectid import ObjectId
from bson.errors import InvalidId


class UserInputError(Exception):
    pass


def program_logic() -> None:
    while True:
        menu()
        escolha: int = int(input(">>> "))
        pula_linha()

        if escolha == 0:
            break
        elif escolha == 1:
            save_document(connected_collection)
            pula_linha()
        elif escolha == 2:
            update_document(connected_collection)
            pula_linha()
        elif escolha == 3:
            find_by_object_id(connected_collection)
            pula_linha()
        elif escolha == 4:
            find_all_objects_by_name(connected_collection)
            pula_linha()
        elif escolha == 5:
            find_all_objects(connected_collection)
            pula_linha()
        elif escolha == 6:
            delete_object_by_id(connected_collection)
            pula_linha()
        elif escolha == 9:
            menu()
            pula_linha()
        else:
            print("Escolha uma opção válida!")
            pula_linha()


def pula_linha() -> None:
    print()


def connect_to_db_and_retrieve_collection(collection_name: str) -> Collection:
    client: MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")  # cria um client no endereco mencionado
    db: Database = client["db_test_python"]  # seleciona a database

    if collection_name not in db.list_collection_names():
        return db.create_collection(collection_name)  # cria e retorna a collection
    else:
        return db.get_collection(collection_name)


def menu() -> None:
    menu_text: dict = {
        0: "Sair",
        1: "Inserir um documento",
        2: "Atualizar um documento",
        3: "Encontrar um documento pelo ID",
        4: "Encontrar documentos pelo nome",
        5: "Listar todos os documentos",
        6: "Deletar um documento pelo ID",
        9: "Mostra esse menu"
    }

    separator_multiplier: int = 15
    print("-" * separator_multiplier, "MENU", "-" * separator_multiplier)
    print("Selecione uma das seguintes opções:")
    for k, v in menu_text.items():
        print(f"{k} - {v}")


def get_object_id_from_input() -> str:
    return str(input("Digite o ID do objeto: "))


def create_new_document() -> dict:
    try:
        name: str = str(input("Digite o nome do objeto: "))
        age: int = int(input("Digite a idade do objeto: "))
        return {"name": name, "age": age}
    except ValueError:
        print("Não foi possível salvar o documento, os parâmetros são inválidos")
        pula_linha()
        raise UserInputError


def create_object_id(object_id: str) -> ObjectId:
    try:
        return ObjectId(object_id)
    except (InvalidId, ValueError):
        print("O ObjectId informado é inválido")
        pula_linha()
        raise UserInputError


def save_document(collection: Collection) -> None:
    obj_to_save: dict = create_new_document()

    returned_obj: InsertOneResult = collection.insert_one(obj_to_save)
    print(f"O documento foi salvo com sucesso. Id do documento: {returned_obj.inserted_id}")


def update_document(collection: Collection):
    object_id: str = get_object_id_from_input()
    obj_to_update: dict = {"_id": create_object_id(object_id)}
    updated_object: dict = create_new_document()
    update_result: UpdateResult = collection.update_one(obj_to_update, updated_object)

    print(f"O documento foi atualizado com sucesso.")
    print(update_result.raw_result)


def find_by_object_id(collection: Collection) -> None:
    object_id: str = get_object_id_from_input()

    obj_to_find: dict = {'_id': ObjectId(create_object_id(object_id))}
    for s in collection.find(obj_to_find):
        print(s)


def find_all_objects_by_name(collection: Collection) -> None:
    object_name: str = str(input("Digite o nome do objeto: "))
    obj_to_find: dict = {'name': object_name}

    for s in collection.find(obj_to_find):
        print(s)


def find_all_objects(collection: Collection) -> None:
    for s in collection.find():
        print(s)


def delete_object_by_id(collection: Collection) -> None:
    object_id: str = str(input("Digite o ID do objeto: "))
    obj_to_delete: dict = {"_id": create_object_id(object_id)}

    collection.delete_one(obj_to_delete)


if __name__ == '__main__':
    inputted_name: str = str(input("Digite o nome da collection: "))
    pula_linha()
    connected_collection: Collection = connect_to_db_and_retrieve_collection(inputted_name)

    try:
        program_logic()
    except UserInputError:
        program_logic()

    print("Fim da execução")
