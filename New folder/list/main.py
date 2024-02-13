seq=[1,"d",7,"h",3.4,[9,"a",2.4]]
a=0
c=0
for i in seq:
    try:
        a+=i
    except AttributeError:
        a+=i
    except TypeError:
        pass
    if type(i)==list:
      for k in i:  
        try:
            c+=k
        except AttributeError:
            pass 
        except TypeError:
            pass           
print(a+c)        