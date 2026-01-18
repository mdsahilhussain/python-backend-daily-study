def sum_all(*args):

    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6,7))
print(sum_all(1,2,10,3,5,20))

def sum_all(*chai):
    
    return sum(chai)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6,7))
print(sum_all(1,2,10,3,5,20))

# * keyword how to know there is a multiple argument coming form function use

def sum_all(*args):
    print(args) # return in tuple (1,2,3), therefor we use iteration on tuple
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))
