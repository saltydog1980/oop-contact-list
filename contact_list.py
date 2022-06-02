from functools import cmp_to_key
def sort_by_name(a, b):
    if a['name'] < b['name']:
        return -1
    elif a['name'] > b['name']:
        return 1
    elif a['name'] == b['name']:
        return 0

class ContactList:
    contact_main = {}
    def __init__(self, contact_type):
        self.contact_type = contact_type

        if self.contact_type not in ContactList.contact_main:
            ContactList.contact_main[self.contact_type] = []
        
    def contact(self, name):
        for i, x in enumerate(ContactList.contact_main[self.contact_type]):
            if x['name'] == name:
                print(f"{x['name']}'s phone number is {x['number']}")

    def add_contact(self, name, number):
        self.name = name
        self.number = number
        self.entry = {'name': self.name, 'number': self.number}
        if self.entry not in ContactList.contact_main[self.contact_type]:
            ContactList.contact_main[self.contact_type].append(self.entry)
            ContactList.contact_main[self.contact_type] = sorted(ContactList.contact_main[self.contact_type], key=cmp_to_key(sort_by_name))

    def del_contact(self, name):
        for i, x in enumerate(ContactList.contact_main[self.contact_type]):
            if x['name'] == name:
                ContactList.contact_main[self.contact_type].pop(i)


co_workers = ContactList('co_workers')
friends = ContactList('friends')
family = ContactList('family')

family.add_contact('Susan', '(123)456-7890')
family.add_contact('Robert', '(123)456-7890')
# print(ContactList.contact_main)
# print(family.contact('Susan'))
# family.del_contact('Susan')
print(ContactList.contact_main)



