print("Welcome to Nintal")
print('\n')
while True:
    print("Type exit to quit or you can print statements!")
    i = input("> ")
    msg = ''
    error213 = "Error"
    if "print" in i:
        msg = i.replace('print ' , '')
        if '"' in msg:
            msg = msg.replace('"','')
        if ';' in msg:
            msg.replace(';','')
            msg = msg[:-1]
            msg = msg[1:]
        print(msg)
    elif i.lower() == "exit":
        print("Exiting the Nintal!")
        break
    else:
        print(error213)