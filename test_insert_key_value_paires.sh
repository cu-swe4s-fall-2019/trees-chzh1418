test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run codestyle binary_tree.py
assert_no_stdout
run codestyle insert_key_value_paires.py
assert_no_stdout
run codestyle test_binary_tree.py
assert_no_stdout

run input_error python insert_key_value_paires.py --data_structure 'btree' --dataset rand.txt --key_value 10000
assert_exit_code 1
run input_error python insert_key_value_paires.py --data_structure 'hash' --dataset random.txt --key_value 10000
assert_exit_code 1
run input_error python insert_key_value_paires.py --data_structure 'hash' --dataset rand.txt --key_value 1

run test_hash python insert_key_value_paires.py --data_structure 'hash' --dataset rand.txt --key_value 10000
assert_exit_code 0
assert_stdout

run test_binary python insert_key_value_paires.py --data_structure 'binary_tree' --dataset rand.txt --key_value 10000
assert_exit_code 0
assert_stdout

run test_val python insert_key_value_paires.py --data_structure 'avl_tree' --dataset rand.txt --key_value 10000
assert_exit_code 0
assert_stdout

run test_hash python insert_key_value_paires.py --data_structure 'hash' --dataset sorted.txt --key_value 10000
assert_exit_code 0
assert_stdout

run test_binary python insert_key_value_paires.py --data_structure 'binary_tree' --dataset sorted.txt --key_value 10000
assert_exit_code 0
assert_stdout

run test_val python insert_key_value_paires.py --data_structure 'avl_tree' --dataset sorted.txt --key_value 10000
assert_exit_code 0
assert_stdout