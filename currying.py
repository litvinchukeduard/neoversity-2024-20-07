# fn(3)(6)(2)  //11

def calculate(a: int):
    def calculate_inner_one(b: int):
        def calculate_inner_three(c: int):
            return c + b + a
        return calculate_inner_three
    return calculate_inner_one

print(calculate(3)(6)(2))