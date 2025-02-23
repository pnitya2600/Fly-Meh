def min_planes(fuel_array):
  
    n = len(fuel_array)  # Get the total number of airports
    if n <= 1:
        return 0  # No planes needed if there's only one airport or none

    planes = 0  # Initialize the number of planes used
    current_position = 0  # Start at the first airport (index 0)

    while current_position < n - 1:  # Continue until the last airport is reached
        fuel = fuel_array[current_position]  # Get the fuel available at the current airport
        if fuel == 0:
            return -1  # Cannot proceed if no fuel is available at the current airport

        furthest_reach = min(current_position + fuel, n - 1)  # Calculate the furthest airport reachable from the current position
        if furthest_reach == current_position:
          return -1 #if you cannot move from current position then you are stuck.

        if furthest_reach == n - 1:  # If the last airport is reachable from the current position
            return planes + 1  

        next_position = current_position + 1 
        # Find the best next position to jump to, maximizing the reach from that position
        for i in range(current_position + 2, furthest_reach + 1):
            if i + fuel_array[i] > next_position + fuel_array[next_position]:
                next_position = i  # Update next_position if a better jump is found

        current_position = next_position  # Move to the best next position
        planes += 1  # Increment the number of planes used

    return planes  # Return the total number of planes used