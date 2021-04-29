import sys
import getopt
import shutil
import os

def find_file_with_prefix_and_extend(path, prefix, extend):
    return [_ for _ in os.listdir(path) if _.startswith(prefix) and  _.endswith(extend)]

def get_file_prefix_time(file):
    try: 
        return file.split('_')[1]
    except:
        return "-1"

def move_file_to_folder(file_path, folder_path, mode):
    # create folder if not exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    dst_file_path = os.path.join(folder_path, os.path.basename(file_path))
    # move file to folder path
    if not os.path.exists(dst_file_path):
        if mode == "copy":
            shutil.copy(file_path, folder_path)
        elif mode == "move":
            shutil.move(file_path, folder_path)
            
        print("{} file '{}' to folder '{}'.".format(mode, os.path.basename(file_path), folder_path))
        return 1
    else:
        print("File '{}' already existed.".format(dst_file_path))
        return 0
        

def file_classifier_with_date_prefix(path, prefix, extend, mode):
    # get file with selected prefix and file extend in the path
    files = find_file_with_prefix_and_extend(path, prefix, extend)
    print("\nFind {} files with prefix '{}' and extend '{}' in '{}'.\n".format(len(files), prefix, extend, path))

    moved_file_count = 0
    not_moved_file_count = 0

    for file in files:
        # get file prefix date
        file_date = get_file_prefix_time(file)
        file_path = os.path.join(path, file)
        folder_path = os.path.join(path, file_date)
        if file_date == "-1":
            not_moved_file_count+=1
            print("Failed to parsing date at file '{}'.".format(file_path))
            continue

        # move file
        if move_file_to_folder(file_path, folder_path, mode) == 1:
            moved_file_count+=1
        else:
            not_moved_file_count+=1
    print("\nSuccessfully {} {} files and {} files Not {}.".format(mode, moved_file_count, not_moved_file_count, mode))

def main(argv):
    path = os.getcwd()
    file_prefix = ''
    file_extend = 'jpg'
    mode = "copy"

    try:
        opts, args = getopt.getopt(argv, "hd:p:e:m:", ["help", "dir=", "prefix=", "extend=", "mode="])
    except getopt.GetoptError:
        print('python file_classification.py -d <directory> -p <file prefix> -e <file extend> -m <copy or move>')
        sys.exit(2)

    for (opt, arg) in opts:
        if opt == "-h":
            print('python file_classification.py -d <directory> -p <file prefix> -e <file extend> -m <copy or move>')
            sys.exit()
        elif opt in ('-d', '--dir'):
            path = arg
        elif opt in ('-p', '--prefix'):
            file_prefix = arg
        elif opt in ('-e', '--extend'):
            file_extend = arg
        elif opt in ('-m', '--mode'):
            if arg == "copy" or arg == "move":
                mode = arg
            else:
                print('python file_classification.py -d <directory> -p <file prefix> -e <file extend> -m <copy or move>')
                sys.exit(2)

    file_classifier_with_date_prefix(path, file_prefix, file_extend, mode)

if __name__ == "__main__":
    main(sys.argv[1:])