def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return f'{one} {delimiter} {two}'
text = get_sum('Learn', 'Python')
print(text)
print(text.upper())
