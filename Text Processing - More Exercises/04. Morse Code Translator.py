data = input().split(' ')


text = ''
char = ''
for w in data:

            if w == '|' :
                text += ' '
            if w == '.-':
                char = 'A'
                text += char
            elif w == '-...':
                char = 'B'
                text += char
            elif w == '-.-.':
                char = 'C'
                text += char
            elif w == '-..':
                char = 'D'
                text += char
            elif w == '.':
                char = 'E'
                text += char
            elif w == '..-.':
                char = 'F'
                text += char
            elif w == '--.':
                char = 'G'
                text += char
            elif w == '....':
                char = 'H'
                text += char
            elif w == '..':
                char = 'I'
                text += char
            elif w == '.---':
                char = 'J'
                text += char
            elif w == '-.-':
                char = 'K'
                text += char
            elif w == '.-..':
                char = 'L'
                text += char
            elif w == '--':
                char = 'M'
                text += char
            elif w == '-.':
                char = 'N'
                text += char
            elif w == '---':
                char = 'O'
                text += char
            elif w == '.--.':
                char = 'P'
                text += char
            elif w == '--.-':
                char = 'Q'
                text += char
            elif w == '.-.':
                char = 'R'
                text += char
            elif w == '...':
                char = 'S'
                text += char
            elif w == '-':
                char = 'T'
                text += char
            elif w == '..-':
                char = 'U'
                text += char
            elif w == '...-':
                char = 'V'
                text += char
            elif w == '.--':
                char = 'W'
                text += char
            elif w == '-..-':
                char = 'X'
                text += char
            elif w == '-.--':
                char = 'Y'
                text += char
            elif w == '--..':
                char = 'Z'
                text += char
            elif w == '-----':
                char = '0'
                text += char
            elif w == '.----':
                char = '1'
                text += char
            elif w == '..---':
                char = '2'
                text += char
            elif w == '...--':
                char = '3'
                text += char
            elif w == '....-':
                char = '4'
                text += char
            elif w == '.....':
                char = '5'
                text += char
            elif w == '-....':
                char = '6'
                text += char
            elif w == '--...':
                char = '7'
                text += char
            elif w == '---..':
                char = '8'
                text += char
            elif w == '----.':
                char = '9'
                text += char

print(text)