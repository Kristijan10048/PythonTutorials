import csv
from typing import TextIO


def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num) -> None:
    print("Square: {}".format(num * num))


def list_to_csv_file():
    # field names
    fields = ['Name', 'Branch', 'Year', 'CGPA']

    # data rows of csv file
    rows = [['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]

    with open('GFG', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(fields)
    # write.writerows(rows)


def write_to_file():
    f: TextIO = open("", "a")
    f.write("Now the file has more content!")
    f.close()


def load_and_process_files(s_path: str):
    print('s_path' + s_path)
    all_files = glob.glob(s_path + '/**/*.*', recursive=True)

    if len(all_files) <= 0:
        log_info('No JPG files under {}'.format(s_path))
        return

    # init loop vars
    start_time = datetime.datetime.now()
    uniqFiles: Dict[object, str] = {}
    duplFiles = list()
    allFilesCnt = len(all_files)
    i = 0
    iProgressBarStep = int(round(allFilesCnt / 100))
    file_writer = open("AllFiles.txt", 'w', encoding="utf-8")
    for currFile in all_files:
        md_hash = calculate_file_md5(currFile)
        if md_hash in uniqFiles.keys():
            # print("Duplicate file: {} md5 {}".format(currFile, md_hash ))
            duplFiles.append(currFile)
            duplFiles.append(uniqFiles[md_hash])
        else:
            uniqFiles[md_hash] = currFile

        # console progress bar
        if i % iProgressBarStep == 0:
            percent = int(round((i / allFilesCnt) * 100, 0))
            log_info("Complete: {:d}%. Unique files: {:d}. Duplicates: {:d}".format(
                percent, len(uniqFiles), len(duplFiles)))

        # write to file
        file_writer.write(currFile + '\n')
        i = i + 1
    file_writer.close()

    duplFilesCnt = len(duplFiles)
    uniqFilesCnt = len(uniqFiles)

    th1 = threading.Thread(target=write_to_txt_file, args=('duplFiles.txt', duplFiles, None))
    th2 = threading.Thread(target=write_to_txt_file, args=('uniqFiles.txt', None, uniqFiles))
    th1.start()
    th2.start()

    end_time = datetime.datetime.now()
    exec_time = end_time - start_time

    log_info("Done Listing")
    log_info("Loaded {} files.".format(allFilesCnt))
    log_info("Unique files: {}".format(uniqFilesCnt))
    log_info("Duplicate files: {}".format(duplFilesCnt))
    log_info("Check: {}".format(allFilesCnt - (uniqFilesCnt + duplFilesCnt)))
    log_info("Run time: {} seconds".format(exec_time.total_seconds()))

    # t1.join()
    # t2.join()