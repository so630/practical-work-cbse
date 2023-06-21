def case(str: str):
    return "lowercase" if str.islower() else "uppercase"

a = input("enter a string: ")
print(case(a))