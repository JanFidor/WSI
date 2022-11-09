class Problem:
    def __init__(self, input_size) -> None:
        self.input_size = input_size

    def evaluate(self, input):
        assert(self.input_size == len(input))
        
        i = 0

        fuel = list(input).count("1")

        height = 200
        acceleration = 0
        velocity = 0
        mass = 200 + fuel
        while height > 2:
            if(i < self.input_size and input[i] == "1"):
                mass -= 1
                acceleration += 45 / mass
                
            acceleration -= 0.09
            velocity += acceleration
            height += velocity
            i += 1

        if 0 < height < 2 and abs(velocity) < 2: return 2000 - fuel
        return -1000
