class vogn:
    __slots__ = ['x', 'y', 'test_val_', 'func']
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.test_val_ = 0;

    def __call__(self, pstr):
        print("Fra call")
        print(pstr)
        return "Retur"

    def __str__(self):
        return "String fra vogn object"

    def __del__(self):
        #print("Buy")
        pass

    def make_func(self, n):
        if n == 1:
            return lambda x: x + 1

        if n == 2:
            return lambda x: x + 2

    def receive_func(self, func):
        self.func = func
        return self.func(10)

    def func_call(self, x):
        return self.func(x)

    @property
    def test_val(self):
        return self.test_val_

    @test_val.setter
    def test_val(self, val):
        if val < 10:
            self.test_val_ = val
        else:
            self.test_val_ = 0    


print ("#Bruger indskriver hvor mange instanser af vogn der skal oprettet (x5)")
antal = int(input("Indskriv antal objecter: "))


print ("#Opretter objecter via list comprehensions gange 5")
a = [vogn(x, y) for x in range(antal) for y in range(5)]


print ("#Udskriver object.x og .y")
for vogn_obj in a:
    print(vogn_obj.x, vogn_obj.y)


print ("#Opretter v=vogn - functors")
v = vogn(1, 2)
v("Fra main")
print(v("Fra main"))


print ("#Modtager 2 forskellige funktioner")
func1 = v.make_func(1)
print(func1(1))
func2 = v.make_func(2)
print(func2(1))


print ("#Sender funktion til object")
print(v.receive_func(lambda x: x))
print(v.func_call(10))
print(v.receive_func(lambda x: x*10))
print(v.func_call(10))


b = "Dette-er-en-test"
print (b[2:11:2])


print ("#Filter")
test_list = [0,1,2,3,4,5,6,7,8,9]
print (list(filter(lambda x: x > 3,test_list)))


print ("#map - gennemløber list med funktion")
print (list(map(lambda x: x*2, test_list)))


print ("#zip og zip *list")
test_list2 = [10,11,12,13]
list3 = list(zip(test_list, test_list2))
print (list3)
l1, l2 = zip(*list3)
print (l1)
print (l2)


print ("Filter using comprehensions")
list4 = [x for x in range(10)]
print (list4)
list4 = [x for x in list4 if x > 4]
print (list4)


#iter next


print ("#generators yield")
def test_gen():
    for x in range(10):
        yield x

gen = test_gen()
for x in gen:
    print (x)
    print (type(gen))
    print (type(x))


#Coroutines (an yield with input)


print ("#get and set")
v.test_val = 9
print (v.test_val)


print ("#str object")
print (v)


