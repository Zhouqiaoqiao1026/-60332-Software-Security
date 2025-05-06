# Test 3: Index out of bounds in a for loop

def main():
    lst = [0, 1, 2]
    for i in range(5):  # i is up to 4, which exceeds the last element of lst
        value = lst[i]
        assert value >= 0

main()
