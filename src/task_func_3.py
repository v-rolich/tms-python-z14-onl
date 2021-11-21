from task_func_2 import validate_args


class Math:
    def __init__(self, x, y):
        validate_args(x, y)
        self.x = x
        self.y = y

    def calc_sum(self):
        return self.x + self.y

    def calc_diff(self):
        return self.x - self.y

    def calc_mult(self):
        return self.x * self.y

    def calc_div(self):
        return self.x / self.y
