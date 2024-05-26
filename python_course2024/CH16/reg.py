import re
# text = "from My number is 09111111113. I am available from 8 to 5 fromit"

# patt = "from"
# print(re.search(patt, text))

# match = re.findall(patt, text)
# print(match)

# #row string
# print(r"\n")

# text = "hello, heabo,hecdo,he56o"
# print(re.findall(r"he[abcl][a-d]o", text))

text = "How are you doing today?"
print(re.findall(r"[1-d]", text))
