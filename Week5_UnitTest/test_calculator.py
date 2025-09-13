from calculator import square

def test():
    if square(2) != 4:
        print("error")
    if square(3) != 9:
        print("error")
        
def main():
    test()
    
if __name__ == "__main__":
    main()
