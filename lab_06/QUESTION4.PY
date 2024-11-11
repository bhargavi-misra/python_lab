def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disc {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')
