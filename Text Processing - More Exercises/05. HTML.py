title = input()
article = input()

print('<h1>')
print(f'    {title}')
print('</h1>')
print('<article>')
print(f'    {article}')
print('</article>')

data = input()
while data != 'end of comments':
    comment = data
    print('<div>')
    print(f'    {comment}')
    print('</div>')

    data = input()


