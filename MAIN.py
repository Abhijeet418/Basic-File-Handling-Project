from STOCK import addstock,removestock,showstock,checkstock,showprice,givediscount,LOGON
from BILLING import addbill,billing,clearbill,showsales,showsale,addcustomer
positive=["y","Y","yes","YES","yEs","YEs","yES","yeS","yup","yep","YUP","Yep","Yup","YEP"]
negative=["n","N","No","NO","nO","NOPE","nope","Nope"]
print("\n           WELCOME TO ABHIJEET\' s STORE \n")
while True:
    print("\n1.BUY PRODUCT \n2.MANAGE PRODUCT \n3.SHOW SALES \n4.EXIT \n")
    ask=int(input("Enter Choice: "))
    if ask==1:
        b__=0
        shopping=True
        while shopping:
            product=input("Search for Product: ")
            if checkstock(product):
                price=showprice(product)
                discount=givediscount(product)
                print("YOU WILL BE GIVEN DISCOUNT OF :",discount," PER ITEM. ")
                r=int(input("Required Quantity: "))
                if r<=0:
                    print("PLEASE DONT PURCHASE INVALID AMOUNT :( \n")
                else:    
                    removestock(product,r)
                    addbill(product,r,price,discount)
                    b__ += 1
                    askagain=input("Do you want to CHECKOUT? Y/N \n")
                    if askagain in positive :
                        name=input("Enter your Name: ")
                        billing(name)
                        addcustomer(name)
                        shopping=False
            else:
                askagain=input("Do you want to search anything else ? Y/N \n")
                if askagain in negative :
                    if not b__==0:
                        checkout=input("DO YOU WANT TO CHECKOUT? \n")
                        if checkout in negative :
                            clearbill()
                            print("OKAY..")
                            shopping=False
                        else:
                            name=input("Enter your Name: ")
                            billing(name)
                            addcustomer(name)
                            shopping=False
                    else:
                        shopping=False
    if ask==2:
        if LOGON():
            manager=True
            while manager:
                question=int(input("1.SHOW STOCK \n2.SEARCH STOCK  \n3.ADD STOCK / MODIFY EXISTING  \n4.EXIT  \n"))
                if question==1:
                    showstock()
                    anythingelse=input("ANYTHING ELSE? Y/N \n")
                    if anythingelse in negative:
                        manager=False
                if question==2:
                    check=True
                    while check:
                        item=input("Enter Item: ")
                        checkstock(item)
                        anythingelse=input("DO YOU WANT TO CHECK ANY OTHER ITEM? Y/N \n")
                        if anythingelse in negative :
                            check=False
                if question==3:
                    add=True
                    while add:
                        item=input("Item: ")
                        qty=int(input("Quantity: "))
                        price=int(input("PriceINR: "))
                        if qty<0 or price<0:
                            print("CANT PROCESS NEGATIVE VALUE>>>\n")
                        else:
                            addstock(item,qty,price)
                        anythingelse=input("DO YOU WANT TO ADD\\MODIFY ANY OTHER ITEM? Y/N \n")
                        if anythingelse in negative :
                            add=False
                if question==4:
                    manager=False
    if ask==3:
        if LOGON():
            show=True
            while show:
                showsales()
                select=int(input("SELECT SALE NUMBER TO SHOW BILL: "))
                if select<=0:
                    print("INVALID SALE NUMBER \n")
                else:    
                    showsale(select)
                    anythingelse=input("DO YOU WANT TO SEE ANY OTHER SALE ? Y/N \n")
                    if anythingelse in negative :
                        show=False
    if ask==4:
            print("NOTE: IF YOU HAD ANYTHING IN CART IT HAS BEEN DELETED... \n GOOD BYE !! ")
            clearbill()
            break
        