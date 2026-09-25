# global variable
roll_no=0
name=''
sub1_mark,sub2_mark,sub3_mark=0
sum=0
# function to read student data
def read_data():  
    global sub1_mark,sub2_mark,sub3_mark,name 
    name=input("Enter your name:") 
    # reads the 'str' typedata from keyboard
    sub1_mark=input("Enter first subject mark") 
    # converts to 'int'
    sub1_mark=int(sub1_mark)
    sub2_mark=input("Enter second subject mark") 
    # converts to 'int'
    sub2_mark=int(sub2_mark)
    # returns multiple values
    return roll_no,name,sub1_mark,sub2_mark,sub3_mark


# to calculate total mark
def getTotal(firstmark,secondmark,thirdmark):
    global sum
    sum=firstmark + secondmark +thirdmark
    return sum
# to calculate average mark in 3 subject
def getAverage():
    print(sum)
    pass
# to determine student grade
def findGrade():
    pass

# to display student result
def displayResult():
    pass

for number in range(2,5):
    a,b,c,d,e=read_data()
    # stores returned value in 'total'
    total=getTotal()
    getAverage()
    


