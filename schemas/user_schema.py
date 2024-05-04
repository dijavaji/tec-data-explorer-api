def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "lastName": user["lastName"],
            "address": user["address"],
            "email": user["email"],
            "phone": user["phone"],
            "password": user["password"]
    }


def users_schema(users) -> list:
    return [user_schema(user) for user in users]