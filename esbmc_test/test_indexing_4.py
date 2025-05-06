# Test 4: Index out of bounds in a while loop

def main():
    lst = [5, 6, 7]
    i = 0
    while i <= 5:  # Error condition, list length exceeded
        value = lst[i]
        assert value >= 0
        i += 1

main()
