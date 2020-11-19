import json
import csv
def sort(elem):
    return (elem['date'], elem['consumer_id'])
files = list(input("\nEnter the names : ").strip().split())
lines = []
for file in files:
    with open (file) as f:
        temp = f.read().split("\n")
        for line in temp:
            lines.append(json.loads(line))

lines = sorted(lines, key = sort)

for i in range(len(lines)):
    del lines[i]['consumer_id']




keys = ['date', 'message']
with open("output.tsv",'w') as f:
    dict_writer = csv.DictWriter(f, keys, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(lines)  
        

