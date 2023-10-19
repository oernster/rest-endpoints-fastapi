from fastapi import APIRouter


router = APIRouter()

def fibonacci(n):
    n = int(n)

    def fibon(a,b,n,result):
        c = a+b
        result.append(c)
        if c < n:
            fibon(b,c,n,result)
        return result

    return fibon(0,1,n,[])

# Note this only works up to a max fibonacci value of 'max_val' - to increase, increase this value by e.g. tenfold and rerun the program
max_val = 100000000
fib_seq = [0, 1]
fib_seq.extend(fibonacci(max_val))
iteration = 0

@router.get("/", tags=["root"])
def read_root():
    # I don't like globals but I don't want to calculate the fib sequence every time.
    global iteration
    output = {"result": f"{fib_seq[iteration]}"}
    iteration += 1
    return output
