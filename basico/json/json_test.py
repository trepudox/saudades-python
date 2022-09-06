import json

if __name__ == '__main__':
    json_string: str = '{"name":"Marco", "age":20, "city":"Sao Paulo"}'
    converted_json: dict = json.loads(json_string)  # turns the JSON into a python dict
    print(converted_json)
    print(type(converted_json))

    print("-" * 50)

    python_dict: dict = {'name': 'Marco', 'age': 20, 'city': 'Sao Paulo'}
    converted_dict: str = json.dumps(python_dict)  # turns the python dict into a string JSON
    print(converted_dict)
    print(type(converted_dict))
