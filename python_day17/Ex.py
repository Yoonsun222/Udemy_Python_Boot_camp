class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following= 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

#모든 클래스 이름 맨 첫글자 대문자여야 한다. camelCase는 두번째단어첫글자가대문자 스네이크케이스는 모든게 소문자


user_1 = User("001",  "angela")
user_2 = User("001", "jack")


user_1.follow(user_2)


print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)