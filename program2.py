import requests
import logging

logging.basicConfig(filename='webpageclonelog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s'  )
#program to clone a webpage url using python request module 
logging.debug('Start of program')

# Get url from user and store in a new variable page
print('Please enter the webpage url')
page = str(input())
logging.debug('value of url = %s' %(page))

#Sending a get request of the requests module
#to copy contents and store in res
res = requests.get(page)
if(res):
    res.raise_for_status()
    logging.debug('status code: %s' %(res.status_code))
logging.debug('contents of the url retrieved from url')
print('Length of file in KB = %s' %(len(res.text)))

playFile = open('clone.html', 'wb')
logging.debug('destination initialised..')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    logging.debug('Cloning...')
playFile.close()   
logging.debug('Cloning complete') 
print('Web page copied')
logging.debug('End of the program')
    
   