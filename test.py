# separate file to test methods before adding to final product
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

def find_thief(relations, thief):
    t_count = {suspect: 0 for suspect in relations}  # Initialize count for each suspect

    for suspect, info in relations.items():
        for other_suspect, other_info in relations.items():
            if suspect != thief:
                # If the suspect accuses the thief and is telling the truth
                if other_info.get("isThief", False) and other_info.get("subject") == suspect:
                    t_count[suspect] += 1
                # If the suspect denies being the thief and is telling the truth
                elif other_info.get("isNotThief", False) and other_suspect != suspect:
                    t_count[suspect] += 1

    # Find the suspect with the maximum true statements
    max_true_statements = max(t_count.values())
    possible_thieves = [suspect for suspect, count in t_count.items() if count == max_true_statements]

    if len(possible_thieves) == 1:
        return possible_thieves[0]
    else:
        return None  # More than one suspect might be the thief

for suspect in suspects:
    # assume current suspect is the thief
    thief = find_thief(relations, suspect)
    if thief:
        print(f"The thief is: {thief}")
        break
