# region Exercise 1

MINIMUM_AGE = 18

def check_and_validate_user(users_list):
    validate_users = []
    for user in users_list:
        age = user[1]
        status = user[2]
        if age >= MINIMUM_AGE and status == "active":
            validate_users.append(user[0])
    return validate_users

user_list = [
            ["Dan", 25, "active"],
            ["Noa", 16, "active"],
            ["Yael", 30, "inactive"],
]
print(check_and_validate_user(user_list))

# endregion