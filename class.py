class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("Name:", self.name)
        print("Username:", self.username)


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 5
members = []
member1 = Member("김예은", "xenddy", "password123")
member2 = Member("백송이", "songsong", "password2")
member3 = Member("백유리", "glass", "password3")
members.extend([member1, member2, member3])
for member in members:
    print(member.name)
    print("\n-------------------")

print("회원 정보:")
for member in members:
    member.display()

# 6
posts = []
for member in members:
    for i in range(3):
        post = Post(f"{member.name}'s Post {i+1}", f"Content of {member.name}'s post {i+1}", member.username)
        posts.append(post)

#posts[0].content='test'

print("\n게시글 정보:")
for post in posts:
    print("제목:", post.title)
    print("내용:", post.content)
    print("작성자:", post.author)
    print("\n-------------------")

# 6-1
print("\n특정 유저가 작성한 게시글의 제목:")
for post in posts:
    if post.author == member3.username:
        print(post.title)

# 6-2
print("\n특정 단어가 포함된 게시글의 제목:")
for post in posts:
    if member2.name in post.content:
        print(post.title)

