name = "ada lovelace"
print(name.title())  # 每个单词首字母大写，其他字母小写
print(name.lower())
print(name.upper())

name = "aDa lovELace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

favourite_language = "Python    "
print(favourite_language.rstrip())  # 删除字符串末尾的空白，不会影响原字符串
print(favourite_language)
favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = "\t\nPython    "
print(favourite_language)
print(favourite_language.lstrip())  # 删除字符串前面的空白
print(favourite_language.strip())  # 删除字符串前后的空白

# 看到 P20