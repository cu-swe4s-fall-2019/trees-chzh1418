import sys
import os
import time
import argparse
import importlib
import binary_tree
sys.path.append('hash-tables-chzh1418')
sys.path.append('avl_tree')
hash_functions = importlib.import_module('hash-tables-chzh1418.hash_functions')
hash_tables = importlib.import_module('hash-tables-chzh1418.hash_tables')
avl_tree = importlib.import_module('avl_tree.avl')


def parse_args():
    parser = argparse.ArgumentParser(description='Pass parameters')
    parser.add_argument('--data_structure',
                        type=str,
                        help="Specify data structure",
                        required=True)
    parser.add_argument('--dataset',
                        type=str,
                        help='Specify dataset to use',
                        required=True)
    parser.add_argument('--key_value',
                        type=int,
                        help='Number of key value pairs to use',
                        required=True)
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


def hash_time(keys):
    """
    Time to insert, search keys
    Arguments
    --------
    keys: keys to insert to hash table

    Return
    --------
    insert_time: time took to insert
    search_time: time took to search
    search_nonexist_time: time took to search nonexiting keys
    """
    # Hash table and hash functions to use and initiate hash table
    hash_table = hash_tables.ChainedHash(100000,
                                         hash_functions.h_rolling)
    # Insert keys
    insert_start = time.time()
    for key in keys:
        hash_table.add(key, key + '_value')
    insert_end = time.time()

    # Search exiting keys
    search_start = time.time()
    for key in keys:
        hash_table.search(key)
    search_end = time.time()

    # Search non-existing keys
    search_nonexist_start = time.time()
    for key in keys:
        hash_table.search(key + 'Nonexiting')
    search_nonexist_end = time.time()

    insert_time = insert_end - insert_start
    search_time = search_end - search_start
    search_nonexist_time = search_nonexist_end - search_nonexist_start

    return insert_time, search_time, search_nonexist_time


def binary_tree_time(keys):
    """
    Time to insert, search keys
    Arguments
    --------
    keys: keys to insert to binary tree

    Return
    --------
    insert_time: time took to insert
    search_time: time took to search
    search_nonexist_time: time took to search nonexiting keys
    """
    # Initiate binary tree
    bt = binary_tree.BinaryTree()
    # Insert keys
    insert_start = time.time()
    for key in keys:
        bt.insert(key, key + '_value')
    insert_end = time.time()

    # Search exiting keys
    search_start = time.time()
    for key in keys:
        bt.search(key)
    search_end = time.time()

    # Search non-existing keys
    search_nonexist_start = time.time()
    for key in keys:
        bt.search(key + 'Nonexiting')
    search_nonexist_end = time.time()

    insert_time = insert_end - insert_start
    search_time = search_end - search_start
    search_nonexist_time = search_nonexist_end - search_nonexist_start

    return insert_time, search_time, search_nonexist_time


def avl_tree_time(keys):
    """
    Time to insert, search keys
    Arguments
    --------
    keys: keys to insert to avl tree

    Return
    --------
    insert_time: time took to insert
    search_time: time took to search
    search_nonexist_time: time took to search nonexiting keys
    """
    # Initiate AVL tree
    at = avl_tree.AVL()
    # Insert keys
    insert_start = time.time()
    for key in keys:
        at.insert(key)
    insert_end = time.time()

    # Search exiting keys
    search_start = time.time()
    for key in keys:
        at.find(key)
    search_end = time.time()

    # Search non-existing keys
    search_nonexist_start = time.time()
    for key in keys:
        at.find(key + 'Nonexiting')
    search_nonexist_end = time.time()

    insert_time = insert_end - insert_start
    search_time = search_end - search_start
    search_nonexist_time = search_nonexist_end - search_nonexist_start

    return insert_time, search_time, search_nonexist_time


if __name__ == '__main__':
    # Get arguments from argparse
    args = parse_args()
    if not os.path.exists(args.dataset):
        print('Data file not found')
        sys.exit(1)
    if args.key_value > 10000 or args.key_value < 100:
        print('Number of key value too large or too small')
        sys.exit(1)
    keys = data_keys(args.dataset, args.key_value)
    if args.data_structure == 'hash':
        insert_time, search_time, search_nonexist_time = hash_time(keys)
        print(insert_time, search_time, search_nonexist_time)
    elif args.data_structure == 'binary_tree':
        insert_time, search_time, search_nonexist_time = binary_tree_time(keys)
        print(insert_time, search_time, search_nonexist_time)
    elif args.data_structure == 'avl_tree':
        insert_time, search_time, search_nonexist_time = avl_tree_time(keys)
        print(insert_time, search_time, search_nonexist_time)
    else:
        print('Data structure not supported')
        sys.exit(1)
