#What is the output?
'''
    code = [[0,1,2],[1,3,4]]
    print(code[1,2])
    Ans = 4
'''
#print only the odd numbers between 1-50
'''
for i in range(1,50,2):
    print(i)
'''
#10
'''
for i in range(1,11):
    for j in range(1,11):
        print(f'({i*j})',end=" ")     
    print()
'''

'''
d = {'a':10, 'b':1, 'c':22}
t = d.keys()
print(d['a'])
b = 22 in d
print(b)
'''
'''
Calories = {"milk":150, "paneer":150, "butter":45}
mcal = Calories['milk']
pcal = Calories['paneer']
bcal = Calories['butter']
print(f'1 cup of Whole milk has {mcal} Calories.')
print(f'60 gms of Paneer has {pcal} Calories.')
print(f'1 tbsp of Butter has {bcal} Calories')
'''
'''
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
A = rectangle(4,5)
A.area()
print(f'{A.area()}')
'''
def RecPascal(n, m=1, prev=[]):
    if m > n+1:
        return []
    elif m == 1:
        return RecPascal(n, m+1 , [1])
    else:
        return [prev] + RecPascal(n, m+1, calculate(prev))

def calculate(prev):
    res = [0]*(len(prev)+1)
    res[0], res[-1] = 1, 1
    for i in range(0,len(res)):
        if res[i] == 0:
            res[i] = prev[i-1] + prev[i]
    return res

for line in RecPascal(8):
    print(line)