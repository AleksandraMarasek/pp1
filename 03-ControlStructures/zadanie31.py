time24=str(input('Enter time: 24-hour format(hh:mm):'))

hours=int(time24[:2])

minutes=int(time24[3:])

if hours>0 and hours<=12 and minutes<=59:
    print(f'Time in 12-hour format: {time24} AM')
elif hours>12 and hours <24 and minutes<=59:
    print(f'Time in 12-hour format: {hours-12}:{minutes} PM')
else:
    print('Invalid time. Minutes should be in the range (0,59) and hours should be in the range(0,23)')
