
ascii_code = input('Enter ASCII: ')
parity_rule = input('do you want an odd or even parity rule: ')
    
ones = 0


for number in ascii_code:
    if number == '1':
        ones+= 1
    
        
if parity_rule == 'odd':
    if ones % 2 == 0:
        ascii_code = '1' + ascii_code
    else:
        ascii_code = '0' + ascii_code


if parity_rule == 'even':
    if ones % 2 == 0:
        ascii_code = '0' + ascii_code
    else:
        ascii_code = '1' + ascii_code
        
print(ascii_code)