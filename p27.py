def add_contact(contacts,name,phone):
    contacts[name]=phone
    print("Contact saved successfully!")


def search_contact(contacts,name):
    if name in contacts:
        print("Phone Number:",contacts[name])
    else:
        print("Contact not found")


contacts ={}

add_contact(contacts,"Rahul","9563268745")
add_contact(contacts,"Aman","9632542653")
add_contact(contacts,"Riya","9758632568")

search_contact(contacts,"Rahul")
search_contact(contacts,"Riya")
search_contact(contacts,"Karan")