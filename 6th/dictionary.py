f = open("D:\Bhavana\python4\dictionary.csv", "a")
import json
thisdict = {
"Fname":"BHAVANA",
"Lname":"VENUGOPAL",
"collage":"SJCET"
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open("D:\Bhavana\python4\dictionary.csv", "r")
print(f.read())