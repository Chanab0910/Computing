import pyinputplus as pyip

name = pyip.inputStr('Enter your name: ')
age = pyip.inputInt('Please enter your age: ',
                    min=3,
                    max=120)

print(f'Hello {name}, you will be {age+1} on your next birthday')
