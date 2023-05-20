from datetime import datetime

lists="""
Rice    Rs 100
milk    Rs 30
oil     Rs 80
Sugar   Rs 40
salt    Rs 20
Paneer  Rs 120
Magi    RS 50
Boost   Rs 100
Colgate Rs 20 
"""

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items= {
'Rice' : 100,
'milk'  : 30,
"oil"   : 80,
"Sugar" : 40,
"salt"    : 20,
"Paneer"  : 120,
"Magi"    : 50,
"Boost"   : 100,
"Colgate"  : 20    
}

option = int(input("Enter 1 for list of items:"))
if option==1: print(lists)
def inp1():
 while  True:
    inp1=int(input("If you want buy press 1 or 2 for exit:"))
    if inp1==2:
        
       break
    if inp1==1:
         item=input("Enter items:")
         quantity=int(input("Enter quantity:"))
         if item in items.keys():
          price=quantity*(items[item])
          pricelist.append((item,quantity,items ,price))
          totalprice+=price    
          ilist.append(item)
          qlist.append(quantity)
          plist.append(price)
          gst=(totalprice*5)/100
          finalprice= gst+totalprice
         else:
           print("Soory your entered items is not available")
    else:
        print("your entered wrong number")
        e=(def inp1())
        print (e)
    




inp2=input("can i bill the items yes or no:") 
if inp2=='yes':
   pass
   if finalprice!=0:
      print(25*"=","Super_Market",25*"=")
      for i in range(len(pricelist)):
         print(10*" ",i,10*" ",list[i],10*" ",qlist[i],10*" ",plist[i])          
         print(25*"-","kurnool",25*"-")
         print(25*"*","totalprice",10*" ",totalprice,25*"*")
         print(25*"_","gst",17*" ",gst,25*"_")
         print(25*"_","finalprice",10*" ",finalprice,25*"_")






















        

    

    