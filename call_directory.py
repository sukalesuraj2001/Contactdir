print("--------------------------------------------------------")
print("-- Welcome to contact directory console application --")
print("--------------------------------------------------------")
print()
while True:
    print("The options are: \n")
    print("----------------------")
    print()
    print("1.Create Contact : ")
    print()
    print("2.View Contact :")
    print()
    print("3.Search Contact by Name :")
    print()
    print("4.Search Contact by Number :")
    print()
    print("5.Exit")
    print("----------------------------")
    print()
    ch=int(input("Enter your choice:"))
    print()
    import write as w

    if ch==1:
       w.create_contact()
       pass
    elif ch==2: 
        w.read()
        pass
        
    elif ch==3:
        w.name_search()
        pass
        
    elif ch==4:
        mn=int(input("Enter the number"))
        a,b= w.number(mn)
        # print(a)
        print(b)
        if b==1:
            print("Number Found")
            print(a)
        else:
            print("Not Found")
        pass
    

    elif ch==5:
        break
    else:
        print()
        print("Please Enter valid option!!!")
print("You Are Sucessfully Exit!!")
print()
print("Thank You for using Application")
print("------------------------------------")
