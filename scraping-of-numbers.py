#fget=input("Enter the file name")
fopen=open("youfilename.txt")
count=dict()
for t in fopen:
    if t.startswith("From "):
       #print (t)
       t=t.split()
       #print(t)
       #print(t[1])
       count[t[1]] = count.get(t[1],0) + 1
#print(count.items())
max = 0
for key,value in count.items():
    if max==0 or value>max:
       maxword = key
       max=value
print (maxword,max)
