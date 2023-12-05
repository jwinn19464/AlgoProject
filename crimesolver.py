def find_thief(suspects, current_index, statements, truth_count, thief):
    if current_index == len(suspects):
        if truth_count == 1:
            return True, thief
        return False, None
    
    # Assume the current suspect is lying
    result = find_thief(suspects, current_index + 1, statements, truth_count, thief)
    if result[0]:
        return result
    
    # If assuming the current suspect as a liar didn't lead to a solution, consider them telling the truth
    truth_count += 1
    result = find_thief(suspects, current_index + 1, statements, truth_count, suspects[current_index])
    if result[0]:
        return result
    
    return False, None

# Test scenario
suspects = ['A', 'B', 'C']
statements = [
    "I am not the thief",
    "A is the thief",
    "I am not the thief"
]

solution = find_thief(suspects, 0, statements, 0, None)
if solution[0]:
    print(f"The thief is {solution[1]}")
else:
    print("No solution found")
