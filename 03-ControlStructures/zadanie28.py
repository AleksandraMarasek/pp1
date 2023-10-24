facebook=input('Do you have a facebook account?(yes or no): ')
twitter=input('Do you have a twitter account?(yes or no): ')
instagram=input('Do you have a instagram account?(yes or no): ')

if facebook=="yes" :
    facebook=True
if instagram=="yes" :
    instagram=True
if twitter=="yes" :
    twitter=True

if facebook+instagram+twitter>= 2 :
    print('A person can be a good influencer!')
else:
    print('This person can not be a good influencer')