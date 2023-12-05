# suspects: a list containing the names of the suspects
# current_index: index of current suspect being checked
# statements: list containing statements each suspect made
# truth_count: counter of how many suspects are telling the truth
# thief: current assumed thief

def generate_statements(num_suspects):
    import random
    import names

    # Generate unique random names for suspects using a set
    unique_suspects = set()
    while len(unique_suspects) < num_suspects:
        name = names.get_first_name()
        unique_suspects.add(name)

    suspects = list(unique_suspects)  # Convert set to list for shuffling
    random.shuffle(suspects)

    # Create statements based on shuffled suspects
    statements = []
    for i in range(num_suspects):
        if i % 2 == 0:
            accusation = random.choice(suspects)
            while accusation == suspects[i]:  # Ensure a suspect doesn't accuse themselves
                accusation = random.choice(suspects)
            statement = f"{suspects[i]}: \"{accusation} is the thief.\""
        else:
            statement = f"{suspects[i]}: \"I'm not the thief.\""
        statements.append(statement)

    return suspects, statements

# Get user input for the number of suspects
num_suspects = int(input("Enter the number of suspects: "))

# Generate suspects and their statements
suspects, statements = generate_statements(num_suspects)

# Display the suspects and their statements
for statement in statements:
    print(statement)

# Print the list of suspects
print("Suspects:", suspects)

def find_thief(suspects, current_index, statements, truth_count, thief):
    # base case: when all suspects have been checked, see if conditions have been met to find thief
    if current_index == len(suspects):
        # potential solution if only 1 suspect is being truthful
        if truth_count == 1:
            return True, thief
        return False, None
    
    # Assume the current suspect is lying and calls find_thief for next suspect
    result = find_thief(suspects, current_index + 1, statements, truth_count, thief)
    if result[0]:
        return result
    
    # If assuming the current suspect as a liar didn't lead to a solution, consider them telling the truth
    truth_count += 1
    result = find_thief(suspects, current_index + 1, statements, truth_count, suspects[current_index])
    if result[0]:
        return result
    
    return False, None


solution = find_thief(suspects, 0, statements, 0, None)
if solution[0]:
    print(f"The thief is {solution[1]}")
else:
    print("No solution found")


# # Test scenario
# # suspects = ['A', 'B', 'C']
# # statements = [
# #     "I am not the thief",
# #     "A is the thief",
# #     "I am not the thief"
# # ]