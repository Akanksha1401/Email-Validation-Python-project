# Check the email
email=input("enter the email:")  #aka@.com
x=0
y=0
z=0
if len(email) >=6:     #condition'A'
    if email[0].isalpha():    #condition'B'
        if("@" in email) and (email.count("@")==1):  #condition 'C'
            if(email[4]==".")^(email[-3]=="."):   #condition 'D'
                for i in email:
                    if i==i.isspace():   #condition 'E'
                        x=1
                    elif i.isalpha():
                        if i==i.upper():
                            y=1
                    elif i.isdigit():
                        continue
                    elif i == "-" or i == "." or i == "@":
                        continue
                    else:
                        z=1
                if x==1 or y==1 or z==1:
                     print("wrong email E")
            else:
                print("right email D")
        else:
            print("wrong email C")
    else:
        print("wrong email B")
else:
    print("wrong email A")



