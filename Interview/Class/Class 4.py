class Divide:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def divide(self):
        try:
            result = self.num1 / self.num2
        except ZeroDivisionError as e:
            print(f"error : Divide by zero is not allowed.{e}")
            return None
        except TypeError as e :
            print(f"error :Type error .{e}")
            return None
        else:
            print(f"Division result:{result}")
            return result
        finally:
            print(f"Execution of division is completed")

dr = Divide(10,5)
dr.divide()
dr = Divide(10,0)
dr.divide()






