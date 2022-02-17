calculation_to_hrs = 24


def calculate_days(no_of_days):
    return f"{no_of_days} days are {no_of_days * calculation_to_hrs} hrs"


def validate_and_execute(user_input):
    if user_input.isdigit():
        user_input_val = int(user_input)
        condition_check = (user_input_val > 0)
        if condition_check:
            res = calculate_days(user_input_val)
            print(res)
        elif user_input_val == 0:
            print("entered 0")
    else:
        print("Not a valid no")


user_input = input("number of days\n")
validate_and_execute(user_input)
