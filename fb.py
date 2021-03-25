def do_fizzbuzz():
    n = int(input())
    curr = 1
    while curr <= n:
        if curr % 3 == 0 and curr % 5 == 0:
            print(curr," : fizzbuzz")
        elif curr % 3 == 0:
            print(curr, " : fizz")
        elif curr % 5 == 0:
            print(curr, " : buzz")

        curr += 1
def do_fizzbuzz_by_listComprehension(num):
    result = ["fizzbuzz" if i % 15 == 0 
            else "fizz" if i % 3 == 0 
            else "buzz" if i % 5 == 0 
            else i 
            for i in range(1, num+1)
            ]
    print(result)

if __name__ == "__main__":
    do_fizzbuzz()
    num = int(input())
    do_fizzbuzz_by_listComprehension(num)
