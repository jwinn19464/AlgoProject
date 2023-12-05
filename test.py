# separate file to test methods
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

print(statements)
# Display the suspects and their statements
for statement in statements:
    print(statement)

# Print the list of suspects
print("Suspects:", suspects)

def parse_logic(statements):
    truth_dict = {}  # Dictionary to store truth information

    for statement in statements:
        person, claim = statement.split(": ")
        name, assertion = person.strip(), claim.strip().replace('"', '')

        if "the thief" in assertion:
            subject = assertion.split("is the thief.")[0].strip()
            if assertion.endswith("is the thief."):
                if name in truth_dict:
                    truth_dict[name]["isThief"] = True
                else:
                    truth_dict[name] = {"subject": subject, "isThief": True, "isNotThief": False}
            else:
                if name in truth_dict:
                    truth_dict[name]["isNotThief"] = True
                else:
                    truth_dict[name] = {"isThief": False, "isNotThief": True}

    return truth_dict

boolean_results = parse_logic(statements)
print(boolean_results)

# for result in boolean_results:
#     print(result)
    

# def create_truth_table(suspects, boolean_results):
#     isThief = False
#     isNotThief = True
#     truth_table = {suspect: None for suspect in suspects}
#     print(truth_table)

#     for boolean_statement in boolean_results:
#         name, statement = boolean_statement.split(": ")
#         print(name)
#         print(statement)
#         suspect = name.strip()
#         print("suspect: ", suspect)
# #         print("s:", statement)
#         if " == " in statement:
#             truth_value = statement.split(" == ")[1].strip(" '")
#             # print("t-val: ", truth_value)
#         # else:
#         #     truth_value = statement.split(" != ")[1].strip(" '")
#             # print("t-val: ", truth_value)
#         if truth_table[suspect] is None:
#             truth_table[suspect] = truth_value
#             print("t-table:", truth_table)
# #         # elif truth_table[suspect] != truth_value:
# #         #     truth_table[suspect] = False  # Inconsistency found, mark as False

#     return truth_table
# create_truth_table(suspects, boolean_results)
# def eliminate_inconsistencies(truth_table):
#     consistent_suspects = [suspect for suspect, value in truth_table.items() if value]

#     return consistent_suspects

# # Assuming only one person is telling the truth
# def identify_thief(suspects, statements):
#     boolean_results = parse_logic(statements)
#     truth_table = create_truth_table(suspects, boolean_results)
#     consistent_suspects = eliminate_inconsistencies(truth_table)

#     if len(consistent_suspects) == 1:
#         return consistent_suspects[0]
#     else:
#         return "No clear identification"  # More than one consistent suspect

# thief = identify_thief(suspects, statements)
# print(f"The thief is: {thief}")
