def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    current = str(x)
    for x in range(len(current)):
        if current[x] != current[len(current) - 1 - x]:
            return False
    return True
