N = int(input(''))
TnP = []
for i in range(N):
    tnp = [int(x) for x in input('').split()]
    TnP.append(tnp)
n = len(TnP)
x =0
while x < len(TnP):
    if int(TnP[x][0]) > n:
        TnP.pop(x)
        n = n - 1
        continue
    else:
        n = n - 1
    x += 1   

print(TnP)
new =[]
add = 0
while True:
    if add >= len(TnP):
        break
    day = 0
    money = 0
    index = add
  
    while True:
        day += TnP[index][0]
        money += TnP[index][1]
        index = day
        print(day, money)
        if index >= len(TnP):
            new.append(money)
            add += 1
            break

print(new)
    


