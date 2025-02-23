## Fly-Meh

# Minimum Planes to Destination

This repository contains a Python solution to determine the minimum number of planes required to reach a destination airport, given an array representing fuel availability at each airport.

## Problem Description

You are initially positioned at airport number one and need to reach the last airport (N). Each airport has a plane with limited fuel. You need 1 unit of fuel to travel to the next adjacent airport. The goal is to find the minimum number of planes required to reach the destination.

## Function Description

## Step-by-Step Explanation
# Initialization:

* n = len(fuel_array): Get the number of airports.
* planes = 0: Initialize plane count.
* current_position = 0: Start at the first airport.
# Base Cases:

* if n <= 1: return 0: If 1 or 0 airports, no planes needed.
# Iterative Travel:

* while current_position < n - 1:: Loop until the last airport.
* fuel = fuel_array[current_position]: Get current fuel.
* if fuel == 0: return -1: If no fuel, unreachable.
* furthest_reach = min(current_position + fuel, n - 1): Calculate max reach.
* if furthest_reach == current_position: return -1: if no movement possible, unreachable.
* if furthest_reach == n - 1: return planes + 1: If destination reached, return.
# Greedy Next Position Selection:
* next_position = current_position + 1: Start with the next airport.
* for i in range(current_position + 2, furthest_reach + 1):: Check reachable airports.
* if i + fuel_array[i] > next_position + fuel_array[next_position]: next_position = i: Find best next jump.
* current_position = next_position: Move to the chosen airport.
* planes += 1: Increment plane count.
# Return Result:

* return planes: Return total plane count.
