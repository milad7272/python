def reverse_v1 (s) :
	r = ''
	for char in s:
		r = char + r
	return r
#milad
input_str = input("insert your string: ")
reverse = reverse_v1(input_str)
print reverse
