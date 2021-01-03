# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。

# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，
# 是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。

# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，
# 其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。

# 单例模式
# 动物园类要求有“名字”属性和“添加动物”的方法，
# “添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能

from abc import ABCMeta, abstractmethod,abstractproperty

class Animal(metaclass=ABCMeta):

    # 属性："类型" 、"体型"、"性格"、"是否属于凶猛动物"
    def __init__(self, somatotype,shape,character):
        self.somatotype = somatotype
        self.shape = shape
        self.character = character
        # self.fierce_or_not = None

    @property
    def is_fierce(self):
        return self.somatotype == '食肉' and self.character == '凶猛' and animal_size(self.shape) >= 1

        # return self.somatotype is 50 and self.breed is '食肉类型' and self.character is '凶猛'
    
    @abstractmethod  #下面是抽象方法
    def test(self):
        pass

class Dog(Animal):
    # the properties generally  like Cat,name & is_suitable_as_pets

    # 名字
    def __init__(self,name, somatotype,shape,character):
        # 这一行需要安排吗？
        super(Dog,self).__init__(somatotype,shape,character)
        self.name = name

    # 是否适合作为宠物
    @property
    def is_suitable_as_pets(self):
        return self.character != '凶猛'
        # return self.fierce_or_not

   
    def test(self):
        pass
    
class Cat(Animal):
    # 猫类属性:“叫声”、“名字”、“是否适合作为宠物”

    # 类属性：叫声
    calls = 'miaow'

    # 名字
    def __init__(self,name, somatotype,shape,character):

        super(Cat,self).__init__(somatotype,shape,character)
        self.name = name

    # 是否适合作为宠物
    @property
    def is_suitable_as_pets(self):
        return self.character != '凶猛'
   
    def test(self):
        pass

class Zoo(object):
    def __init__(self,name):
        self.name = name
        self._animals = []

    # add animals
    def add_animal(self, animal):
        for a in self._animals:
            if animal is a:
                return
        # 添加动物
        self._animals.append(animal)
    
    # 动物园是否有某种类型的动物
    def has_animal_of_type(self, type_name):
        for a in self._animals:
            if type_name == type(a).__name__:
                return True
        return False

    def show_animals(self):
        for animal in self._animals:
            print(animal)
        # print(animal for animal in self._animals)

    def __getattr__(self, type_name): 
        print(f'There is   no called type_name:{type_name}')
        # 不存在的属性返回默认值 'OK'
        return False


# 这里需要对type_name传入的参数进行限制，忘了怎么写
def hasattr(zoo, type_name):
    return zoo.has_animal_of_type(type_name)

def animal_size(x): 
    return {
        '小':1,
        '中':2,
        '大':3,
    }.get(x,0)


if __name__ == '__main__':

    z = Zoo('时间动物园')
    # 动物园是否有猫这种动物
    print('动物园是否有猫这种动物', hasattr(z, 'Cat'))
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('小狸花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    print(z._animals)
    # 增加一只到动物园
    dog1 = Dog('大黄狗 1', '食肉', '中', '凶猛')
    z.add_animal(dog1)
    print(z.show_animals)

    # 同一只猫不会被重复添加
    z.add_animal(cat1)
    print(z.animals)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
