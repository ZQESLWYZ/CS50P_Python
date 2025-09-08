name = input("What's is your name? ")

if name == "Harry":
    print("AAA")
elif name == "Ron":
    print("VVV")
else:
    print("Who")
    

match name:
    case "Harry":
        print("Hello")
    case "Harry1":
        print("Hello")
    case "Harry2":
        print("Hello")
    case "A1" | "A2" | "A3":
        print("Yese")
    # 用于表示无匹配情况
    case _: 
        print("Who?")