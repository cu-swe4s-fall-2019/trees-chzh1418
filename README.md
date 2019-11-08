# Trees
Understanding the performance difference between hash tables and trees(binary tree and avl tree)
## Continuous Integration Status

## Required packages
* os
* sys
* argparse
* time
* importlib
* unittest
* pycodestyle

## Usage
The main program can benchmark the required time for insert and search different type of data structure.
To run the program use the following scripts:
```
python insert_key_value_paires.py --data_structure 'hash' --dataset rand.txt --key_value 10000
python insert_key_value_paires.py --data_structure 'binary_tree' --dataset rand.txt --key_value 10000
python insert_key_value_paires.py --data_structure 'avl_tree' --dataset rand.txt --key_value 10000
python insert_key_value_paires.py --data_structure 'hash' --dataset sorted.txt --key_value 10000
python insert_key_value_paires.py --data_structure 'binary_tree' --dataset sorted.txt --key_value 10000
python insert_key_value_paires.py --data_structure 'avl_tree' --dataset sorted.txt --key_value 10000
```
## Results

