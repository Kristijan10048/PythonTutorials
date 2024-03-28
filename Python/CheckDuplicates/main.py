import datetime
import glob
import hashlib
import threading
import logging
from typing import Dict
import os
import argparse


# custom logger for this project
import dupl_logger as d_log


def get_file_size(file_path: str) -> float:
    """
    Returns file size in MB
    :param file_path: Path of the file to calculate file size
    :return:
    """
    file_stats = os.stat(file_path)
    # print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
    return round(file_stats.st_size / (1024 * 1024), 1)


def calculate_file_md5(file_path: str) -> str:
    try:
        with open(file_path, 'rb') as file_to_check:
            # read contents of the file
            data = file_to_check.read()
            # pipe contents of the file through
            return hashlib.md5(data).hexdigest()
    except Exception as e:
        d_log.log_error(str(e))
        d_log.log_error(file_path)


def write_to_txt_file(s_file_name: str, lst_data: list, dict_data: dict = None) -> None:
    try:
        f = open(s_file_name, 'w', encoding='utf-8', newline='\n')
        if dict_data is not None:
            for keyItem in dict_data.keys():
                f.write('{} md5: {} {} Mb'.format(dict_data[keyItem], keyItem, get_file_size(dict_data[keyItem])) + '\n')
        else:
            for lstItem in lst_data:
                f.write(lstItem + '\n')

        f.close()
        d_log.log_info("Done write to {}.".format(s_file_name))
    except Exception as e:
        d_log.log_error(str(e))


def load_and_process_files_threaded(s_path: str, s_file_ext: str, thread_id: int):
    print('s_path' + s_path)
    all_files = glob.glob(s_path + '/**/' + s_file_ext, recursive=True)

    i_files_cnt = len(all_files)
    if i_files_cnt <= 0:
        d_log.log_info('No files under {}'.format(s_path))
        return
    else:
        d_log.log_info('Loaded {:d} files'.format(i_files_cnt))

    # init loop vars
    start_time = datetime.datetime.now()
    uniqFiles: Dict[object, str] = {}
    duplFiles = list()
    allFilesCnt = len(all_files)
    i = 0
    iProgressBarStep = int(round(allFilesCnt / 100))

    # main log file
    processing_files_log = 'main-' + str(thread_id) + '.log'  # os.path.join(s_path,

    # open file writer
    file_writer = open(processing_files_log, 'w', encoding="utf-8")

    for currFile in all_files:
        md_hash = calculate_file_md5(currFile)
        if md_hash in uniqFiles.keys():
            # print("Duplicate file: {} md5 {}".format(currFile, md_hash ))
            duplFiles.append(currFile)
            duplFiles.append(uniqFiles[md_hash] + ' Duplicate')
        else:
            uniqFiles[md_hash] = currFile

        # console progress bar
        if i % iProgressBarStep == 0:
            percent = int(round((i / allFilesCnt) * 100, 0))
            d_log.log_info("THREAD {:d}: Complete: {:d}%. Unique files: {:d}. Duplicates: {:d}".format(
                thread_id, percent, len(uniqFiles), len(duplFiles)))
        elif i % 100 == 0:
            d_log.log_info('Processed {}/{} files.'.format(i, i_files_cnt))

        # write to file
        file_writer.write(currFile + '\n')
        i = i + 1
    file_writer.close()

    duplFilesCnt = len(duplFiles)
    uniqFilesCnt = len(uniqFiles)

    # threaded write to log files
    duplicates_files_log = os.path.join(s_path, 'duplicates-' + str(thread_id) + '.log')
    unique_files_log = os.path.join(s_path, 'unique-' + str(thread_id) + '.log')

    tt1 = threading.Thread(target=write_to_txt_file, args=(duplicates_files_log, duplFiles, None))
    tt2 = threading.Thread(target=write_to_txt_file, args=(unique_files_log, None, uniqFiles))

    tt1.start()
    tt2.start()

    tt1.join()
    tt2.join()

    end_time = datetime.datetime.now()
    exec_time = end_time - start_time

    d_log.log_info("THREAD {} : Done Listing".format(thread_id))
    d_log.log_info("THREAD {} : Loaded {} files.".format(thread_id, allFilesCnt))
    d_log.log_info("THREAD {} : Unique files: {}".format(thread_id, uniqFilesCnt))
    d_log.log_info("THREAD {} : Duplicate files: {}".format(thread_id, duplFilesCnt))
    d_log.log_info("THREAD {} : Check: {}".format(thread_id, allFilesCnt - (uniqFilesCnt + duplFilesCnt)))
    d_log.log_info("THREAD {} : Run time: {} seconds".format(thread_id, exec_time.total_seconds()))


if __name__ == "__main__":
    # script arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument('--path')
    argParser.add_argument('--threads')
    argParser.add_argument('--gen_html')
    args = argParser.parse_args()
    print(args.path)

    # configure logging
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

    my_path = r'Z:\kris\Photos'  # r'C:\Users\Kristijan\Desktop\Photos'
    if args.threads:

        t1 = threading.Thread(target=load_and_process_files_threaded, args=(my_path, '*.jpg', 1))
        t1.start()
        t2 = threading.Thread(target=load_and_process_files_threaded, args=(my_path, '*.mp4', 2))
        t2.start()

        # all done
        exit(0)
    elif args.gen_html:
        parse_html_gallery()
        exit(0)
    else:
        load_and_process_files_threaded(my_path, '*.*', 1)
        exit(0)
