states= ['abia','adamawa''akwaibom','anambra','bauchi','bayelsa''benue','ebonyi','edo','kastina',
         'kebbi','kogi','ogun','osub','ondo','oyo']
user_name= input('enter your state of origin')
if user_name in states:
    print(f"{user_name} is found")
else:
    print( f"{user_name} is not found")
first_letter = user_name[0]
matching_state =[state for state in state stt states.startswith(first_letter)
print(f"state that start with '{first_letter}:matching_state:")
