from sys import argv
#this is how we get vommand line arugment
# print(type(argv))
print(argv)

# if len(argv) <2:
#     print("please provide filename")
# else:
file= open('c:\\CODE\\python_course2024\\myfile.txt')
lines = file.read()    
# print(file)
# print(type(lines))
# print(lines)
linesList =lines.split("\n")
print(linesList)
line_count = len(lines) - 1


wordCountList = []
wordCount = 0
letterCount = 0
for item in linesList:
      wordCountList += item.split(" ") 
      letterCount += len(item)

wordCount = len(wordCountList)
print(wordCountList)
print(f"the word count is {wordCount}")



# for item in wordCountList:
#       letterCount += len(item)

print(f"the letter count is {letterCount}")



