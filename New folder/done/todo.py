choice=1
mylist=[]
f=open("todo.txt","w")
f.close()
while choice!=0:
    print('''
             1. ADD TASK
             2. DELETE TASK
             3. VIEW TASK
             4. EDIT TASK
             0. EXIT
             ENTER YOUR CHOICE
              ''')
    choice=int(input())
    if choice==1:
        f=open("todo.txt","r")
        mylist=f.read().splitlines()
        f.close()
        a=input("enter the task")
        mylist.append(a)
        f=open("todo.txt","w")
        f.write('\n'.join(mylist))
        print("task successfully entered")
        f.close()
    elif choice==2:
        file=open("todo.txt","r")
        list2=file.read().splitlines()
        j=1
        for k in list2:
            print(j,end=" ")
            print(k)
            j+=1
        file.close()  
        f=open("todo.txt","w")
        print("enter the number of the task you want to delete ")  
        delchoice=int(input())  
        delchoice-=1
        list2.pop(delchoice)
        print("task deleted")
        f.write("\n".join(list2))
        f.close()
        for i in list2:
            print(i)
    elif choice==3:
        file=open("todo.txt","r")
        list2=file.read().splitlines()
        for h in list2:
            print(h)
        file.close()    
    elif choice==4:
        file=open("todo.txt","r")
        list2=file.read().splitlines()
        file.close()
        k=1
        for h in list2:
            print(k,end=" ")
            print(h)
            k+=1
        print("enter  the number of task you want to edit")
        edchoice=int(input())
        edchoice-=1    
        print(list2[edchoice])
        print("enter the task")
        new1=input()
        list2[edchoice]=new1
        f=open("todo.txt","w")
        f.write("\n".join(list2))
        f.close()
        print("task updated successfully")
    elif choice==0:
        print(" thank you")    
    else:
        print("wrong choice")    


