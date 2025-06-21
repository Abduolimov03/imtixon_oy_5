# 2.n ta butun sonlardan iborat a massiv berilgan. b massivni hosil qiluvchi decorator yozilsin. b massivning har bir elementi quyidagicha hisoblanadi:
# b[k] = a[0] + a[1] + ... + a[k]


def sum_decorator(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        b = []
        yigindi = 0
        for i in a:
            yigindi += i
            b.append(yigindi)
        return b

    return wrapper

@sum_decorator
def get_array():
    return [1 , 5 ,2 , 2, 4, 1, 1]
print(get_array())

