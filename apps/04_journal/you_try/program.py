import journal


def main():  # this is just a "main" method to call which initiates the app
    header()  # call the header function
    event_loop()  # call the event_loop


def header():  # make a header that consists of 3 lines
    print('-' * 30)
    print('       JOURNAL APP')
    print('-' * 30)


def event_loop():  # this is the function that starts the UI
    print('What would you like to do?')  # user prompt
    cmd = 'init'  # the cmd variable is used to capture user data
    journal_name = 'default'  # name the journal default
    journal_data = journal.load(journal_name)  # a variable that contains the output of journal.load(journal_name)

    while cmd != 'x' and cmd:  # while cmd is not x and cmd has something in it
        cmd = input('Press L to [L]ist entries, A to [A]dd entry, and X to e[x]it: ')  # prompt for entry
        cmd = cmd.lower().strip()  # strip the whitespace on right

        if cmd == 'l':
            list_entries(journal_data)  # call list_entries, pass journal_data (list)
        elif cmd == 'a':
            add_entries(journal_data)  # call add_entries, pass journal_data (list)
        elif cmd != 'x' and cmd:
            print('"{}" Not valid, try again'.format(cmd))

    print('Saving... Goodbye!')
    journal.save(journal_name, journal_data)  # on exit call journal.save w/ the name of the journal and list


def list_entries(data):
    entries = reversed(data)  # reverse the list
    for idx, entry in enumerate(entries):  # call enumerate to index things
        print('- [{}] {}'.format(idx+1, entry))  # print in this format


def add_entries(data):
    text = input('Type your entry and press <enter>\n')  # tell them to input something, store in "text"
    journal.add_entry(text, data)  # call the journal.add_entry w/ the text and the journal data


main()
