def perfect_number(low_range,High_range):
     print('perfect numbers are')
     for number in range (low_range,High_range):
          sum=0

          for j in range(1,(number//2)+1):
               if number%j==0:
                    sum=sum+j
                    
          if sum==number:
               print(number,end=" ")

low_range=int(input('enter min range'))
High_range=int(input('enter max range'))

perfect_number(low_range,High_range)
