import ast
from datetime import datetime
def addbill(item,amount,price,discount):
    price=price-discount
    price=price*amount
    discount=discount*amount
    bill=open("BILL","a+")
    bill.seek(0)
    billdata=bill.read()
    bill.close()
    if billdata=="":
        bill=open("BILL","a+")
        b={"Item":[item],"Amount":[amount],"DiscPrice":[price],"Discount":[discount]}
        bill.write(str(b))
        bill.seek(0)
        billdata=bill.read()
        bil=ast.literal_eval(billdata)
        bill.flush()
        bill.close()
    else:
        bill=open("BILL","a+")
        bill.seek(0)
        billdata=bill.read()
        bil=ast.literal_eval(billdata)
        bill.flush()
        bill.close()    
        if item not in bil["Item"]:
            bill=open("BILL","a+")
            bill.seek(0)
            billdata=bill.read()
            bill.close()
            bil=ast.literal_eval(billdata)
            bil['Item'].append(item)
            bil['Amount'].append(amount)
            bil['DiscPrice'].append(price)
            bil['Discount'].append(discount)
            bill=open("BILL","w")
            bill.write(str(bil))
            bill.flush()
            bill.close()
        if item in bil["Item"]:
            bill=open("BILL","a+")
            bill.seek(0)
            billdata=bill.read()
            bill.close()
            bil=ast.literal_eval(billdata)
            index=bil["Item"].index(item)
            bil["Amount"][index]+=amount
            bil["DiscPrice"][index]=price
            bil["Discount"][index]=discount
            bill=open("BILL","w")
            bill.write(str(bil))
            bill.flush()
            bill.close()
    stockfile=open("STOCK","a+")
    stockfile.seek(0)
    stockdata=stockfile.read()
    stock=ast.literal_eval(stockdata)
    if item in stock["Item"]:
        index=stock["Item"].index(item)
        stock["Sales"][index]+=amount
    stockfile.close()
    stockfile=open('STOCK',"w")
    stockfile.write(str(stock))
    stockfile.close()            
def clearbill():
    bill=open("BILL","w")
    bill.write("")
    bill.close()        
def billing(name):
    bill=open("BILL","r")
    bill.seek(0)
    bill_=bill.read()
    if bill_=="":
        print("BILLING FAILED :-| \n")
        clearbill()
    else:    
        b=ast.literal_eval(bill_)
        sales=open('SALES',"a+")
        sales.seek(0)
        taketime=datetime.now()
        givetime=taketime.strftime("%d-%m-%y %H:%M")
        saleread=sales.read()
        sno=1
        if saleread=="":
            rtime=str(sno)+". "+givetime
            s={rtime:b}
            sales.write(str(s))
            sales.close()
        else:
            salesdata=ast.literal_eval(saleread)
            for sale in salesdata:
                sno+=1
            rtime=str(sno)+". "+givetime
            salesdata[rtime]=b
            sales.close()
            sales=open("SALES","w")
            sales.write(str(salesdata))
            sales.close()
        
        print("NAME: ",name)
        print()
        for key in b:
            print("   ",key,end="     ")
        print()    
        sn=0
        billtotal=0
        for i in range(len(b["Item"])):
            sn+=1
            print(sn,end=". ")
            print(b["Item"][i],b["Amount"][i],b["DiscPrice"][i],b["Discount"][i],sep="           ")
            billtotal+=(b["DiscPrice"][i])
        print("TOTAL BILL: INR ",billtotal,"\n")
        bill.close()
        clearbill()
def showsales():
    sales=open("SALES","r")
    sale=sales.read()
    if sale=="":
        print("NO SALES RECORDED YET...\n")
    else:
        salesdata=ast.literal_eval(sale)
        for sale in salesdata:
            print(sale,"for INR ",end="")
            tp=0
            for p in salesdata[sale]['DiscPrice']:
                tp+=p
            print(tp,"\n")
    sales.close()
def addcustomer(name):
    customers=open("CUSTOMERS","a+")
    customers.seek(0)
    customerdata=customers.read()
    if customerdata=="":
        customers.close()
        c={"Name":[name]}
        customers=open("CUSTOMERS","w")
        customers.write(str(c))
        customers.close()   
    else:
        customers.close()
        custom=ast.literal_eval(customerdata)
        custom["Name"].append(name)
        customers=open("CUSTOMERS","w")
        customers.write(str(custom))
        customers.close()           
def showsale(sno):
    sales=open("SALES",'r')
    salesread=sales.read()
    if salesread=="":
        print("INVALID SALE NUMBER")
    else:
        salesdata=ast.literal_eval(salesread)
        salekey=str(str(sno)+". ")
        for sales in salesdata:
            if salekey in sales:
                salesindex=salekey+sales[3:]
                if salesindex[4]==" ":
                    salesindex=salesindex[:4]+salesindex[5:]
                sale=salesdata[salesindex]
                customers=open("CUSTOMERS","a+")
                customers.seek(0)
                customerdata=customers.read()
                if customerdata=="":
                    print("NO CUSTOMER FOUND\n")
                else:
                    custom=ast.literal_eval(customerdata)
                    customername=custom["Name"][sno-1]
                    customers.close()
                    print("NAME: ",customername)    
                for keys in sale:
                    print("     ",keys,end=" ")    
                print()    
                sn=0
                saletotal=0
                for i in range(len(sale["Item"])):
                    sn+=1
                    print(sn,end=". ")
                    print(sale["Item"][i],sale["Amount"][i],sale["DiscPrice"][i],sale["Discount"][i],sep="           ")
                    saletotal+=(sale["DiscPrice"][i])            
                print("TOTAL SALE: INR ",saletotal)
                break 
        else:
            print("INVALID SALE NUMBER \n")  
