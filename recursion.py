ver = int(input("type in summed number-"))
total = 0 
for i in range(1,ver + 1):
    total  = total + i 
print(total)

def sum(n):
    if n == 0 or n== 1:
        return n 
    else: 
        return n +sum(n-1)

print(sum(6))
print(sum(0))
