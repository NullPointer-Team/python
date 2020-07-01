import uuid


ticket = uuid.uuid1()

try:
    print('Type the name of hte configuration file to load')
    configfile = input('Filename: ')
    with open(configfile, 'r') as configfileObj:
        switchconfig = configfileObj.read()

except:
    x = 'General error with obtaining configuration file'

else:
    x = 'Switch to config file found.'

finally:
    with open("try04.log", "a") as zlog:
        print("\n\nWriting results of routine to log file")
        print(ticket, " - ", x, file=zlog)
