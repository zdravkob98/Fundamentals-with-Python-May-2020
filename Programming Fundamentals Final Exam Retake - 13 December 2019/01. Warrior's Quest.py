skills = input()

while True:
    line = input()
    if line == 'For Azeroth':
        break
    tokens = line.split()
    command = tokens[0]
    if command == "GladiatorStance":
        skills = skills.upper()
        print(skills)
    elif command == "DefensiveStance":
        skills = skills.lower()
        print(skills)
    elif command == 'Dispel':
        index = int(tokens[1])
        letter = tokens[2]
        if 0 <= index < len(skills):
            skills = skills[:index] + letter + skills[index + 1:]
            print('Success!')
        else:
            print('Dispel too weak.')
    elif tokens[1] == 'Change':
        substring = tokens[2]
        second_substring = tokens[3]
        skills = skills.replace(substring, second_substring)
        print(skills)
    elif tokens[1] == 'Remove':
        substring = tokens[2]
        skills = skills.replace(substring, '')
        print(skills)
    else:
        print("Command doesn't exist!")