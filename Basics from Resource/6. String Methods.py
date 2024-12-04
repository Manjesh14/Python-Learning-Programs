# STRING METHODS

# Strip() Method
str1="   Hello World     "
print(str1.strip())

str2="###Hello World##"
print(str2.strip('#'))

str3=" ##Hello World###"
print(str3.strip('#'))

str4="Hello World"
print(str4.strip('HloW'))

# "lstrip()" Method

print(str1.lstrip())

print(str2.lstrip('#'))

print(str1.rstrip())
print(str2.rstrip('#'))

# "split()" Method
x="Hello!$I$am$Manjesh"
print(x.split('$',maxsplit=2))
print(x.split('$',maxsplit=3))
print("I am Manjesh".split())

#"rsplit()"Method
print(x.rsplit('$',maxsplit=2))

#"join()" Method

l1=['H','e','l','l','o']
print(''.join(l1))

a="I am Manjesh"
print(''.join(a))

l2=['I','am','Manjesh']
print(' '.join(l2))

d1={'name':'Adams','country':'US'}
print(" and ".join(d1))

# "replace()" Method
print(a.replace('Manjesh','Manju'))
print(a.replace(' ','-',1))

# "upper()" Method
name="manjesh"
print(name.upper())

# "lower()" Method
Name="MANJESH"
print(Name.lower())

# "capitalize()" Method
print(name.capitalize())
print("14manjesh".capitalize())

# "isupper()" Method
print(name.isupper())
print(Name.isupper())

# "islower()" Method
print(name.islower())
print(Name.islower())

# "isalpha()" Method
print(name.isalpha())
print('12A'.isalpha())
print(a.isalpha())

# "isnumeric()" Method
print('12'.isnumeric())
print('12.3'.isnumeric())
print("4/2".isnumeric())

# "isalnum()" Method
print(name.isalnum())
print('123'.isalnum())
print('14Manjesh'.isalnum())
print(a.isalnum())

# "count()" Method
print(a.count('a'))
print(a.count('a',1,5))
print(a.count('Manjesh',0,len(a)-1))

# "find()" Method
print(a.find("a"))
print(a.find('a',5))
print(a.find('Manjesh'))

# "rfind()" Method
print(a.rfind("a"))
print(a.rfind('a',0,5))
print(a.rfind('Manjesh'))

# "index()" Method
print(a.index("a"))
print(a.index('a',0,5))
print(a.index('Manjesh'))
# print(a.index("R"))  Value Error

# "rindex()" Method
print(a.rindex("a"))
print(a.rindex('a',0,5))