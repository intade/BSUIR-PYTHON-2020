def cached(func):
    cache = {}
    def wrapper(*args):
        if cache.get(args, False) is False:
            cache[args] = func(*args)
        else:
            print("already cached")
        return cache[args]
    return wrapper

@cached
def a(x, y):
    return x + y

print(a(2,3))
print(a(2,3))
print(a(5,6))