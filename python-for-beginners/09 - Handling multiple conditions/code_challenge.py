# Ask a user their name
# If their first name starts with A or B
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

name = input("Enter your name: ")

first_letter = name[0:1]

if first_letter.upper() in ('A', 'B'):
    print("Please go to room AB")
elif first_letter.upper() == 'C':
    print("Please go to room CD")
else:
    last_name = input("Please enter your last name: ")
    last_letter = last_name[0:1]
    if last_letter.upper() == 'Z':
        print("Please go to room Z")
    else:
        print("Please go to room OTHER")
