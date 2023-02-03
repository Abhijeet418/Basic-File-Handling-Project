import ast
def addstock(item,amount,price):
    stockfile=open("STOCK","a+")
    stockfile.seek(0)
    stockdata=stockfile.read()
    stockfile.close()
    if stockdata=="":
        stockfile=open("STOCK","a+")
        d={"Item":[item],"Amount":[amount],"Price":[price],"Sales":[0]}
        stockfile.write(str(d))
        stockfile.seek(0)
        stockdata=stockfile.read()
        stock=ast.literal_eval(stockdata)
        stockfile.flush()
        stockfile.close()
    else:
        stockfile=open("STOCK","a+")
        stockfile.seek(0)
        stockdata=stockfile.read()
        stock=ast.literal_eval(stockdata)
        stockfile.flush()
        stockfile.close()    
        if item not in stock["Item"]:
            stockfile=open("STOCK","a+")
            stockfile.seek(0)
            stockdata=stockfile.read()
            stockfile.close()
            stock=ast.literal_eval(stockdata)
            stock['Item'].append(item)
            stock['Amount'].append(amount)
            stock['Sales'].append(0)
            stock['Price'].append(price)
            stockfile=open("STOCK","w")
            stockfile.write(str(stock))
            stockfile.flush()
            stockfile.close()
        if item in stock["Item"]:
            stockfile=open("STOCK","a+")
            stockfile.seek(0)
            stockdata=stockfile.read()
            stockfile.close()
            stock=ast.literal_eval(stockdata)
            index=stock["Item"].index(item)
            stock["Amount"][index]+=amount
            stock["Price"][index]=price
            stockfile=open("STOCK","w")
            stockfile.write(str(stock))
            stockfile.flush()
            stockfile.close()
    print("STOCK UPDATED...\n")
def showstock():
    stockfile=open("STOCK","a+")
    stockfile.seek(0)
    stockdata=stockfile.read()
    if stockdata=="":
        d={"Item":["Apple"],"Amount":[20],"Price":[60],"Sales":[0]}
        stockfile.write(str(d))
        stockfile.flush()
        stockfile.close()
    print("SHOWING STOCK \n")
    stockfile=open("STOCK","r")
    stockdata=stockfile.read()
    stock=ast.literal_eval(stockdata)
    for key in stock:
        print(key,end="          ")
    print()
    for i in range(len(stock["Item"])):
        print(stock["Item"][i],stock["Amount"][i],stock["Price"][i],stock["Sales"][i],sep=" "*((len(stock["Item"][i]))-(len(stock["Item"][i])-10)))
    print()    
    stockfile.close()    
def checkstock(item):
    stockfile=open("STOCK","a+")
    stockfile.seek(0)
    stockdata=stockfile.read()
    if stockdata=="":
        d={"Item":["Apple"],"Amount":[20],"Price":[60],"Sales":[0]}
        stockfile.write(str(d))
        stockfile.flush()
        stockfile.close()
    stockfile=open("STOCK","r")
    stockfile.seek(0)
    stockdata=stockfile.read()
    stock=ast.literal_eval(stockdata)
    if item in stock["Item"]:
        if stock["Amount"][(stock["Item"].index(item))] !=0:
            print("ITEM FOUND \n")
            index=stock["Item"].index(item)
            print("ITEM         AMOUNT     PRICE")
            print(item,stock["Amount"][index],stock["Price"][index],sep=" "*((len(stock["Item"][index]))-(len(stock["Item"][index])-10)))
            print()
            return True
        else:
            print(item,"OUT OF STOCK...\n")
    else:
        print(item,"NOT IN STOCK...\n")

def removestock(item,amount):
    stockfile=open("STOCK","a+")
    stockfile.seek(0)
    stockdata=stockfile.read()
    if stockdata=="":
        d={"Item":["Apple"],"Amount":[20],"Price":[60],"Sales":[0]}
        stockfile.write(str(d))
        stockfile.flush()
        stockfile.close()
    elif item not in stockdata:
        print("ITEM NOT FOUND \n")
    elif item in stockdata:
        stockfile.seek(0)
        stockdata=stockfile.read()
        stockfile.close()
        stock=ast.literal_eval(stockdata)
        index=stock["Item"].index(item)
        A=stock["Amount"][index]
        if A<amount:
            print("ITEM AMOUNT UNAVAILABLE...\n")
        else:
            stock["Amount"][index]-=amount    
        stockfile=open("STOCK","w")
        stockfile.write(str(stock))
        stockfile.flush()
        stockfile.close()
        print("ADDED TO THE CART: ",amount,item,"(s)\n")
def showprice(item):
    stockfile=open("STOCK","r")
    stockfile.seek(0)
    stockdata=stockfile.read()
    stock=ast.literal_eval(stockdata)
    if item in stock["Item"]:
        return (stock["Price"][(stock["Item"].index(item))])
    stockfile.close()
def givediscount(item):
    stockfile=open("STOCK","a+")
    stockfile.seek(0)
    stockdata=stockfile.read()
    stock=ast.literal_eval(stockdata)
    if item in stock["Item"]:
        index=stock["Item"].index(item)
        sales=stock["Sales"][index]
        if sales==0:
            return (showprice(item)*0.4)
        elif sales<=10:
            return (showprice(item)*0.25)
        elif sales<=20:
            return (showprice(item)*0.15)
        elif sales<=50:
            return (showprice(item)*0.1)
        elif sales<=100:
            return (showprice(item)*0.05)
        else:
            return 0
    stockfile.close()    
def LOGON():
    ADMIN=open("ADMINS","a+")
    ADMIN.seek(0)
    a=ADMIN.read()
    if a == "":
        print("\nWELCOME TO YOUR STORE PLEASE SIGN UP AS ADMIN TO ACCESS THIS AREA...\n")
        l=input("ENTER USERNAME: ")
        p=input("ENTER PASSWORD: ")
        admins=str({str(l):str(p)})
        ADMIN.write(admins)
        ADMIN.close()
        print("\nTHANK YOU YOU MAY ACCESS THIS AREA NOW...\n")
        return True
    else:
        print(("\nADMIN ACCESS REQUIRED PLEASE LOG IN....\n"))
        admin=input("ENTER USERNAME: ")
        pw=input("ENTER PASSWORD: ")
        ad=ast.literal_eval(a)
        for i in ad:
            user=i
            break
        ps=ad[user]
        if ps == pw and user == admin :
            print("\n WELCOME BACK...\n")
            return True
        else:
            print("INVALID ID OR PASSWORD..TRY AGAIN LATER>>>>")
            return False
        ADMIN.close()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    