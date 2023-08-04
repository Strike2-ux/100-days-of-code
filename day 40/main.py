'''name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")'''

def get_contact_info():
    name = input("Name: ").strip().capitalize()
    dob = input("Date of Birth: ").strip()
    tel = input("Telephone number: ").strip()
    email = input("Email: ")
    address = input("Address: ")
    return {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

def print_contact_info(contact):
    print()
    print(f"""Name: {contact["name"]}""")
    print(f"""DOB: {contact["dob"]}""")
    print(f"""Tel: {contact["tel"]}""")
    print(f"""Email: {contact["email"]}""")
    print(f"""Address: {contact["address"]}""")

contact_info = {}
contact_info.update(get_contact_info())
print_contact_info(contact_info)
