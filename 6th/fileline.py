fo = open("D:\Bhavana\py\demo.txt",'r')
x = []
fo_content = fo.read()
x.append(fo_content)
print(x)
fo.close()