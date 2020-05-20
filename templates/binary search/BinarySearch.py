from bisect import bisect_left, bisect_right

class Result:
    def __init__(self, index, value):
        self.index = index
        self.value = value

class BinarySearch:
    def __init__(self):
        pass

    @staticmethod
    def greater_than(num: int, func, size: int = 1):
        """Searches for smallest element greater than num!"""
        if isinstance(func, list):
            index = bisect_right(func, num)
            if index == len(func):
                return Result(None, None)
            else:
                return Result(index, func[index])
        else:
            alpha, omega = 0, size - 1
            if func(omega) <= num:
                return Result(None, None)
            while alpha < omega:
                if func(alpha) > num:
                    return Result(alpha, func(alpha))
                if omega == alpha + 1:
                    return Result(omega, func(omega))
                mid = (alpha + omega) // 2
                if func(mid) > num:
                    omega = mid
                else:
                    alpha = mid

    @staticmethod
    def less_than(num: int, func, size: int = 1):
        """Searches for largest element less than num!"""
        if isinstance(func, list):
            index = bisect_left(func, num) - 1
            if index == -1:
                return Result(None, None)
            else:
                return Result(index, func[index])
        else:
            alpha, omega = 0, size - 1
            if func(alpha) >= num:
                return Result(None, None)
            while alpha < omega:
                if func(omega) < num:
                    return Result(omega, func(omega))
                if omega == alpha + 1:
                    return Result(alpha, func(alpha))
                mid = (alpha + omega) // 2
                if func(mid) < num:
                    alpha = mid
                else:
                    omega = mid
