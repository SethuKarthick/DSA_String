def longest_balanced_substring(string):
	
	max_length = 0
	
	opening_count = 0
	closing_count = 0 
	
	for char in string:
		if char == '(':
			opening_count += 1	
		else:
			closing_count += 1
			
		if opening_count == closing_count:
			max_length = max(max_length, closing_count*2)
		elif closing_count > opening_count:
			opening_count = 0
			closing_count = 0
			
	opening_count = 0
	closing_count = 0
			
	for i in reversed(range(len(string))):
		char = string[i]
			
		if char == '(':
			opening_count += 1
		else:
			closing_count += 1
				
		if opening_count == closing_count:
			max_length = max(max_length, opening_count*2)
		elif opening_count > closing_count:
			opening_count = 0
			closing_count = 0
			
	return max_length


longest_count = longest_balanced_substring(string='(()))(')
print(longest_count)