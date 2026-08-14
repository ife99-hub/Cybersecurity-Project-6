def check_privileges(role):
    if role == "administrator":
        return "High risk: privileged account"
    elif role == "analyst":
        return "Low risk: analyst account"
    else:
        return "Standard: normal account"

users = [{"username": "admin", "role": "administrator"},
         {"username": "alice", "role": "analyst"},
         {"username": "guest", "role": "guest"}]
for user in users:
    result = check_privileges(user["role"])
    print(f"{user['username']}: {result}")
