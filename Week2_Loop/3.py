n = int(input("What's is n?"))

while n < 0:
    n = int(input("What's is n?"))
    
for _ in range(n):
    print("meow")
    
    
while True:
    n = int(input("What's is n?"))
    if n > 0:
        break