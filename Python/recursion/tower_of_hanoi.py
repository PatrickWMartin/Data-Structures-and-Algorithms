def tower_of_hanoi(n, source, helper, destination):
    if n == 0:
        return
    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Disk {n} from rod {source} to rod {destination}")
    tower_of_hanoi(n-1, helper, source, destination)


tower_of_hanoi(3, 'A', 'B', 'C')
