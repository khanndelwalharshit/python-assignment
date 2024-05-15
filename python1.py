numbers = [12, 75, 150, 180, 145, 525, 50]
new_numbers =[]
for i in numbers:
    
    if i>500 :
        continue
    elif i>150:
        continue
    
    if i%5==0:
        new_numbers.append(i)
    
print(new_numbers)
