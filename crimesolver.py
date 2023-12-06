# Final Product
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
        if (i % 2 == 0) or (i % 3 == 0) or (i % 7 == 0):
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

# print(statements)
# Display the suspects and their statements
for statement in statements:
    print(statement)

# Print the list of suspects
# print("Suspects:", suspects)

def parse_logic(statements):
    truth_dict = {}  # Dictionary to store truth information

    for statement in statements:
        person, claim = statement.split(": ")
        name, assertion = person.strip(), claim.strip().replace('"', '')

        if "the thief" in assertion:
            subject = assertion.split("is the thief.")[0].strip()
            if assertion.endswith("is the thief."):
                truth_dict[name] = {"subject": subject, "isThief": True, "isNotThief": False, "t_count": 0}
            else:
                truth_dict[name] = {"isThief": False, "isNotThief": True, "t_count": 0}

    return truth_dict

relations = parse_logic(statements)
# print(relations)

def is_valid_solution(solution, relations):
    for suspect, accusation in solution.items():
        if accusation == suspect:  # A suspect cannot accuse themselves
            return False
        if relations[suspect]["isThief"] and accusation != relations[suspect]["subject"]:
            return False
        if not relations[suspect]["isThief"] and accusation == suspect:
            return False
    return True

def find_thief_backtrack(relations, solution, i):
    if i == len(solution):
        if is_valid_solution(solution, relations):
            return True
        return False
    
    for suspect in relations:
        solution[i] = suspect
        if is_valid_solution(solution, relations) and find_thief_backtrack(relations, solution, i + 1):
            return True
        solution[i] = None
    
    return False

def find_thief(relations):
    solution = [None] * len(relations)
    if find_thief_backtrack(relations, solution, 0):
        return [solution[i] for i in range(len(solution))]
    return None

suspect_names, suspect_statements = generate_statements(num_suspects)
suspect_relations = parse_logic(suspect_statements)
thief_solution = find_thief(suspect_relations)

if thief_solution:
    print("The thief is:")
    for i, thief in enumerate(thief_solution):
        print(f"Suspect {suspect_names[i]} accuses {thief}")
else:
    print("No single solution found.")
