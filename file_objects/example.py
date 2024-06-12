# Opens a file and writes lines in new file
with open('file_objects/text.txt', 'r') as rf:
    with open('file_objects/text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Copies a picture file
# Uses 'rb' and 'wb' for binary copy
with open('file_objects/Nyssa.JPG', 'rb') as rpf:
    with open('file_objects/Nyssa_copy.JPG', 'wb') as wpf:
        chunk_size = 4096
        rpf_chunk = rpf.read(chunk_size)

        while len(rpf_chunk) > 0:
            wpf.write(rpf_chunk)
            rpf_chunk = rpf.read(chunk_size)
