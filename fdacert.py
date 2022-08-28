import json
import datetime

def register_user(user_json, name, password, age, phn):
    user = {
        "id": 1,
        "name": name,
        "password": password,
        "age": age,
        "phone number": phn,
        "order history": []
    }
    try:
        file = open(user_json, "r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "User already Exists"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except json.JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "success"

print(register_user("users.json","sairam","000000",21,82212121))