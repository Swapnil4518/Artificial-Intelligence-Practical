def hanoi_state_space(n):

    source = list(range(n, 0, -1))
    auxiliary = []
    destination = []

    pegs = [source, auxiliary, destination]
    names = ["Source", "Auxiliary", "Destination"]

    moves = []

    def move_disk(src, dst):

        if not pegs[src]:
            return False

        if pegs[dst] and pegs[dst][-1] < pegs[src][-1]:
            return False

        disk = pegs[src].pop()
        pegs[dst].append(disk)

        moves.append(
            f"Move disk {disk} from {names[src]} to {names[dst]}"
        )

        return True

    def solve(k, src, aux, dst):

        if k == 0:
            return

        solve(k - 1, src, dst, aux)

        move_disk(src, dst)

        solve(k - 1, aux, src, dst)

    print("-------- Tower of Hanoi -------")

    print("Initial State:", pegs)

    solve(n, 0, 1, 2)

    print("\nSolution Path:")

    for i, move in enumerate(moves, 1):
        print(f"{i}. {move}")

    print("\nGoal State:", pegs)

    print("Total Moves:", len(moves))


n = int(input("Enter number of disks: "))

hanoi_state_space(n)