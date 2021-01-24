import base64
import sys

in_file_binary = open(sys.argv[1], 'rb').read()
in_file_b64 = base64.b64encode(in_file_binary)
b64_string = in_file_b64.decode()
print(b64_string)