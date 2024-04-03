class Q:
    def __init__(a):
        a.items = [0 for i in range(5)]
        a.en = -1
        a.d = -1
        a.count = 0

    def is_empty(a):
        return a.count == 0
    
    def is_full(a):
        return a.count == len(a.items)
    
    def enQ(a, e):
        if not a.is_full():
            a.en = (a.en +1)%len(a.items)
            a.items[a.en] = e
            a.en += 1
            a.count += 1
        else:
            raise IndexError("Q is full")
        
    def DQ(a):
        if not a.is_empty():
            a.d = (a.d +1)%len(a.items)
            data = a.items[a.d]
            a.items[a.d] = 0
            a.d +=1
            a.count -= 1

            return data

        else:
            raise IndexError("our Queue is underflow")
    
    # def enQ(a, e):
    #     if not a.is_full():
    #         a.en = (a.en +1)%len(a.items)
    #         data = a.items[a.en]
    #         a.items[a.en] = 0
    #         a.en +=1
    #         return data
    #     else:
    #         raise IndexError("Q is full")
        
    def dQ(a):
        if not a.is_empty():
            a.d = (a.d +1)%len(a.items)
            data = a.items[a.d]
            a.items[a.d] = 0
            a.d +=1
            a.count -=1
            return data
        else:
            raise IndexError("Q is khali h")
    
    def enQ(a, e):
        if not a.is_full():
            a.en = (a.en +1)%len(a.items)
            a.items[a.en] = e
            a.en +=1
            a.count +=1

        else:
            raise IndexError("Q is full")


q = Q()
print(q.items)
q.enQ(44)
q.enQ(343)
print(q.items)




#Practice again

class Queue:
    def __init__(self) -> None:
        pass
