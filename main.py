import sys
import platform

print("python version: " + platform.python_version() + "\n")

if len(sys.argv) == 1:
print("One argument is required like in the example bellow")
print("python decode.py C5.D4.89.E2")
else:
    coded_message = sys.argv[1]

coded_message = coded_message.replace('.','')

coded_message = bytearray.fromhex(coded_message)
message = coded_message.decode('utf-8')

# Check if the decode message has valid ascii character 
# if not use another decoding set
flag = False
for i in message:
    if not 0 <= ord(i) <= 127: 
        flag = True
        break

if flag:
    message = coded_message.decode('cp500')

print("\n{" + message + "}\n")
