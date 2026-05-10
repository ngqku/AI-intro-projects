#1.VARIABLE DEFINITION
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
#2.Domain definition
colors=['Red','Green','Blue']
#3.constraints. Neighbors can not use the same color
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  [] 
}

def is_safe(state, color, assignment):
    for neighbor in neighbors[state]:
        # check if using the color breaks any constraints
        if neighbor in assignment and assignment[neighbor] == color:
            return False 
    
    return True 

def solve_map(index, assignment):
    # BASE CASE: If we have colored all 16 states, we are DONE!
    if len(assignment) == len(variables):
        return assignment

    
    current_state = variables[index]

    #try all colors
    for color in colors:
        # check if its safe to use the color
        if is_safe(current_state, color, assignment):
            
            # If safe, record it on the scoreboard
            assignment[current_state] = color

            # MOVE FORWARD: Call the function again for the NEXT state (index + 1)
            result = solve_map(index + 1, assignment)
            
            # If the next steps also worked, keep going!
            if result is not None:
                return result

            # BACKTRACK: If we hit a dead end, erase the last choice and try the next color
            del assignment[current_state]

    # If no colors work for this state, return none
    return None

solution = solve_map(0, {})
if solution:
    print("--- Australia Map Coloring Solution ---")
    for state, color in solution.items():
        print(f"{state}: {color}")
else:
    print("Solution is empty! Failed to color map")
    print("Try adding more colors")
