import re

txt="Hello World ! "
if re.search("^Hello",txt):
    print("Yes")

# search() Function
print(re.search(' ',txt))

# Match Object
print(re.search(' ',txt).span())

# Meta Characters
