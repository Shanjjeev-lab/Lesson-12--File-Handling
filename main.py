file = open('Codingal.txt')
content = file.read()
print(content)
file.close()

file_write = open('Codingal.txt', 'w')
file_write.write('I am a new line')
file.close()

file_append = open('Codingal.txt', 'a')
file_append.write('I am an append line')
file.close()

file_write = open('Codingal.txt', 'w')
file_write.write('Codingal is on a mission to inspire school kids to fall in love with coding./nCoding helps develop logical thinking and problem-solving skills./nCoding jobs are the future. ')
file_write.close()

file.open('Codingal.txt', 'r')
content = file.read()
split_content = file.split('/n')
print("Number of lines: ", len(split_content))
file.close()

f1 = open('newfile.txt', 'r')
f2 = open('Codingal.txt', 'a')

data = f1.read()
f2.write(data)

f1.close()
f2.close()