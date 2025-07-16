from abc import ABC, abstractmethod
class Ab(ABC):
    def p(self,x):
        print("Value passed: ",x)
    @abstractmethod
    def task(self):
        print("We are inside absclass task")

class tc(Ab):
    def task(self):
        print("We are inside tc task")

test__obj = tc()
test__obj.task()
test__obj.p(100)



