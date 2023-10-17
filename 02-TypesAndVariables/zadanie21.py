registration_number = input("Enter the vehicle registration number: ")

if registration_number.upper().startswith("KR") or registration_number.upper().startswith("KK"):
    print(True)
else:
    print(False)