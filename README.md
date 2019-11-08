# Trees
Understanding the performance difference between hash tables and trees(binary tree and avl tree)
## Continuous Integration Status
[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/trees-chzh1418.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/trees-chzh1418)
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
To run plot_figures.py
```
python plot_figures.py --dataset rand.txt --key_value 2000
python plot_figures.py --dataset sorted.txt --key_value 2000
```

## Results
For radom keys
![](rand.txt_Insert_time.png)
![](rand.txt_Search_time.png)
![](rand.txt_Search_nonexist_time.png)

For sorted keys
![](sorted.txt_Insert_time.png)
![](sorted.txt_Search_time.png)
![](sorted.txt_Search_nonexist_time.png)
