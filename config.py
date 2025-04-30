from operator import add, sub, mul, truediv


DIGIT_BUTTONS = (f'btn_{i}' for i in range(10))

OPERATOR_BUTTONS = ('btn_sum', 'btn_dif', 'btn_mul', 'btn_sub')

OPERATIONS = {
    '+': add,
    '-': sub,
    '×': mul,
    '/': truediv
}

ZERO_DIVISION_ERROR = 'Division by Zero'
