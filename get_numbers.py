import time
import urllib.request

# Note that these sizes are optimized for rgb values
def request(number, min_val=0, max_val=255):
	if min_val > max_val:
		min_val = max_val

	# The max numbers that can be requested at once is 10000, this loop makes
	# my algorithm capable of exceeding that limit
	numbers = []
	max_numbers = 10000
	for i in range(int(number/max_numbers) + 1):
		requested_numbers = number
		if number - max_numbers > 0:
			number -= max_numbers
			requested_numbers = max_numbers
		url = 'https://www.random.org/integers/?num=%d&min=%d&max=%d&col=1&base=10&format=plain&rnd=new' % (requested_numbers, min_val, max_val)
		resp = urllib.request.urlopen(url)

		# We do this in multiple steps because the reponse contains a return at the end
		nums = resp.read().decode('utf-8').split('\n')
		nums.pop()
		numbers.extend(map(int, nums))

		print('Downloading Numbers: %d / %d' % (len(numbers), number))

		# random.org has asked for a large timeout between requests, they don't specify what "large" is
		# but 5 seconds seems huge, so I'm hoping that counts
		if i < int(number/max_numbers):
			time.sleep(5)
	return numbers
