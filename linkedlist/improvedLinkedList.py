# 把列表扩展成一个类 可以对其添加方法 如同类一样操作。需要理解列表的实现方式 通过 python 内置提供的这种抽象基类来建立新式的列表。
# 1. 利用元类组织这几个类型 使用抽象类 通过继承+slots的方式创建 header 和 Linked sections 类型。
#   1. 元类 类中类 继承超类  抽象类 分别含义和作用 如何实现 关键字
# 2. 我的 extend 方法调用的是哪一个内置函数 extend 增加的到底是 section 还是数字

# 不要尝试将列表的第 0 项特殊化。
from collections import Iterable
from collections import MutableSequence

class Section(object):
    def __init__(self,nextIndex,value=0):
        self.value = value
        self._nextIndex = nextIndex

class Header(object):
    def __init__(self,size,endSign):
        self.size = size
        self.endSign = endSign

class LinkedList(MutableSequence):

        # def standarlizeInput(self,cont):
        #     if isinstance(cont,iterable):
        #         return cont
        #     else:
        #         return [0 for i in range(cont)]

    def __init__(self,cont,endSign=-1):
        super(LinkedList,self).__init__()
        def initSections(cont,endSign=-1): 
        # 这个 def 是写在 init 里面比较好还是写在 init 外面比较好 ？ 因为外面不需要继续调用这个函数 写在里面可以防止不必要的调用 修正作用域 另一方面也表示创建者不希望在外面调用这个函数。
            def standarlizeInput(cont):
                if isinstance(cont,Iterable):
                    return cont
                else:
                    return [0 for i in range(cont)]
            cont = standarlizeInput(cont)
            # 函数变更的时候能够改变类型？ 应该是可以的 动态语言 确定是可以的。
            tempList = [Header(len(cont),endSign)]
            tempList.extend([Section(i,value) for i,value in enumerate(cont)])
            return tempList
        self._list = initSections(cont,endSign)
        # 合并 standatlize 函数和 initsections 函数 使得初始化调用语句变得简单

    @property
    def size(self):
        return self._list[0].size

    @property
    def endSign(self):
        return self._list[0].endSign

    def __getitem__(self,index):
        if index == 0:
            return None
        return self._list[index].value
    # actually has included del method. 

    # def __delitem__(self, index):
    #     """Delete an item"""
    #     del self._list[index]

    def __len__(self):
        """List length"""
        # len 返回的多了一项 header 而这是希望被隐藏的。
        # return len(self._list)-1 
        return self._list[0].size

    def __setitem__(self, index, val):
        # optional: self._acl_check(val)
        self._list[index].value = val

    def __delitem__(self, ii):
        """Delete an item"""
        # strenthen 适应 ii 为首项和末项的情况
        # self._list[ii-1].
        del self._list[ii]

    def insert(self, index, val):
        # optional: self._acl_check(val)
        # TODO: strenthen 适配在最后的情形 在 index 为 0 时返回错误
        self._list.insert(index, Section(index+1, val))

    def append(self, val):
        # 调用已经有的方法来创建新的方法 不戳 是个好的思想 提高代码复用率。
        self.insert(len(self._list), val)

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __str__(self):
        # print(Lklst) 调用的是 str 这个方法
        # return 0
        return str(self._list)


def TestLinkedList():
    lklst = LinkedList(list(range(10,100)))
    print("link list values %d for index %d" % (lklst[10], 10))
    print(len(lklst))

if __name__ == "__main__":
    TestLinkedList()