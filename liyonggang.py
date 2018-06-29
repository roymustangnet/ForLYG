# coding:utf-8
from itertools import combinations
from itertools import product

def main():
	input_list1 = input("Input 1.1:")
	input_list2 = input("Input 1.2:")
	input_list3 = input("Input 1.3:")
	input_list4 = input("Input 1.4:")

	l1 = [int(i) for i in input_list1.split()]
	l2 = [int(i) for i in input_list2.split()]
	l3 = [int(i) for i in input_list3.split()]
	l4 = [int(i) for i in input_list4.split()]

	input_list1 = input("Input 2.1:")
	input_list2 = input("Input 2.2:")
	input_list3 = input("Input 2.3:")
	input_list4 = input("Input 2.4:")

	ll1 = [int(i) for i in input_list1.split()]
	ll2 = [int(i) for i in input_list2.split()]
	ll3 = [int(i) for i in input_list3.split()]
	ll4 = [int(i) for i in input_list4.split()]


	print("Please input flag(0, 1, 2)")
	print("flag = 0 means no condition")
	print("flag = 1 means there have only one neighbour in the list")
	print("flag = 2 means there don't have any neighbour in the list")
	flag = input("What do you want:")
	flag = int(flag)

	r1 = get_combinations(l1, l2, l3, l4)
	r2 = get_combinations(ll1, ll2, ll3, ll4);

	for i in intersection(r1, r2, flag):
		print(i)


def get_combinations(list1, list2, list3, list4):
	# the count of list4 is 14, so select 2 number for it
	r = list(product(list1, list2, list3, combinations(list4,2)))
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


if __name__ == '__main__':
	main()



