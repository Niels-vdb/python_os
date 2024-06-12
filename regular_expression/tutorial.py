import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

abcdeg

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

laurawilliams@bogusemail.com
coreyjefferson@bogusemail.com
jenniferwhite@bogusemail.com
tomdavis@bogusemail.com
neilpatterson@bogusemail.com
laurajefferson@bogusemail.com

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
rat
nat
"""

sentence = "Start a sentence and then bring it to an end"

# raw strings show te escaped charcters
# print('\tTab')
# print(r'\tTab')

# creates search pattern
# pattern = re.compile(r'abc')

# finditer finds all matches to the pattern in the given string
# returns:  <re.Match object; span=(1, 4), match='abc'>
#           <re.Match object; span=(155, 158), match='abc'>
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# print(text_to_search[1:4])
# print(text_to_search[155:158])

# See snippets.txt for all compile formats
# pattern = re.compile(r'coreyms\.com')
# Searching for patterns
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# Searching for patterns in a file
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

# with open('regular_expression/data.txt', 'r') as f:
#     contents = f.read()

#     matches = pattern.findall(contents)

#     for match in matches:
#         print(match)

# findall() returns a list with matched strings
# When used in combination with groups it ONLY returns the groups
# pattern = re.compile(r'[^b]at')

# matches = pattern.findall(text_to_search)
# for match in matches:
#     print(match)


# match() method determents if the RegEx matches at the BEGINING of a string
# Returns a match object: <re.Match object; span=(0, 5), match='Start'>
# Returns None if no match is found
# pattern = re.compile(r'Start')
# matches = pattern.match(sentence)
# print(matches)

# pattern = re.compile(r'sentence')
# matches = pattern.match(sentence)
# print(matches)

# search() method determents if the RegEx matches in a string
# Returns a match object: <re.Match object; span=(0, 5), match='Start'>
# Returns None if no match is found
# pattern = re.compile(r'sentence')
# matches = pattern.search(sentence)
# print(matches)

# pattern = re.compile(r'foobar')
# matches = pattern.search(sentence)
# print(matches)

# Flags

# IGNORECARE/I can be used to match if case is not the same
# pattern = re.compile(r"start", re.IGNORECASE)
# matches = pattern.search(sentence)
# print(matches)

# VERBOSE can be used to enable whitespace and comments
# pattern = re.compile(
#     r"""    [a-z0-9_.+-]+             # local Part 
#             @                         # single @ sign 
#             [a-z0-9-]+                # Domain name 
#             \.                        # single Dot . 
#             [a-z0-9_.-]+              # Top level Domain 
#                      """,
#     re.VERBOSE | re.IGNORECASE
# )
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
