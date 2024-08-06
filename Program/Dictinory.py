choice = 0
dict1 = {'Name':[],'Phone':[]}
while choice == 6:
    print('''1 - Add Contact
          2 - Delete a Contact
          3 - Edit a Contact
          4 - Search a Contact
          5 - List a Contact
          6 - Exit
          Enter your choice:''')
    
    if choice == 1:
        name = input("Enter the name:")
        phone = input("Enter the phone.no:")
        dict1['Name'] = name
        dict1['Phone'] = phone
    elif choice == 2:
        name = input("Which named contact to delete:")
        if name in dict['name']:
            dict1.pop('name')
            print(dict1)
