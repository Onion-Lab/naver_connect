class inventory() :
    def __init__(self) :
        self.item = []


class inventory2() :
    def __init__(self) :
        self.__item = []

class inventory3() :
    def __init__(self) :
        self.__item = []

    @property
    def item(self) :
        return self.__item




a = inventory()
b = inventory2()
c = inventory3()

a.item.append(1)
print(a.item)

c.item.append(1)
print(c.item)

b.__item.append(1)
print(b.__item)