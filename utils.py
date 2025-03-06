def validate_input(prompt, data_type, condition=None):
    while True:
        try:
            user_input = data_type(input(prompt))
            if condition and not condition(user_input):
                raise ValueError
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")
