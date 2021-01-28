import csv
from datetime import datetime
start_time = datetime.now()

result = {}
local_path = "/home/mxnthng/Desktop/20201/Project3/"

for i in range(1,48):
    text_file = open(local_path+"data/data"+str(i)+".txt")
    lines = text_file.readlines()
    for line in lines:
        wordlist = line.split()
        for word in wordlist:
            count = result.get(word,0)
            result[word] = count + 1
    text_file.close()

result_file = open(local_path+"result.csv", mode="w", encoding="utf-8")
writer = csv.writer(result_file)
for key, value in result.items():
    writer.writerow([key, value])

result_file.close()

stop_time = datetime.now()
total_time = stop_time - start_time
print("Total time: ", total_time)