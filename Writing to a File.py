strings_to_write = ['Hello,', 'world']

content_to_write = '\n'.join(strings_to_write)

file = open('output.txt', 'w')

file.write(content_to_write)

file.close()