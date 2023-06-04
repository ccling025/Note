from itertools import count

def generatorA():
    yield 3 #使用後即消失
    yield 2
    yield 1

g = generatorA()

#print(sum(g)) / sorted(g)

for i in count():
    try:
        value = next(g) #return 3 then return 2 next run
        print(value)
    except:
        print("Done printing")
        break

