import sys
import os
import time
import argparse
import importlib
import binary_tree
import numpy as np
import matplotlib.pyplot as plt
import insert_key_value_paires as ikvp
sys.path.append('hash-tables-chzh1418')
sys.path.append('avl_tree')
hash_functions = importlib.import_module('hash-tables-chzh1418.hash_functions')
hash_tables = importlib.import_module('hash-tables-chzh1418.hash_tables')
avl_tree = importlib.import_module('avl_tree.avl')
hash_time = ikvp.hash_time
binary_tree_time = ikvp.binary_tree_time
avl_tree_time = ikvp.avl_tree_time


def parse_args():
    parser = argparse.ArgumentParser(description='Pass parameters')
    parser.add_argument('--data_structure',
                        type=str,
                        help="Specify data structure",
                        required=False)
    parser.add_argument('--dataset',
                        type=str,
                        help='Specify dataset to use',
                        required=True)
    parser.add_argument('--key_value',
                        type=int,
                        help='Number of key value pairs to use',
                        required=False)
    return parser.parse_args()


def data_keys(data, number_of_keys):
    """
    To get the data file and specify how many key value pairs to use
    Arguments
    --------
    data: data file to use
    number_of_keys: number of key value pairs
    Return
    --------
    keys
    """
    count = 1
    keys = []
    for line in open(data):
        if count <= number_of_keys:
            keys.append(line)
            count += 1
    return keys


if __name__ == '__main__':
    # Get arguments from argparse
    args = parse_args()
    if not os.path.exists(args.dataset):
        print('Data file not found')
        sys.exit(1)
    if args.key_value > 10000 or args.key_value < 0:
        print('Number of key value too large or too small')
        sys.exit(1)
    keys = data_keys(args.dataset, args.key_value)
    insert_time_np = np.empty([3, args.key_value])
    search_time_np = np.empty([3, args.key_value])
    search_nonexist_time_np = np.empty([3, args.key_value])
    for i in range(len(keys)):
        insert_time, search_time, search_nonexist_time = hash_time(keys[:i])
        insert_time_np[0, i] = insert_time
        search_time_np[0, i] = search_time
        search_nonexist_time_np[0, i] = search_nonexist_time
        insert_time, search_time, search_nonexist_time = \
            binary_tree_time(keys[:i])
        insert_time_np[1, i] = insert_time
        search_time_np[1, i] = search_time
        search_nonexist_time_np[1, i] = search_nonexist_time
        insert_time, search_time, search_nonexist_time = \
            avl_tree_time(keys[:i])
        insert_time_np[2, i] = insert_time
        search_time_np[2, i] = search_time
        search_nonexist_time_np[2, i] = search_nonexist_time
    fig = plt.figure()
    plt.scatter(range(0, args.key_value), insert_time_np[0],
                label="Hash_Table")
    plt.scatter(range(0, args.key_value), insert_time_np[1],
                label="Binary Tree")
    plt.scatter(range(0, args.key_value), insert_time_np[2],
                label="Avl Tree")
    plt.title(args.dataset + "_Insert Time Comparison")
    plt.xlabel('Number of Keys')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig(args.dataset + '_Insert_time.png', bbox_inches="tight")

    fig = plt.figure()
    plt.scatter(range(0, args.key_value), search_time_np[0],
                label="Hash_Table")
    plt.scatter(range(0, args.key_value), search_time_np[1],
                label="Binary Tree")
    plt.scatter(range(0, args.key_value), search_time_np[2],
                label="Avl Tree")
    plt.title(args.dataset + "_Search Time Comparison")
    plt.xlabel('Number of Keys')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig(args.dataset + '_Search_time.png', bbox_inches="tight")

    fig = plt.figure()
    plt.scatter(range(0, args.key_value), search_nonexist_time_np[0],
                label="Hash_Table")
    plt.scatter(range(0, args.key_value), search_nonexist_time_np[1],
                label="Binary Tree")
    plt.scatter(range(0, args.key_value), search_nonexist_time_np[2],
                label="Avl Tree")
    plt.title(args.dataset + "_Search Nonexist Time Comparison")
    plt.xlabel('Number of Keys')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig(args.dataset + '_Search_nonexist_time.png',
                bbox_inches="tight")
