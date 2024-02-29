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


# Step 5
members = []
member1 = Member("John Doe", "johndoe", "password1")
member2 = Member("Jane Smith", "janesmith", "password2")
member3 = Member("Alice Wonderland", "alicew", "password3")
members.extend([member1, member2, member3])

print("Step 5:")
for member in members:
    print(member.name)


# Step 6
posts = []
for member in members:
    for i in range(3):  # 각 회원당 3개의 게시글 생성
        post = Post(f"{member.name}'s Post {i+1}", f"Content of {member.name}'s post {i+1}", member.username)
        posts.append(post)

print("\nStep 6-1:")
for post in posts:
    print(post.title)

print("\nStep 6-2:")
for post in posts:
    if 'Content' in post.content:  # 'Content'라는 단어가 content에 포함된 게시글만 출력
        print(post.title)
