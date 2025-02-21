import datetime
import glob
import hashlib
import threading
import logging
from typing import Dict
import os
import argparse
import json

def get_file_size(file_path: str) -> float:
    """
    Returns file size in MB
    :param file_path: Path of the file to calculate file size
    :return:
    """
    file_stats = os.stat(file_path)
    # print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}') (1024 * 1024)
    return round(file_stats.st_size, 1)


def calculate_file_md5(file_path: str) -> str:
    try:
        with open(file_path, 'rb') as file_to_check:
            # read contents of the file
            data = file_to_check.read()
            # pipe contents of the file through
            return hashlib.md5(data).hexdigest()
    except Exception as e:
        print(str(e))
        return ""


def write_to_txt_file(s_file_name: str, lst_data) -> None:
    try:
        f = open(s_file_name, 'w', encoding='utf-8', newline='\n')
        if lst_data is not None:
            f.write(json.dumps(lst_data,indent=4))
        f.close()
    except Exception as e:
        print(str(e))


def load_and_process_files(s_path: str, s_file_ext: str = ""):
    start_time = datetime.datetime.now()
    print('s_path' + s_path)
    all_files = glob.glob(s_path + '/**', recursive=True, include_hidden=True)

    i_files_cnt = len(all_files)
    if i_files_cnt <= 0:
        print('No files under {}'.format(s_path))
        return
    else:
        print('Loaded {:d} files'.format(i_files_cnt))

    # init loop vars
    file_info = {}
    lt_files = list()
    i = 0
    iProgressBarStep = int(round(i_files_cnt / 100))

    for curr_file in all_files:
        if os.path.isfile(curr_file):
            md_hash = calculate_file_md5(curr_file)
            dt_curr_file_info = {'path': curr_file, 'md5':  md_hash ,'size':get_file_size(curr_file) }
            lt_files.append(dt_curr_file_info)

            # console progress bar
            if i % iProgressBarStep == 0:
                percent = int(round((i / i_files_cnt) * 100, 0))
                print("Complete: {:d}%".format(percent))
            elif i % 100 == 0:
                print('Processed {}/{} files.'.format(i, i_files_cnt))

        i = i + 1

    end_time = datetime.datetime.now()
    exec_time = end_time - start_time
    print(f'Execution time: {exec_time}')
    write_to_txt_file('test.json', lt_files)


if __name__ == "__main__":
    # script arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument('--path')
    args = argParser.parse_args()
    print(args.path)

    if args.path:
        load_and_process_files(args.path)
        # all done
        exit(0)
    else:
        exit(0)
