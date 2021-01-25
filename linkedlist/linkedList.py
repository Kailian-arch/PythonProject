# things to be finished with this script
# 1. recursion calculus. 
# 2. class functions scope and usage.
# 3. isinstance() function and _getitem_() function hasattri() function
# 4. Errors in python and when to use them.
# 5. 通过继承列表类的方式来改进这个类。 https://www.thinbug.com/q/6560354

from collections import Iterable

class Section(object):
    def __init__(self,nextIndex,value=0): 
        self._value = value
        self._nextIndex = nextIndex
# try to realize this Section part with dictionaries.
class LinkedList(object):
    # 创建的 init 函数和更改增长的 setter 函数 内容抽出合并
    # 这个 create 和 extend 还可以合并一下。

    # 再次重构。做一个 list 的列表。index = 0 用来储存相应的信息和 header 放一个 header 的实例进去。 后面用 index lenth 实际来进行表示。 
    # 由于遇到了无法理解的错误 是一个失败的尝试。

    # def addSections(self,cont):
    #     if isinstance(cont,Iterable):
    #         try:
    #             self._sections[self._lenth-1]._nextIndex = self._lenth
    #             self._sections.append([Section(self._lenth+1+i,inputValue) for i,inputValue in enumerate(cont)])
    #             # self._sections.append([Section(1+lenth+=1,inputValue) for inputValue in cont])
    #             self._lenth += len(cont)
    #             self._sections[self._lenth-1]._nextIndex = -1
    #         except ValueError:
    #             pass
    #     else:
    #         self.addSections([0 for _ in range(len(cont))])
        


    def __init__(self,cont):
        self._lenth = 1
        self._sections = [Section(-1)]
        self.addSections(cont)


    # def makeSections(self,cont):
    #     if isinstance(iter, Iterable):


    
    def _CreateByLenth(self,lenth):
        newSections = [Section(i+1,i) for i in range(self._lenth-1)]
        newSections.append(Section(-1))
        return newSections
    
    def _ExtendSections(self,iter):
        if isinstance(iter, Iterable):
            # try:
            #     self._sections.extend([Section(i+1,j) for i in range(len(iter)), j in iter])
            #     self._sections[self._lenth]._nextIndex = lenth
            # except 
            self._sections.extend([Section(i+1,j) for i in range(len(iter)) for j in iter])
            self._sections[self._lenth]._nextIndex = self._lenth
            self._lenth += len(iter)
        else:
            self._ExtendSections([iter])

    def __init__(self,convey):
        # 这里实现的太丑了 判断应该放到函数里面去 把这几部分重构一下。
        self._lenth = 1
        if isinstance(convey,Iterable):
            self._lenth = len(convey)
        else:
            self._lenth = convey

        self._head = 0 
        self._tail = self._lenth-1
        # tail 的更改 还要一起放在 extend 的函数里面

        self._sections = self._CreateByLenth(convey)
    
    @property
    def lenth(self):
        return self._lenth
    
# delete useless intance-creating function.
# def CreateLinkedList(content):
#     linkedList = LinkedList(content)
#     return linkedList
    

    def SearchByValue(self,value,currIndex=0,searchDepth=0):
    # achieved with recursion
    # if searchDepth == 1000:
    #     raise ValueError('not exist! ')
    # if value == linkedList._sections[currIndex]._value:
    #     return currIndex
    # else:
    #     return SearchByValue(linkedList,value,linkedList._sections[currIndex]._nextIndex,searchDepth+1)+1
    #     we can see in this case that the return value was passed one by one. 
    
    # achieved with iterator.
        def yieldItem(currIndex=currIndex,searchDepth=searchDepth):
            while searchDepth <= self._lenth:
                yield self._sections[currIndex]
                currIndex = self._sections[currIndex]._nextIndex
                searchDepth += 1

        for i in yieldItem():
            if i._value == value:
                return i
    
    
# def AddByValue(linkedList,value,currIndex=0,searchDepth=):
#     linkedList.lenth += 1
#     linkedList.

def TestLinkedChart():
    content = list(range(100,1000))
    linkedList = LinkedList(content)
    # linkedList = LinkedList(list(range(10)))
    print(linkedList.lenth)
    print(linkedList.SearchByValue(45)._value)

if __name__ == '__main__':
    TestLinkedChart()