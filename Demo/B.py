from Demo.A import Demo1
class Bemo:
    def dd(self):
        print('bye bye')
        self.x = Demo1()

    def tt(self):
        self.x.test()

d = Bemo()
d.dd()
d.tt()
