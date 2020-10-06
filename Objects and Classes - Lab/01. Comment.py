class Comment :
    def __init__(self, username, content, likes = 0 ):
        self.username = username
        self.content = content
        self.likes = likes


zdravko = Comment('Zdravko' , 'Bonev', 125)
print(zdravko.username)
print(zdravko.content)
print(zdravko.likes)

