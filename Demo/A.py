class Demo1:
    def test(self):
        print('hello test how are you')

class Demo2:
    def test(self):
        print('hello')

class Demo3(Demo2, Demo1):
    pass


d = Demo3()
d.test()
