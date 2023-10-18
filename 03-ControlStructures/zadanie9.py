all_tasks=int(input('Enter the  number of all tasks:'))
correct=int(input('Enter the number of tasks completed correctly:'))

result=correct/all_tasks

if result>=0.5 :
    print('Test passed')
else:
    print('Test  failed')