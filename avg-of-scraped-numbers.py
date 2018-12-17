fname = input ("Enter a file name") #to open your file
fopen = open ("youfilename.txt") #Your file name
count=0 #Declare counter
y=0 #Storage variable
for word in fopen:
    word = word.rstrip()  #to convert string into a list
    word = word.replace(' ','')  #to replace all blanks
    if word.startswith("Keyword you are looking for") : #Enter the keyword you are looking for
        #print(word[19:]) #to verify your code works well
        x=float(word[19:]) #storage in a float variable
        count=count + 1
        z=x+y
        y=z
print(count,z)
avg=z/count
print("Avg is",avg)
