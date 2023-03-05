def getdate():
    import datetime
    return datetime.datetime.now()


r = str(getdate())

print("Enter your Id")
x = int(input())
if x == 2010:
    print("Hello Ankita")
    print("1 for Retrieve OR 2 for Login")
    y = int(input())
    if y == 2:
        print("diet or excerise")
        z = int(input())
        if z == 1:

            print("enter your diet")
            d = input()
            f = open("ankita diet.txt", "a")

            f.write(r)
            f.write(d)

            f.close()
        elif z == 2:
            print("enter your excerise")
            e = input()
            f = open("ankita ex.txt", "w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")
    elif y == 1:
        print("which file you want to retrive")
        k = int(input())
        if k == 1:
            f = open("ankita diet.txt","r")
            print(f.read())
        else:
            g = open("ankita ex.txt", "r")
            print(g.read())
elif x == 8405:
    print("Hello Aadil")
    print("1 for Retrieve OR 2 for Login")
    y = int(input())
    if y == 2:
        print("diet or excerise")
        z = int(input())
        if z == 1:

            print("enter your diet")
            d = input()
            f = open("adil diet.txt", "a")

            f.write(r)
            f.write(d)
            f.close()
        elif z == 2:
            print("enter your excerise")
            e = input()
            f = open("adil ex.txt", "w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")
    elif y == 1:
        print("which file you want to retrive")
        k = int(input())
        if k == 1:
            f = open("adil diet.txt", "r")
            print(f.read())
        else:
            g = open("adil ex.txt", "r")
            print(g.read())
elif x == 1408:
    print("Hello Kartik")
    print("1 for Retrieve OR 2 for Login")
    y = int(input())
    if y == 2:
        print("diet or excerise")
        z = int(input())
        if z == 1:

            print("enter your diet")
            d = input()
            f = open("kartik diet.txt", "a")

            f.write(r)
            f.write(d)
            f.close()
        elif z == 2:
            print("enter your excerise")
            e = input()
            f = open("kartik ex.txt", "w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")
    elif y == 1:
        print("which file you want to retrive")
        k = int(input())
        if k == 1:
            f = open("kartik diet.txt", "r")
            print(f.read())
        else:
            g = open("kartik ex.txt", "r")
            print(g.read())
elif x == 2811:
    print("Hello Nikhil")
    print("1 for Retrieve OR 2 for Login")
    y = int(input())
    if y == 2:
        print("diet or excerise")
        z = int(input())
        if z == 1:

            print("enter your diet")
            d = input()
            f = open("nikhil diet.txt", "a")

            f.write(r)
            f.write(d)
            f.close()
        elif z == 2:
            print("enter your excerise")
            e = input()
            f = open("nikhil ex.txt", "w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")
    elif y == 1:
        print("which file you want to retrive")
        k = int(input())
        if k == 1:
            f = open("nikhil diet.txt", "r")
            print(f.read())
        else:
            g = open("nikhil ex.txt", "r")
            print(g.read())
else:
    print("User id not created")