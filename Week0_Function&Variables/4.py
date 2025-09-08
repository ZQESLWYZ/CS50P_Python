def main():
    name = input("请输入名称")
    Hello(name)
    
def Hello(name="Unknown"):
    print(f"Hello，{name}")
    
main()