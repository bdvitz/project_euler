# projecteuler.net solutions
def solution0001(maximum: int):
    s = set(range(3,maximum,3)) | set(range(5,maximum,5))
    return sum(s)
if __name__ == "__main__":
    print(solution0001(1000))