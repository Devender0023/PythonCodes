# Define the Comment class below:
class Comment:
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes

    def description(self):
        return f"{self.username} {self.text}"

    def initials(self):
        return f"{self.username[0].upper()}.{self.username[1].upper()}."

    def senior(self):
        return self.likes > 65

c = Comment("davey123", "lol you're so silly", 45)
another_comment = Comment("rosa77", "soooo cute!!", 72)
# print(c.username)
# print(c.text)
# print(c.likes)
# print(another_comment.username)
# print(another_comment.text)
# print(another_comment.likes)

print(c.description())
print(another_comment.senior())
print(c.initials())
print(c.senior())


