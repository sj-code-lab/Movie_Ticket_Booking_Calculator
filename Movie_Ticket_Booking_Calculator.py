# Movie Ticket Booking Calculator
base_price = 15 # Storing integer in variable
age = 21 # Storing integer in variable
seat_type = 'Gold' # Storing string in variable
show_time = 'Evening' # Storing string in variable

if age > 17: # Creating an if statement to check if variable age is greater than 17
    print('User is eligible to book a ticket') # If age is greater than 17 output: User is eligible to book a ticket 

if age >= 21: # Creating an if statement to check if variable age is greater than or equal to 21
    print('User is eligible for Evening shows') # If age is greater than or equal to 21 output: User is eligible for Evening shows
else: # Using else statement 
    print('User is not eligible for Evening shows') # If age is not greater than or equal to 21 output: User is not eligible for Evening shows

is_member = False # Setting variable to False
is_weekend = False # Setting variable to False

discount = 0 # Storing integer in variable
if is_member and age >= 21: # Creating an if statement to check if is member variable True and age greater than or equal to 21
    discount = 3 # Storing integer in variable 
    print('User qualifies for membership discount') # If is member and age variables are True output: User qualifies for membership discount
else: # Using else statement
    print('User does not qualify for membership discount') # If is member and age variables are False output: User does not qualify for membership discount
print('Discount:', discount) # output: discount amount

extra_charges = 0 # Storing integer in variable
if is_weekend or show_time == 'Evening': # Creating an if statement to check if is weekend variable True or show time variable is equal to Evening
    extra_charges = 2 # Storing integer in variable
    print('Extra charges will be applied') # If is weekend variable True or show time variable is equal to Evening output: Extra charges will be applied
else: # Using else statement
    print('No extra charges will be applied') # If is weekend variable False or show time variable dose not equal Evening output: No extra charges will be applied
print('Extra charges:', extra_charges) # output: extra charges amount

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member): # Creating an if statement to check if age is greater than or equal to 21 or 18 
# and show time variable is not equal to Evening or is member variable True 
# Using parentheses to regroup show time and is member variables 
    print('Ticket booking condition satisfied') # If one of the variables from condition group 1 is met and one variable from condition group 2 is met
# output: Ticket booking condition satisfied

    service_charges = 0 # Storing integer in variable
    if seat_type == 'Premium': # Creating an if statement to check if seat type variable is equal to Premium 
        service_charges = 5 # Storing integer in variable 
    elif seat_type == 'Gold': # Creating an else if statement to check if seat type variable is equal to Gold
        service_charges = 3 # Storing integer in variable
    else: # using else statement
        service_charges = 1 # Storing integer in variable
    print('Service charges:', service_charges) # output: service charge amount

    final_price = base_price + extra_charges + service_charges - discount # Storing the result of base price + extra charges + service charges - discount in variable
    print('Final price of ticket:', final_price) # output: final price amount 
else: # Using else statement
    print('Ticket booking failed due to restrictions') # If neither of the variables from condition group 1 are met and neither of the variable from condition group 2 are met
# output: Ticket booking failed due to restrictions