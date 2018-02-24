import string
import random



usuarios = ['Time1', 'Time2', 'Time3', 'Time4']

# [user]
# usernumber=900
# usersitenumber=1
# username=time1
# usertype=team
# userenabled=t
# usermultilogin=f
# userfullname=[TIME 1]ASAP
# userdesc=[TIME 1]ASAP
# userpassword=20194143

print('[user]')
for usuario in usuarios:
	print('userna')
	print(usuario + ' ' + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)))

