def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

def main(n):
    hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    n = 5
    main(n)
