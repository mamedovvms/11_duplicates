import os


def compare_files(filename, filedirs):
    list_duplicates = []
    path_file = os.path.join(filedirs[-1], filename)
    size_file = os.path.getsize(path_file)
    for dir in filedirs[:-1]:
        path_file2 = os.path.join(dir, filename)
        if os.path.getsize(path_file2) == size_file:
            list_duplicates.append((os.path.join(path_file), path_file2))
    return list_duplicates


def get_duplicates_files(directory):
    dict_files = {}
    list_duplicates = []
    for d, dirs, files in os.walk(directory):
        for f in files:
            if f in dict_files:
                file_dirs = dict_files[f]
                file_dirs.append(d)
                list_duplicates += compare_files(f, file_dirs)
            else:
                dict_files[f] = [d]
    return list_duplicates


if __name__ == '__main__':
    directory = input('Input directory: ')
    for f1, f2 in get_duplicates_files(directory):
        print(f1, f2)
