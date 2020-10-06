username = input().split(', ')


for user in username:
    if 3 <= len(user) <= 16:
            if user.isalnum() or '-' in user or '_' in user:
                print(user)

    else:
        continue