text = input().split('\\')

folder = text[-1].split('.')

file_name = folder[0]
file_extension = folder[1]

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')