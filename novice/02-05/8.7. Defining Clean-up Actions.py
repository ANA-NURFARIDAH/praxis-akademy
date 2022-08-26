# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
# print(bool_return())


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
print(divide(2, 1))
print(divide(2, 0))
print(divide("2", "1"))