import datetime

def log(*args, **kwargs):
    with open('log.log', 'a', encoding = 'utf-8') as f:
        now = datetime.datetime.now()
        string = '\n● {}'.format(now.strftime("%d-%m-%Y %H:%M"))

        for element in args:
            element = str(element)
            if element[0] == ' ':
                string += '{}'.format(element)

            else:
                string += ' {}'.format(element)

        f.write(string)


def logpr(*args, **kwargs):
    print(*args)
    with open('log.log', 'a', encoding = 'utf-8') as f:
        now = datetime.datetime.now()
        string = '\n● {}'.format(now.strftime("%d-%m-%Y %H:%M"))

        for element in args:
            element = str(element)
            if element[0] == ' ':
                string += '{}'.format(element)

            else:
                string += ' {}'.format(element)

        f.write(string)
