
email=''' Dear <|NAME|>,

Congratulations, 
You have been selected!!!

Date : <|DATE|>
'''

name=input('Please enter your name : \n')
date=input('Please enter the date at which has to be sent : \n')
email=email.replace("<|NAME|>",name)
email=email.replace("<|DATE|>",date)
print(email)