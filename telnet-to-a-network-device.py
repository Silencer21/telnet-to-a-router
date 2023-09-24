import pexpect
#import required modules/packages/library


#define variables

ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

#create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding='utf-8',timeout=20)
result = session.expect(['Username:',pexpect.TIMEOUT])

#check for erros in terminal, if there is display and exit
if result != 0:
    print('-'*3,'FAILURE! creating session for: ',ip_address)
    exit()

#session is expecting username, enter details
session.sendline(username)
result = session.expect(['Password: ',pexpect.TIMEOUT])

#check for error, if exists then display error and exit
if result != 0:
    print('-'*3,'FAILURE! entering username: ', username)

#session is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

#check for error, if exists then display error and exit
if result != 0:
    print('-'*3,'FAILURE! entering password: ',password)
    exit()

#display a success message if successful
print('-'*25)
print('')
print('--- Success! connecting to : ',ip_address)
print('---          username: ',username)
print('---          password: ',password)
print('')
print('-'*25)

#terminate telnet session
session.sendline('quit')
session.close()
