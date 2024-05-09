colors = ['red','blue','green','orange','yellow','violet']

states = ['A','B','C','D','E']

neighbours = {
    'A':['B','D','E'],
    'B':['A','D','C'],
    'C':['B'],
    'D':['A','E','B'],
    'E':['D','A']
}

state_colors = {}
def promising(state, color):
    for neighbour in neighbours.get(state): 
        color_of_neighbor = state_colors.get(neighbour)
        if color_of_neighbor == color:
            return False

    return True
    
for state in states:
    for color in colors:
        if promising(state, color):
            state_colors[state] = color

print (state_colors)
