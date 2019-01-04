import os  # import the os module
import cat_service  # import cat_service module


def main():
    header() # call header func
    folder = get_folder()  # store return from get_folder func in 'folder'
    download_cats(folder)  # call download_cats(pass folder)


def header():
    print('*' * 30)
    print('       LOLCAT FACTORY')
    print('*' * 30)


def get_folder():
    print('Running get folder')
    base_dir = os.path.dirname(__file__)  # I think this is getting the directory from which this module is running
    print('Base_dir is: ' + base_dir)
    folder = "cat_pictures"  # Save the name of the folder
    full_path = os.path.join(base_dir, folder)  # I think this is joining the basedir and folder into a file path
    print('Full_path is :' + full_path)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):  # check if full path exists or if its actually a directory
        print('Creating dir {}'.format(full_path))
        os.mkdir(full_path)

    return full_path  # return the full path


def download_cats(folder):
    print('Contacting cat server')
    cat_count = 8
    for i in range(1, cat_count+1):
        name = "lolcat {}".format(i)  # name the lolcat file
        print('Getting cat {}'.format(name))
        cat_service.get_cat(folder, name)  # call get_cat(pass folder and name)


if __name__ == '__main__':
    main()
