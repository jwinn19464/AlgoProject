def find_possible_thieves():
    suspects = ['A', 'B', 'C', 'D']
    possible_thieves = []

    for thief in suspects:
        statements = {
            'A': (thief == 'B'),
            'B': (thief != 'B'),
            'C': (thief == 'D'),
            'D': (thief == 'C')
        }

        truthful_suspects = [suspect for suspect in statements if statements[suspect]]

        if len(truthful_suspects) == 1:
            possible_thieves.append(truthful_suspects[0])

    return possible_thieves

thieves = find_possible_thieves()
if thieves:
    print("Possible thief(s):", thieves)
else:
    print("No unique solution found.")
