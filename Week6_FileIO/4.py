with open("nameandhome.csv") as f:
    lines = f.readlines()
    # print(lines) ['Harry,Griy\n', 'Hermione,Griy\n', 'Ron,Griy\n', 'Draco,Slyt']
    
for line in lines:
    name, home = line.rstrip().split(',')
    print(f"{name} is in {home}")