

################################################## Day 1
with open('D:/adventofcode2022/day1.txt', 'r') as file:
    input_lines = file.read().splitlines()
    
nb_cal=0
elves_cal=[]    

for i in input_lines :
    if i=="":
        elves_cal.append(nb_cal)
        nb_cal=0
    else:
        nb_cal+=int(i)
elves_cal.append(nb_cal)
    
  
max_cal=max(elves_cal)    
elfnb=elves_cal.index(max_cal)+1
    

print("Total Calories carried by the Elf with the most Calories:", max_cal,"elf ist nb",elfnb)


#part 2 
elves_cal=sorted(elves_cal) 
maxthree= sum(elves_cal[-3:])
t=elves_cal[-3:]
print("Total Calories carried by the 3 Elves with the most Calories:", maxthree)


######################################################### Day 2

with open('day2.txt', 'r') as file:
    rounds = file.read()

dic={"A":1,"B":2,"C":3,"X":1,"Y":2,"Z":3," ":""}
for i in dic.keys():
    rounds=rounds.replace(i,str(dic[i]))
rounds=rounds.splitlines()
    
total=0
for i in rounds:
    if i[0]==i[1]:
        total+=3+int(i[1])
    elif i in ("12","23","31"):
        total+=6+int(i[1])
    else:
        total+=int(i[1])
print(total)
    
######## part2


with open('day2.txt', 'r') as file:
    rounds = file.read()

dic={"A":1,"B":2,"C":3,"X":0,"Y":3,"Z":6," ":""}
for i in dic.keys():
    rounds=rounds.replace(i,str(dic[i]))
rounds=rounds.splitlines()

dict={"1":3,"2":1,"3":2}
total=0
for i in rounds:
    if int(i[1])==3:
        total+=3+int(i[0])
    elif int(i[1])==6 :
        total+=int(i[1])+(int(i[0])%3+1)
    else:
        total+=int(i[1])+dict[i[0]]
print(total)



######################################################### Day 3

with open('day3.txt', 'r') as file:
    rucksach = file.read().splitlines()
    
a1=ord("a")-1
a2=ord("A")-27
p=0
for r in rucksach:
    n=len(r)
    u=set(r[0:(n//2)]).intersection(r[(n//2):])
    inter= ord(''.join(u))
    if inter < a1:
        p+= inter-a2
    else :
        p+= inter-a1

print("the sum of the priorities of item types", p)

######################### p2

with open('D:/adventofcode2022/day3.txt', 'r') as file:
    rucksach = file.read().splitlines()
    
a1=ord("a")-1
a2=ord("A")-27
p=0
i=0
while i<len(rucksach)-2 :
    u=set(rucksach[i]) & set(rucksach[i+1]) & set (rucksach[i+2])
    inter= ord(''.join(u))
    if inter < a1:
        p+= inter-a2
    else :
        p+= inter-a1
    i+=3
    
print("the sum of the priorities of item types", p)

######################################################### Day 4


with open('D:/adventofcode2022/day4.txt', 'r') as file:
    pairs = file.read().splitlines()

n=0
for p in pairs:
    p=[int(i) for i in (p.replace(",","-" ).split("-"))]
    if (p[0]<= p[2] and p[3]<= p[1]) or (p[2]<= p[0] and p[1]<= p[3]) :
        n+=1
        
    
print("the nb of assignment pairs where one range fully contain the other ", n)

################# part 2

with open('D:/adventofcode2022/day4.txt', 'r') as file:
    pairs = file.read().splitlines()

n=0
for p in pairs:
    p=[int(i) for i in (p.replace(",","-" ).split("-"))]
    if (p[0]<= p[2] and p[3]<= p[1]) or (p[2]<= p[0] and p[1]<= p[3]) or (p[0]<= p[2]<=p[1]  or p[2]<= p[0]<=p[3]  ):
        n+=1
        
    
print("the nb of assignment pairs the ranges overlap ", n)


######################################################### Day 5

with open('D:/adventofcode2022/day5.txt', 'r') as file:
    step = file.read().splitlines()

n=1
f=3
t=5

a1=["F","T","C","L","R","P", "G", "Q"]
a2=["N","Q","H","W","R","F", "S", "J"]
a3=["F","B","H","W","P","M", "Q"]
a4=["V","S","T","D","F"]
a5=["Q","L","D","W","V","F", "Z"]
a6=["Z","C","L","S"]
a7=["Z","B","M","V","D","F"]
a8=["T","J","B"]
a9=["Q","N","B","G","L","S", "P", "H"]

dicc={1:a1, 2:a2, 3:a3, 4:a4, 5:a5, 6:a6, 7:a7, 8:a8, 9:a9 }

for s in step :
    s=s.split()
    for i in range(0,int(s[n])):
        dicc[int(s[t])].append(dicc[int(s[f])].pop())
    
for i in range(1,len(dicc)+1):
    print(dicc[i][-1],end="")
    
############part 2

with open('D:/adventofcode2022/day5.txt', 'r') as file:
    step = file.read().splitlines()

n=1
f=3
t=5

a1=["F","T","C","L","R","P", "G", "Q"]
a2=["N","Q","H","W","R","F", "S", "J"]
a3=["F","B","H","W","P","M", "Q"]
a4=["V","S","T","D","F"]
a5=["Q","L","D","W","V","F", "Z"]
a6=["Z","C","L","S"]
a7=["Z","B","M","V","D","F"]
a8=["T","J","B"]
a9=["Q","N","B","G","L","S", "P", "H"]

dicc={1:a1, 2:a2, 3:a3, 4:a4, 5:a5, 6:a6, 7:a7, 8:a8, 9:a9 }

for s in step :
    s=s.split()
    nb=int(s[n])
    while nb>=1:
        dicc[int(s[t])].append(dicc[int(s[f])][-nb])
        del dicc[int(s[f])][-nb]
        nb-=1
    
for i in range(1,len(dicc)+1):
    print(dicc[i][-1],end="")


######################################################### 6

with open('D:/adventofcode2022/day6.txt', 'r') as file:
    codemsg = file.read()
  
for i in range(0,len(codemsg)-3) :
    if len(set(codemsg[i:i+4]))==4:
        print( i+4)
        break


############################## part 2

with open('D:/adventofcode2022/day6.txt', 'r') as file:
    codemsg = file.read()
  
for i in range(0,len(codemsg)-3) :
    if len(set(codemsg[i:i+14]))==14:
        print( i+14)
        break


























 

