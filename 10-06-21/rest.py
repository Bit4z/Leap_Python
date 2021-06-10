l=['pizza','burger','noodle','chicken','idli','dosa','paneer','paratha']
print("list of an items:")
print(l)
ch=input("please select the item=")
if ch in l:
    l.remove(ch)
    
    print(l)
else:
    print("Bye Bye Item is not available..")
print(l)
    
