def validate_args(x, y):
    message = ''
    if not isinstance(x, (int, float)):
        message += f'The first argument type should be int or float. Now it is{type(x)}.\n'
    if not isinstance(y, (int, float)):
        message += f'The second argument type should be int or float. Now it is{type(y)}.\n'
    if message:
        raise ValueError(message)
