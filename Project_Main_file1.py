import json
from datetime import datetime

now = datetime.now()


lifetime = True
customerno = 1
c = open('original_data.json','r') 
d = c.read()
c.close()
s = open("records.txt","a")
f = json.loads(d)
def records(s,name):
    global customerno
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    s.write(f"_______________________________\nCustomer no   -: {customerno}      Date and time {dt_string}\nCustomer Name -: {name}\nProductName   Price\n")
    customerno+=1
def ordered(s,productname,price):
    s.write(f"{productname:14}{price}\n")
while lifetime:
    barno = []
    Qty = []
    total = []
    flag = 0
    flag1 = 0
    name = input("Enter your name :- ")
    no = int(input("how many product have you parchased :"))
    for i in range(no):
      barno.append(int(input("Enter barcode of parchaced products :")))
      if str(barno[i]) not in f.keys():  #special case 1
            flag1 = 1
            print("You entered invalid barcode")
            break
      Qty.append(int(input("Enter quantity you parchaced  :")))
    records(s,name)
    for j in range(no):
      if flag1 == 1: #handled special case 1 
        flag=1
        break
      for i in f.keys():
        if int(i) == barno[j]:
          if Qty[j] >= f[i]['Quantity']: #spcial case 2
            flag = 1
            print(f"We do not hava that much quantity of {f[i]['product_name']}")
            break
          print(f"Product_name: {f[i]['product_name']} | Price of each item: {f[i]['Price']} | Quantity you entered: {Qty[j]} ")
          ordered(s,f[i]['product_name'],f[i]['Price'])
          total.append(int(f[i]["Price"])*Qty[j])
          f[i]['Quantity'] -= Qty[j]  
    if flag == 0:
        print(f"Your total bill is : {sum(total)}")    
    s.write(f"\nTotal bill -: {sum(total)}")
    s.write("\n_______________________________\n")
    new_data = json.dumps(f)
    
    h = open('updated_data.json','w')
    h.write(new_data)
    h.close()
    life = input("Is there any other customer if Yes type 'yes' else type 'no' ")
    if life == 'no':
        lifetime = False
s.close()


 