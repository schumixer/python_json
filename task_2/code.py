import json
file = input("Input data:")
lines = []
result ={'1': 0, '2': 0,'3': 0,'4': 0,'5': 0,}
with open (file) as f:
    temp = f.read().split("\n")
    for line in temp:
        if '{' in line and '}' in line:
            lines.append(json.loads(line))
        else:
           result['5']+=1 
print(result)