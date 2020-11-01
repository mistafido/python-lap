import logging
# Write a program to sum all the elements from n1 to n2 where n1 and n2 are positive integers.

logging.basicConfig(filename='program-1-log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#collect n1 and n2 from user
logging.debug('Start of program')
print('Enter the first number to add:')
n1 = int(input())
logging.debug('value of first integer = %s' %(n1))
print('Enter the second number to add:')
n2 = int(input())
logging.debug('value of second integer = %s' %(n2))
#check if n1 and n2 are positive integers
if(n1 > 0) & (n2 > 0): 
    #sum elements between n1 and n2
    total = 0
    for i in range(n1, n2+1):
        total += i
        sum = total
        logging.debug('i is %s, total is %s' %(i, sum))
    logging.debug('n1 is %s, n2 is %s, sum is %s' %(n1, n2, sum))
    print('Sum of numbers between ' + str(n1) + ' and ' + str(n2) + ' = ' + str(sum))
else: 
    print('Please enter only positive integers')

