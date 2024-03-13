from traits.app import sum

def test_simple():
	"""
	Assert the sum of 1 and 1 gives 2
	"""
	a = 1

	result = sum(a, a)

	assert 2 == result, "Not the sum I expected"

def test_simpler():
	"""
	Assert the sum of 0 and 1 gives 1
	"""
	a = 0
	b = 1

	result = sum(a, b)

	assert 1 == result, "Not the sum I expected"
