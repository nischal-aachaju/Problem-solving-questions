word="I love python and I love coding"
word_count={}
word=word.split()
for i in word:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1

for key,value in word_count.items():
    print(f"{key} : {value}")
