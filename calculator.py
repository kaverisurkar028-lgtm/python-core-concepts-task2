def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b==0: return "Cannot divide by zero"
    return a/b

print("Simple Calculator")
choice = input("Enter 1-Add 2-Sub 3-Mul 4-Div: ")
n1 = float(input("Enter num1: "))
n2 = float(input("Enter num2: "))
if choice=='1': print(add(n1,n2))
elif choice=='2': print(sub(n1,n2))
elif choice=='3': print(mul(n1,n2))
elif choice=='4': print(div(n1,n2)) 
