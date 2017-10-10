#!usr/bin/python
# encoding=utf-8


class Employee:
    empCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print "员工总数：%d" % Employee.empCount

    def displayEmployee(self):
        print "名字：", self.name, "  年龄：", self.age

emp1 = Employee("张三", 23)
emp2 = Employee("李四", 21)
emp1.displayEmployee()
emp2.displayEmployee()
print "员工总数：%d" % Employee.empCount
