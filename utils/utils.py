import re


def getSvgImage(path):
    with open('assets/expand.svg', 'r') as file:
        svg_data = file.read()
    return svg_data


def replaceNRoot(pattern, expression):
    def replace_expression(match):
        number1 = match.group(1)
        number2 = match.group(2)
        number3 = match.group(3) if match.group(3) else '1'
        return f'pow({number2}, {number3}/{number1})'
    return re.sub(
        pattern, replace_expression, expression.value)


def format_number(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num
