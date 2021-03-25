def do_fizzbuzz():
    n = int(input())
    curr = 1
    while curr <= n:
        if curr % 3 == 0 and curr % 5 == 0:
            print(curr," : fizzbuzz")
        elif curr % 3 == 0:
            print(curr, " : fizz")

        curr += 1
        

do_fizzbuzz()
