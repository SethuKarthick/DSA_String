# def longestBalancedSubstring(string):
#     # Write your code here.
# 	_dict = {  '[': ']', '(':')', '{':'}'  }
# 	open_dict = {}
# 	close_dict = {}
	
# 	for char in string:
# 		if char in _dict.keys():
# 			open_dict[char] = open_dict.get(char, 0) + 1
# 		elif char in dict.values():
# 			close_dict[char] = close_dict.get(char, 0) + 1
			
# 	longest_balanced = get_max_balanced_substring(_dict, open_dict, close_dict)
	
# 	return open_dict[longest_balanced[0]]+close_dict[longest_balanced[0]]
			
		
		
			
# def get_max_balanced_substring(_dict, open_dict, close_dict):
# 	longest_balanced = [0, 1]
	
# 	for idx, char in enumerate(open_dict):
# 		if open_dict[char] == close_dict[_dict[char]]:
# 			longest_balanced = max([idx, open_dict[char]], longest_balanced)
			
			
# 	return longest_balanced






def longestBalancedSubstring(string):
    # Write your code here.
	
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


valid_count = longestBalancedSubstring(string='(()))(')
print(valid_count)
			
			
				