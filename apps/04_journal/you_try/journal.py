import os


def load(name):
    data = []  # make an empty list
    filename = get_full_path(name)  # var containing the output of get_full_path(name)
    if os.path.exists(filename):  # check if this file already exists
        with open(filename) as fin:  # open the filename using abso path, as "fin"
            for entry in fin.readlines():  # go over file line for line
                data.append(entry.rstrip())  # append each entry to the list, strip end whitespace

    return data  # return the list whether empty or full


def save(name, journal_data):
    filename = get_full_path(name)

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_path(name):
    return os.path.abspath(os.path.join('.', 'Journals', name + '.jrl'))
    #  get the absolute file path from the relative path


def add_entry(text, journal_data):
    journal_data.append(text)  # append the text entry to the journal_data list


