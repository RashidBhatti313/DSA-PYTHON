d = [i for i in range(100000009)]

def find(d, e):
    for i in range(len(d)):
        if d[i] == e:
            return i
        
    else:
        return -1
e = 100006
x = find(d,e)
if x != -1:
    print(f"{x} is par {e} majood hy is {d} main") 
    print(f"this {x} index has {e} elemnt on {d} data")
else:
    print(f"{e} element is not found on this {d}")