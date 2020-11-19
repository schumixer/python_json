import json

def flatten(x, name=''):
        if len(x)>0:
            for a in x:
                flatten(x[a], name + a + '/')
        
        else:
            out.append(name[:-1])

file = input("\nEnter the name : ").strip()
res = []
with open (file) as f:
        temp = f.read()
        res = json.loads(temp)

out = []

flatten(res)
for site in out:
    print(site)