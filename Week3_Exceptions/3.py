try:
    x = int(input("What's x?"))
except ValueError:
    print("no")
finally:
    print("yes")