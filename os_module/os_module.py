import os
from datetime import datetime


# Get current working directory
print(os.getcwd())

# Navigate to different directory
# os.chdir("/Users/niels/Desktop")
# print(os.getcwd())

# Shows a list of the directory
# If no argument is given it lists the current directory
print(os.listdir())

# Create new directory in the current directory
os.mkdir("test_directory")
print(os.listdir())

# Create new directory with sub directories in the current directory
os.makedirs("new_test_directory/sub_test_dir")
print(os.listdir())


# Deletes directory in the current directory
os.rmdir("test_directory")
print(os.listdir())

# Delete directory with sub directories in the current directory
# This method might create problems try useing os.rmdir()
os.removedirs("new_test_directory/sub_test_dir")
print(os.listdir())


# Rename directory old name first then the new name
# Works with files and directories
os.mkdir("temp_directory")
os.rename("temp_directory", "temp")

# Prints out all information about a file
print(os.stat("demo.html"))
# Size of the file in bytes
print(os.stat("demo.html").st_size)
# Last modified time in timestamp
print(os.stat("demo.html").st_mtime)
# Convert to datetime
mod_time = os.stat("demo.html").st_mtime
print(datetime.fromtimestamp(mod_time))

# # Generates a 3 value tuple
# # (path, dirs in path, files in path)
# for dir_path, dir_names, filenames in os.walk("/Users/niels/Desktop"):
#     print(dir_path)
#     print(dir_names)
#     print(filenames)


# Get environment variables
print(os.environ.get('HOME'))


print(os.path.basename("/tmp/text.txt"))
print(os.path.dirname("/tmp/text.txt"))
print(os.path.join("/tmp/text.txt"))
print(os.path.exists("/tmp/text.txt"))
print(os.path.isdir("/tmp/text.txt"))
print(os.path.isfile("/tmp/text.txt"))
print(os.path.splitext("/tmp/text.txt"))


# To see al methods in a module
print(f"os.path: {dir(os.path)}")
print(f"os.environ: {dir(os.environ)}")

