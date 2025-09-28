# 更方便的命令行参数
# import sys

# def meows(n: int) -> None:
#     for _ in range(n):
#         print("meow")
        
# def main():
#     if len(sys.argv) != 2:
#         sys.exit(0)
    
#     n: int = int(sys.argv[1])
    
#     meows(n)

# if __name__ == "__main__":
#     main()

import argparse

def meow(n: int):
    return "meow " * n

def main():
    parser = argparse.ArgumentParser(description="The times of meow")

    parser.add_argument("-n")
    args = parser.parse_args()

    print(args.n)
    
    print(meow(int(args.n)))
 
if __name__ == "__main__":
    main()
    
    
