items = []
while True:
    print("=======================Welcome To Grocery Market========================")
    print("1. View items\n2. Add new items\n3. Purchasing\n4. Searching\n5. Editing\n6. Exit")
    op = input('Enter the number of your choice : ')
    if op == "1":
         print("===================VIEW ITEMS===================")
         print('Total inventory are : ', len(items))
         while len(items) != 0:
             print("Available items")
             for item in items:
                for key, value in item.items():
                    print(key, ":", value)
                    break
                break
             break
    elif op =='2':
        print("==================ADD ITEMS======================")
        print("Adding new items")
        item={}
        item['name'] = input("ITEM NAME : ")
        while True:
            try:
                item['qty']=int(input('Item quantity : '))
                break
            except ValueError:
                print("Enter numeric value")
        while True:
            try:
                item['price'] = int(input("Price $ : "))
                break
            except ValueError:
                print('Enter numeric value')
        print("Item has been added successfully !!")
        items.append(item)
    elif op == '3':
        print("=================PURCHASE ITEM====================")
        print(items)
        pur_item = input('Which item do you want to purchase? Enter name :')
        for item in items:
            if pur_item.lower()==item['name'].lower():
                if item['qty']!=0:
                    print('Pay ', item['price'], 'at checkout counter.')
                    item['qty']-=1
                else:
                    print("Item out of stock")
    elif op == '4':
        print("=================Search Items=====================")
        fd_item = input('Enter the item\'s name to search in market : ')
        for item in items:
            if item['name'].lower() == fd_item.lower():
                print('The item named '+ fd_item + " is displayed below with its details")
                print(item)
            else:
                print("Item not Found")
    elif op == '5':
        print('=================Edit Items=========================')
        it_name = input('Enter the name of the item that you want to edit : ')
        for item in items:
            if it_name.lower() == item['name'].lower():
                print('Current details of '+ it_name)
                print(item)
                item['name']= input('Item name : ')
                while True:
                    try:
                        item['qty']=int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Enter numeric value')
                while True:
                    try:
                        item['price']= int(input('Price $ :'))
                        break
                    except ValueError:
                        print('Enter numeric value')
                print('Item has been successfully updated')
                print(item)
            else:
                print('Item not found')
    elif op == '6':
        print('=======================Exited=======================')
        break
    else:
        print('You have entered invalid option...Please select any option')
