def get_int():
    while True:
        try:
            return int(input("What's s? "))
        except ValueError:
            print("x is not integer")
    
def main():
    x = get_int()
    print(f"x is {x}")

main()

