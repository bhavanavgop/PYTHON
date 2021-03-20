import csv
f=open("D:\Bhavana\python3\specificcolum.csv",'r')
content=csv.reader(f)
for x in content:
    print(x)
