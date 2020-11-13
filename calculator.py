class Calculator():
 def __init__(self):
         self.inpu='Y'

 def switch(self):
    while self.inpu=='Y':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
        choice = int(input("Your operation: "))
        if choice==1 or choice==2 or choice==3 or choice==4:

            def add():
              result = a + b
              print(result)
            def sub():
              result = a - b
              print(result)
            def mul():
              result = a * b
              print(result)
            def div():
              result = a / b
              print(result)
            switcher = {
              1: add,
              2: sub,
              3: mul,
              4: div
            }
            switcher.get(choice)()
            self.inpu=input("Do you want more calculator?Y/N")
        else:
            print("Wrong Input")
            self.inpu = input("Do you want more calculator?Y/N")


ob1=Calculator()
print(ob1.switch())