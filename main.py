# Einfaches interaktives Anonymisierungs-Tool

def anonymize(data):
    anonymized = []
    for i, entry in enumerate(data):
        anonymized.append({
            "id": f"user_{i+1}",
            "email": f"user_{i+1}@hidden.com"
        })
    return anonymized

# Interaktive Eingabe
users = []
print("Gib Namen und E-Mails ein. Tippe 'stop', wenn fertig.")

while True:
    name = input("Name: ")
    if name.lower() == "stop":
        break
    email = input("Email: ")
    if email.lower() == "stop":
        break
    users.append({"name": name, "email": email})

# Anonymisierung
anon_users = anonymize(users)

# Ausgabe
print("\nAnonymisierte Daten:")
for u in anon_users:
    print(u)