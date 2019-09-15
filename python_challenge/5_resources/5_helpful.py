"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py 
"""
original = "5_text.pickle"
destination = "5_text_unix.pickle"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))

print("Done. Saved %s bytes." % (len(content)-outsize))
