import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def heuristic(state):
    distance = 0

    for i, value in enumerate(state):
        if value == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_index = GOAL.index(value)
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start):
    priority_queue = []

    h = heuristic(start)

    heapq.heappush(priority_queue, (h, 0, start, []))

    visited = set()

    while priority_queue:

        f, g, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        path = path + [state]

        if state == GOAL:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path)
                )

    return None


def print_state(state):

    for i in range(0, 9, 3):
        print(
            " ".join(
                "_" if x == 0 else str(x)
                for x in state[i:i + 3]
            )
        )

    print()


print("========== A* Search for 8-Puzzle ==========")

start = tuple(
    map(
        int,
        input("Enter initial state (use 0 for blank): ").split()
    )
)

solution = a_star(start)

if solution:

    print("\nSolution Found!")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for step, state in enumerate(solution):

        print("Step", step)
        print_state(state)

else:
    print("No solution found.")