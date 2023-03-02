# modules for call_directory




# for contact creation and checking validation of number 
def create_contact():
        fp=open("contact.txt",'a')
        n=input("Enter name")
        mn=input("Enter the mobile number")
        res=validate_mob(mn)
        if res==1:
            a,b=number(mn)
            if b==1:
                print("Number Alreadly Exit")
            else:
             d=n+":"+mn+"\n"
             fp.write(d)
             fp.close()
             print("Contact created successfully!!")
        else:     
            print("Enter the valid Mobile Number!")
# for checking  validation
def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0






# for reading a file
def read():
 fp=open("contact.txt",'r')
# n='itvedant'
 data2=fp.read()
 print(data2)
 fp.close()
 


# for searching name

def name_search():
   name=input("Enter the name ")
   fp=open("contact.txt",'r')
   data=fp.readlines()
   for x in data:
      l=x.split(":")
      if l[0].upper()==name.upper():
         print(x)
   else:
      print("******************")
      print("Name Not Found:!!")
      print("******************")




   # for searching number

def number(mn):
   fp=open("contact.txt", "r")
   # res=validate_mob(num)
   # if res==1:
    
   data=fp.readlines()
   
   for x in data:
      l=x.split(":")
      if int(l[1])== int(mn):
            print("======Call Directory========")
            print("Contact found")
            # print(x) 
            
            return x,1

      else:
        #   print("not found") 
            return "",0 
  
      
    