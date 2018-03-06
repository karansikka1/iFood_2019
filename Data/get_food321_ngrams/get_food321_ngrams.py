# download getngrams from https://github.com/econpy/google-ngrams
from getngrams import getNgrams
import csv
import time
import random
                    
#query = 'gyoza, tamale pie, kulcha'
corpus = 'eng_2012'
startYear = 2007
endYear = 2008
smoothing = 3
caseInsensitive = True


with open('food-321-classes.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content] 
content = [c.replace('_',' ') for c in content]
content = [c.replace('food','') for c in content]


food_items = []
food_ngrams = []
csvfile = "food-321-ngrams_1.csv"
content_mini = content[0:50]

for i,query in enumerate(content_mini):   
    food_items.append(content_mini[i])
    # print(query)
    url, urlquery, df = getNgrams(query, corpus, startYear, endYear, smoothing, caseInsensitive)
    # print(len(df.columns))
    # print(df)
    if(len(df.columns)>2):
        for col in df.columns:
            if col.count('(All)') == 1:
                df[col.replace(' (All)', '')] = df.pop(col)
            #elif col.count('(All)') == 0:
            #    df.pop(col)
        for row in df[-1:].iterrows():
            index, data = row
            food_ngrams.append(data[-1].tolist())  
        continue
    elif(len(df.columns)==2):
        # print(query,len(df.columns))
        for row in df[-1:].iterrows():
            index, data = row
            food_ngrams.append(data[-1].tolist())  
        continue
    elif(len(df.columns)==1):
        #print(query)
        food_ngrams.append('NaN')  
    if(i%10):
        time.sleep(random.uniform(0, 1)*10)

print(food_items)
print(food_ngrams)
    
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')  
    for (fi, fn) in zip(food_items, food_ngrams):
        writer.writerow([fi,fn])


print(len(food_items))
print(len(food_ngrams))
