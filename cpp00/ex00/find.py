array = [1, 2, 6, 3, 4, 5]
#find longest increasing subsequence

def find_longest_increasing_subsequence(array):
	dp = [1] * len(array)
	for inx, i in enumerate(array):
		if inx == 0:
			dp[inx] = 1
		else:
			if array[inx] - 1 == array[inx - 1]:
				dp[inx] = dp[inx - 1] + 1
			else:
				dp[inx] = 1
	#find the max value in dp and index
	print(dp)
	print(max(dp))
	print(dp.index(max(dp)))
	print(array[dp.index(max(dp)) - dp[dp.index(max(dp))] + 1:dp.index(max(dp)) + 1])

find_longest_increasing_subsequence(array)