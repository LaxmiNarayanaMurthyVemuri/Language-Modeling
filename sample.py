lst=[]
file=open("data/test1.txt","r")
book=file.readlines()
print(book)
for line in book:
    print(line)
    innerlst=line.split(" ")
    print(innerlst)
    lst.append(innerlst)
print(lst)
