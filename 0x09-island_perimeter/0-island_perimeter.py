#!/usr/bin/python3
'''0x09. Island Perimeter task'''


def island_perimeter(grid):
    '''returns perimeter of island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # index of the last list in the grid
    lst_max = len(grid[0]) - 1  # index of the last square in list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # both left and right
                if land_idx == 0:
                    # the left side
                    counter += 1

                    # the right side
                    if lst[land_idx + 1] == 0:
                        counter += 1
                elif land_idx == lst_max:
                    # the left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # the right side
                    counter += 1
                else:
                    # the left side
                    if lst[land_idx - 1] == 0:
                        counter += 1

                    # the right side
                    if lst[land_idx + 1] == 0:
                        counter += 1

                # both top and down
                if lst_idx == 0:
                    # top side
                    counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1
                elif lst_idx == grid_max:
                    # the top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    counter += 1
                else:
                    # top side
                    if grid[lst_idx - 1][land_idx] == 0:
                        counter += 1

                    # bottom side
                    if grid[lst_idx + 1][land_idx] == 0:
                        counter += 1

    return counter
