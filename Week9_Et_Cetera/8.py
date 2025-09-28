# map 映射，对元素批量做操作
def main():
    yell("This", "is", "Cs50!")
    
def yell(*args):
    uppercased = map(str.upper, args)
    print(*uppercased)
    
if __name__ == "__main__":
    main()
    