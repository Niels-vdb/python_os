# # Old method
# f = open("file_objects/text.txt", 'r')

# print(f.name)
# print(f.mode)

# f.close()

# # Context manager style
# with open("file_objects/text.txt", 'r') as f:
#     print(f.name)
#     print(f.mode)

# with open("file_objects/text.txt", 'r') as f:
    # For smaller files
    # f_contents = f.read()
    # print(f_contents)


    # Reads all lines
    # f_contents = f.readlines()
    # print(f_contents)

    # Reads one line per execution
    # f_contents = f.readline()
    # print(f_contents, end=(''))
    # f_contents = f.readline()
    # print(f_contents)
    # f_contents = f.readline()
    # print(f_contents)

    # For bigger files itterating over the lines 
    # uses less memory
    # for line in f:
    #     print(line, end=(''))

    # Reads the amount of characters specified as argument
    # f_contents = f.read(50)
    # print(f_contents, end=('\n--'))
    # f_contents = f.read(50)
    # print(f_contents, end=('\n--'))
    # f_contents = f.read(50)
    # print(f_contents, end=('\n--'))
    # f_contents = f.read(50)
    # print(f_contents, end=('\n--'))
    # print()

    # size_to_read = 10
    # f_contents = f.read(size_to_read)

    # Shows carige position
    # print(f.tell())

    # Places carige on location given as argument
    # f.seek(50)
    # print(f.tell())

    # while len(f_contents) > 0:
    #     print(f_contents, end=('*'))
    #     f_contents = f.read(size_to_read)
    # pass

# Writes to a file and creates one if none by that name exists
# This will overwrite the existing data, use 'a' to append 
# to a file
# with open("file_objects/text2.txt", 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('Test')
#     pass