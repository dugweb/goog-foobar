a = [22.2, 46, 100.8] 
b = [23, 11.1, 50.4]



def answer(a = [], b = []):

	results = {}

	for i in range(len(a)):
		for j in range(len(b)):
			improvement = shrunk(a[i], b[j])
			results[improvement] = results.get(improvement, 0) + 1

	#return results
	return max(results, key = results.get)


def shrunk(a, b):
	begin, final = a, b
	if a < b:
		begin, final = b, a

	return int(((float(begin) - float(final) ) / float(begin)) * 100)
	



print answer(a, b)
print answer([5, 76, 65, 654, 12, 98], [8.05, 122.36000000000001, 104.65, 1052.94, 19.32, 157.78])
print answer( [4565485, 54.76, 4.5565, 15654, 412, .98], [456548.5, 5.476, 0.45565, 1565.4, 41.2, 0.098]) # * .1
print answer( [4565485, 54.76, 4.5565, 15654, 412, .98], [5022033.5, 60.236000000000004, 5.01215, 17219.4, 453.20000000000005, 1.078]) # * 1.1
print answer([2.2999999999999998, 15.0, 102.40000000000001, 3486.8000000000002], [23.0, 150.0, 1024.0, 34868.0])

# print growth(90, 100)
# print growth(100, 75)
# print growth(100, 50)
# print growth(100, 90)
# print growth(100, 10)