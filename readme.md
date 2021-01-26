# linkedList

- preview of linkedList.

## Achieved API:
- SearchByValue()
- ExtendSections()
- CreateBylenth()

## to do

- encapsulate the create function. use one function to initialize the class instance and expand it.
- use `MutableSequence` to hide the `._section[]` attribute. 
- or try to inherite from `list` class to hide it.
- achieve addByValue() api

# improvedLikedList

- an adaptation of linkedList. 

## improvemnent

- use `MutableSequence` to hide the `._section[]` attribute. It looks like a list now.

## to do
1. 利用元类组织这几个类型 使用抽象类 通过继承+slots的方式创建 header 和 Linked sections 类型。

    1. 元类 类中类 继承超类  抽象类 分别含义和作用 如何实现 关键字

2. 我的 extend 方法调用的是哪一个内置函数 extend 增加的到底是 section 还是数字