# def show_grid(grid):
#     for grid_row in grid:
#         print(grid_row)
#
#
# def row_selection(player_slot, grid, cellShape):
#     if player_slot in [0,1,2]:
#         row_change(grid[0], player_slot, cellShape)
#     elif player_slot in [3,4,5]:
#         row_change(grid[1], player_slot, cellShape)
#     else:
#         row_change(grid[2], player_slot, cellShape)
#     return grid
#
#
#
#
#
#
#
#
# def row_change(row, player_slot, cellShape):
#     if player_slot in [0, 3, 6]:
#         row[0] = cellShape
#     elif player_slot in [1, 4, 7]:
#         row[1] = cellShape
#     else:
#         row[2] = cellShape
#     return row
#
# def occupy_slot(player_slot, cellShape):
#     if player_slot in slots:
#         new_grid = row_selection(player_slot, grid, cellShape)
#         slots.remove(player_slot)
#         print(slots)
#         show_grid(new_grid)
#     else:
#         print("Slot is already consumed")
#         print(slots)
#
#
#
# print("Welcome to Tic Tac Toe, developed by TahaLearns!")
# print("The slots will be filled by choosing the location from [0-8]")
#
# cellX = ["__X__"]
# cellY = ["__O__"]
# cellEmp = ["_____"]
#
# slots = list(range(0,9))
#
# row1 = [cellEmp, cellEmp, cellEmp,]
# row2 = [cellEmp, cellEmp, cellEmp,]
# row3 = [cellEmp, cellEmp, cellEmp,]
#
# grid = [row1,row2,row3]
#
# show_grid(grid)
#
#
# while True:
#     player_slot1 = int(input("Player 1: Enter the desired slot: "))
#     occupy_slot(player_slot1, cellX)
#     player_slot2 = int(input("Player 2: Enter the desired slot: "))
#     occupy_slot(player_slot2, cellY)
#
#
#
#