#program considers current directory to list contents
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print f
