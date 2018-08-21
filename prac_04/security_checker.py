usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = str(input("Username: "))
access = 0

for i in range(len(usernames)):
    if username == usernames[i]:
        access = 1
if access == 1:
    print("Access Granted")
else:
    print("Access Denied")
