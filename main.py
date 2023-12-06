# different approaches taken
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

# Display the suspects and their statements
for statement in statements:
    print(statement)

# Print the list of suspects
print("Suspects:", suspects)

def parse_logic(statements):
    boolean_statements = []
    
    for statement in statements:
        person, claim = statement.split(": ")
        name, assertion = person.strip(), claim.strip().replace('"', '')
        
        if "the thief" in assertion:
            subject = assertion.split("is the thief.")[0].strip()
            # print(subject)
            # print(assertion)
            # print(assertion.endswith("is the thief."))
            if assertion.endswith("is the thief."):
                boolean_statement = f"{name}: thief == '{subject}'"
            else:
                boolean_statement = f"{name}: thief != '{name}'"
            boolean_statements.append(boolean_statement)
    
    return boolean_statements

boolean_results = parse_logic(statements)

for result in boolean_results:
    print(result)
    
