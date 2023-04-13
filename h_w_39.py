import json

data = {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}

for key, value in data.items():
    with open(f'{key}.json', 'w', encoding="utf-8") as f:
        json.dump({key: value}, f)
