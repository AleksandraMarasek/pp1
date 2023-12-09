import csv

data = [
    ["first_name", "last_name", "age", "gender", "email"],
    ["Decca", "Blackstone", 52, "Male", "dblackstone0@time.com"],
    ["Elena", "Rechert", 27, "Female", "erechert1@ucoz.com"],
    ["Bibbye", "Norree", 26, "Female", "bnorree2@reddit.com"],
    ["Alasdair", "McCoole", 53, "Male", "amccoole3@foxnews.com"],
    ["Hogan", "Hatrey", 26, "Male", "hhatrey4@zimbio.com"]
    ]

file='studentslist.txt'

with open(file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open(file, mode='r') as file:
    reader = csv.DictReader(file)
    
    print("Students under 30:")
    print("{:<10} {:<10} {:<20}".format("First Name", "Last Name", "Email"))
    
    for row in reader:
        if int(row['age']) < 30:
            print("{:<10} {:<10} {:<20}".format(row['first_name'], row['last_name'], row['email']))

#sth is not working 
