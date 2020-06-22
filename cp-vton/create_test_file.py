import random

test_pairs = open('./data/test_pairs.txt')
test_pairs = test_pairs.read()

test_pairs = test_pairs.replace('\n', ' ')
test_pairs = test_pairs.split(' ')
new_pairs = test_pairs[:200]
people_list = [x for x in new_pairs if '_1' not in x]

cloth_list = [x.replace('_0', '_1') for x in people_list]
random.shuffle(cloth_list)

new_test = open('./data_2000/test_pairs.txt', 'w')

for i, x in enumerate(people_list):
    new_test.write(people_list[i] + ' ' +  cloth_list[i] + '\n')