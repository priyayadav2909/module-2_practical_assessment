# Gym Reception Desk Program

# Taking input from the user
member_name = input("Enter Member Name: ")
age = int(input("Enter Age: "))
classes_booked = int(input("Enter Number of Classes Booked: "))
monthly_fee = float(input("Enter Monthly Fee: "))

# Checking active membership
membership = input("Is Membership Active? (yes/no): ").lower()

# Converting membership status into Boolean
active_membership = membership == "yes"

# Updating classes using assignment operator
classes_booked += 2

# Checking whether name contains letter 'e'
name_check = "e" in member_name.lower()

# Checking eligibility using identity and logical operators
eligible = (active_membership is True) and (age > 18) and (classes_booked < 2)

# Displaying member details
print("\n========== GYM MEMBER DETAILS ==========")
print(f"Member Name       : {member_name}")
print(f"Age               : {age}")
print(f"Classes Booked    : {classes_booked}")
print(f"Monthly Fee       : Rs. {monthly_fee:.3f}")
print(f"Active Membership : {active_membership}")
print(f"Name Contains 'e' : {name_check}")

# Displaying eligibility
print("\n========== ELIGIBILITY ==========")

if eligible:
    print("Member is Eligible for Gym Classes.")
else:
    print("Member is Not Eligible for Gym Classes.")

print("========================================")