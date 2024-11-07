# Vacuum Cleaner Agent

This is a simple Python project demonstrating a vacuum cleaner agent for a 2D grid. The agent moves through a room and "cleans" each cell that has dirt.

## Project Structure

- **room**: A 2D list representing the room layout. `1` represents dirt, and `0` represents a clean cell.
- **Functions**:
  - `initialize_room(size)`: Creates a random room layout.
  - `suck(room, x, y)`: Cleans the current cell.
  - `is_dirty(room, x, y)`: Checks if the current cell has dirt.
  - `clean_room(room)`: Runs the cleaning process, moving through each cell in the room.
  - `print_room(room)`: Displays the room layout.

## Example Usage

The agent will:
1. Start at the top-left cell.
2. Move through each cell in each row.
3. Suck if the cell contains dirt.
4. Stop once all cells are clean.

## Code

```python
import time

room = [
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1]
]

def print_room(room):
    for row in room:
        print(" ".join(str(cell) for cell in row))
    print("\n")

def suck(room, x, y):
    print(f"Sucking dirt at position ({x}, {y})")
    room[x][y] = 0

def is_dirty(room, x, y):
    return room[x][y] == 1

def clean_room(room):
    room_height = len(room)
    room_width = len(room[0])
    print("Initial room state:")
    print_room(room)

    for x in range(room_height):
        for y in range(room_width):
            if is_dirty(room, x, y):
                suck(room, x, y)
            print("Room state after cleaning:")
            print_room(room)
            time.sleep(1)
    print("Room is fully clean!")

clean_room(room)
