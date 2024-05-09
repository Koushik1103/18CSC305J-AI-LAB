def calculate_red_fish_to_remove(total_fish, initial_red_percentage, target_red_percentage):
    # Calculate the initial number of red fish
    initial_red_fish = total_fish * (initial_red_percentage / 100)
    
    # Calculate the target number of red fish
    target_red_fish = total_fish * (target_red_percentage / 100)
    
    # Calculate the number of red fish to be removed
    red_fish_to_remove = initial_red_fish - target_red_fish
    
    return red_fish_to_remove

# Given data
total_fish_in_aquarium = 200
initial_red_percentage = 99
target_red_percentage = 98

# Calculate the number of red fish to remove
red_fish_to_remove = calculate_red_fish_to_remove(total_fish_in_aquarium, initial_red_percentage, target_red_percentage)

print("Number of red fish to remove:", int(red_fish_to_remove))

