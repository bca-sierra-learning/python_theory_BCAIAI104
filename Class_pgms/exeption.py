print("Program started..")
a=10
b=0
c=0
name='abcd'
# print(name[10])
try:
    c = a / b    #exception
except ZeroDivisionError:
    print("handled")



print(f"the result :{c}")
print("Program terminated..")
