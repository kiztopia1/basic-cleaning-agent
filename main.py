import time

# Initialize a sample 2D room layout
room = [
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]

# Function to print the current state of the room
def print_room(room):
    for row in room:
        print(" ".join(str(cell) for cell in row))
    print("\n")

# Function to suck dirt at the current position
def suck(room, x, y):
    print(f"Sucking dirt at position ({x}, {y})")
    room[x][y] = 0

# Function to check if there is dirt at the current position
def is_dirty(room, x, y):
    return room[x][y] == 1

# Clean the entire room row by row
def clean_room(room):
    room_height = len(room)
    room_width = len(room[0])

    print("Initial room state:")
    print_room(room)

    # Loop through each cell in the room
    for x in range(room_height):
        for y in range(room_width):
            # Clean if there's dirt
            if is_dirty(room, x, y):
                suck(room, x, y)
            
            # Print the room state after each action
            print("Room state after cleaning:")
            print_room(room)
            time.sleep(1)  # Slow down for readability

    print("Room is fully clean!")

# Start cleaning process
clean_room(room)
