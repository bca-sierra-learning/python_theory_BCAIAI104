print("Program starting..")
first=10
second=0
c=0
try:
    c=first / second
except ZeroDivisionError:
    print("Exception Caught..") 


print(f"Result is :{c}")
print("Program terminating..")