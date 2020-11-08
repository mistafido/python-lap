import random, logging
#write a program to ask the user to guess a chosen random number in 5 guesses

logging.basicConfig(filename='program-3-log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')

#user is required to enter his name
print('Hello what is your name? ')
name = str(input())
logging.debug('User entered name as %s' %(name))

#secret number is generated 
secretNumber = random.randint(1,20)
logging.debug('The secret number is = %d' %(secretNumber))

print('Well ' + name + ' I am thinking of a number')
print('Try and make a guess of what that number is?')
for guessesTaken in range(1,5):
    #user inputs guess number
    print('Take a guess between 1 and 20:')
    guess = int(input())
    logging.debug('User\'s guess is = %d' %(guess))
    #guess is checked if less than secret number
    if guess < secretNumber:
        print('Your guess is too low')
        logging.debug('%d is less than secretnumber' %(guess))
    #guess is checked if more than secret number 
    elif guess > secretNumber:
        print('Your guess is too high')
        logging.debug('%d is more than secretnumber' %(guess))
    else:
        break
if guess == secretNumber:
    print('Good job ' + name + '! you guessed my number in ' + str(guessesTaken) + ' guesses!!')
    logging.debug('User took %d guesses' %(guessesTaken))
else:        
    print('Nope the response I was thinking of was: ' + str(secretNumber))
    logging.debug('%d is the guessed number'   %(secretNumber))
logging.debug('End of program')