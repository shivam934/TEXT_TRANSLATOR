import googletrans
dict = googletrans.LANGUAGES
dict1 = {}
count = 0
for i in dict.items():
    if(i[0]== 'hi'):
        print(count)
    dict1[i[1]] = i[0]
    count+=1
print(dict1)