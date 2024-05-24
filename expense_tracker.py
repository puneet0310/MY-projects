expenses=[2200,2350,2600,2130,3190]
print("1",expenses[1]-expenses[0])
total=0
for i in range (0,3):
    total +=expenses[i]
print("2",total)
print("3")
for i in range (0,len(expenses)):
    if expenses[i] == 2000:
        print("Yes")
    else:
        print("No")
print("4")
expenses[3]-=100
print(expenses[3])
