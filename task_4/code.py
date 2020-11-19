import json

n =7
words = ['station','safety','quality','sales','quarterback',
'stability','standart']
file = 'result.json'

res = {}
for word in words:
    if word[0] not in res:
        res[word[0]] = {word[0:2]:[word]}
    else:
        if word[0:2] not in res[word[0]]:
            res[word[0]][word[0:2]] = [word]
        else:
            res[word[0]][word[0:2]].append(word)

with open(file,'w') as f:
    res = json.dumps(res)
    f.write(res)
