import csv
import math
f=open("class2.csv")
file=csv.reader(f)
df=list(file)
df.pop(0)
marks=[]
for i in range(len(df)):
    num=df[i][1]
    marks.append(float(num))
sum=0
for i in marks:
    sum=sum+i 
mean=sum/len(marks)
sq=[]
for i in marks:
    a=int(i)-mean
    a=a**2
    sq.append(a)
add=0 
for i in sq:
    add=add+i
result=add/(len(marks)-1)
sd=math.sqrt(result)
print(sd) 
import statistics
sd=statistics.stdev(marks)
print(sd)