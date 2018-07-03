# coding:utf-8
from itertools import combinations
from itertools import product
import csv
def main():
	result = user_input()
	if(result and len(result) == 3):
		r1 = get_combinations(result[0])
		r2 = get_combinations(result[1]);
		intersection_set = intersection(r1, r2, result[2])
		if not intersection_set:
			print("The result is empty.")
			return
		for i in intersection_set:
			print(i)
		write_csv(intersection_set)
	else:
		print("There are something wrong with input. Please check them.")


def user_input():
	# list1 = user_input_for_group(1)
	list1 = [
		[4, 11, 14, 15, 22, 27, 35],
		[2, 8, 10, 16, 21, 31, 33],
		[5, 13, 17, 19, 23, 24, 25],
		[1, 3, 6, 7, 9, 12, 18, 20, 28, 29, 30, 32, 34, 26]
	]
	if not check_inputs(list1):
		return False
	list2 = [
		[3, 10, 12, 32, 5, 18, 25],
		[28, 29, 31, 1, 2, 23, 35],
		[4, 9, 19, 21, 27, 30, 11],
		[6, 7, 8, 13, 14, 15, 16, 17, 20, 22, 24, 26, 33, 34]
	]
	# list2 = user_input_for_group(2)
	if not check_inputs(list2):
		return False
	# list1 = [
	# 	[i for i in range(1, 8)],
	# 	[i for i in range(8, 15)],
	# 	[i for i in range(15, 22)],
	# 	[i for i in range(22, 35)],
	# ]
	# list2 = [
	# 	[i for i in range(1, 15, 2)],
	# 	[i for i in range(2, 15, 2)],
	# 	[i for i in range(15, 22)],
	# 	[i for i in range(22, 35)],
	# ]
	print("Please input flag:")
	print("flag = 0 means no condition")
	print("flag = 1 means there have only one neighbour in the list")
	print("flag = 2 means there don't have any neighbour in the list")
	flag = input("What do you want(0,1,2):")
	flag = int(flag)
	if not (flag in [0, 1, 2]):
		print("flag must be 0, 1 or 2")
		return False

	return (list1, list2, flag)

def user_input_for_group(group):
	# process user input for each group
	# there are two group
	input_lists = []
	for i in range(1,5):
		user_input = input(f"Input {group}.{i}:")
		input_list = [int(integer) for integer in user_input.split()]
		length = len(input_list)
		if((length == 7 and i < 4) or (length == 14 and i == 4)):
			input_lists.append(input_list)
		else:
			print("The length of input is not right.")
			return None
	return input_lists

def get_combinations(l):
	# the count of list4 is 14, so select 2 number for it
	r = list(product(l[0], l[1], l[2], combinations(l[3],2)))
	r1 = [ {*item[:3], *item[-1]} for item in r ]
	return r1


def intersection(comb1, comb2, flag = 0):
	# 求comb1和comb2的交集
	# flag = 0 表示不附带任何条件
	# flag = 1 表示每组数字中有且仅有一个相邻数字
	# flag = 2 表示每组数字中没有任何相邻数字
	intersection_set = set(map(tuple, comb1)) & set(map(tuple, comb2))
	if flag == 0:
		return intersection_set
	elif flag == 1:
		intersection_set = set([item for item in intersection_set if neighbour_count(item) == 1])
	elif flag == 2:
		intersection_set = set([item for item in intersection_set if neighbour_count(item) == 0])


def neighbour_count(input_list):
	# 一个数组中有多少个数字是相邻的
	# 例如：
	# [9,1,3,4,10] 相邻数为2，因为3和4相邻，9和10相邻
	input_list = list(input_list)
	input_list.sort()
	is_no_neighbour = True
	last = -1
	count = 0
	for current in input_list:
		if(last and current - last == 1):
			count += 1
		last = current
	return count

def check_inputs(input_lists):
	# 检查输入，判断是否所有的输入是否都包含了1-35
	if(not input_lists):
		return False
	standard_list = [i for i in range(1,36)]
	test_list = []
	[test_list.extend(i) for i in input_lists]
	for i in test_list:
		try:
			standard_list.remove(i)
		except Exception as e:
			print(f"There have more {i}.")
			return False
	if(standard_list):
		print(standard_list)
		return False
	return True
def write_csv(data):
	with open('result.csv', 'w') as f:
	    writer = csv.writer(f)
	    writer.writerows(data)
if __name__ == '__main__':
	main()
