def lower_max(arr: list[int]):

	new_arr = sorted(set(arr))
	new_arr.pop()
	return new_arr

	


"""arr = [12, 34, 22, 56, 90, 12]

red_arr = lower_max(arr)

print(red_arr)"""

if __name__ == '__main__':
	lower_max()
