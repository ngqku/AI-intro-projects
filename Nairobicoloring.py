#1.VARIABLE DEFINITION
variables = [
    "Westlands",
    "Dagoretti North",
    "Dagoretti South",
    "Lang'ata",
    "Kibra",
    "Roysambu",
    "Kasarani",
    "Ruaraka",
    "Embakasi South",
    "Embakasi North",
    "Embakasi Central",
    "Embakasi East",
    "Embakasi West",
    "Makadara",
    "Kamukunji",
    "Starehe",
    "Mathare"]
#2.Domain definition
colors=['Red','Green','Blue','Yellow']
#3.Constraints, no neighbors with the same color
neighbors = {
    "Westlands": ["Dagoretti North", "Roysambu", "Starehe", "Mathare"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Lang'ata", "Kibra", "Starehe"],
    "Dagoretti South": ["Dagoretti North", "Lang'ata", "Kibra"],
    "Lang'ata": ["Dagoretti North", "Dagoretti South", "Kibra", "Makadara", "Starehe"],
    "Kibra": ["Dagoretti North", "Dagoretti South", "Lang'ata", "Makadara"],
    "Roysambu": ["Westlands", "Kasarani", "Ruaraka", "Starehe", "Mathare"],
    "Kasarani": ["Roysambu", "Ruaraka", "Embakasi North", "Embakasi Central"],
    "Ruaraka": ["Roysambu", "Kasarani", "Mathare", "Embakasi North"],
    "Embakasi South": ["Embakasi East", "Embakasi Central", "Makadara", "Starehe"],
    "Embakasi North": ["Kasarani", "Ruaraka", "Embakasi Central", "Embakasi East"],
    "Embakasi Central": ["Kasarani", "Embakasi North", "Embakasi East", "Embakasi South", "Makadara"],
    "Embakasi East": ["Embakasi North", "Embakasi Central", "Embakasi South", "Kamukunji"],
    "Embakasi West": ["Makadara", "Kamukunji", "Starehe"],
    "Makadara": ["Lang'ata", "Kibra", "Embakasi South", "Embakasi Central", "Embakasi West", "Kamukunji", "Starehe"],
    "Kamukunji": ["Embakasi East", "Embakasi West", "Makadara", "Starehe"],
    "Starehe": ["Westlands", "Dagoretti North", "Lang'ata", "Roysambu", "Embakasi South", "Embakasi West", "Makadara", "Kamukunji", "Mathare"],
    "Mathare": ["Westlands", "Roysambu", "Ruaraka", "Starehe"]
}


def is_safe(state, color, assignment):
    for neighbor in neighbors[state]:
        # check if using the color breaks constraint
        if neighbor in assignment and assignment[neighbor] == color:
            return False 
    
    return True 

def solve_map(index, assignment):
    # BASE CASE: If we have colored all 16 states, we are DONE!
    if len(assignment) == len(variables):
        return assignment

    
    current_state = variables[index]

    # Try all the colors
    for color in colors:
        # check if its safe to use the color
        if is_safe(current_state, color, assignment):
            
            # If safe, record it on the scoreboard
            assignment[current_state] = color

            # MOVE FORWARD: Call the function again for the NEXT state (index + 1)
            result = solve_map(index + 1, assignment)
            
            # If the next steps also worked, keep going!
            if result:
                return result

            # BACKTRACK: If we hit a dead end, erase the last choice and try the next color
            del assignment[current_state]
    # If no colors work for this state return none
    return None

solution = solve_map(0, {})
if solution:
    print("--- Nairobi Map Coloring Solution ---")
    for state, color in solution.items():
        print(f"{state}: {color}")
    
else:
    print(f"No solution found with {len(colors)} colors")
    print("Try adding more colors")