from app.utils.winnowing_lib import get_fingerprint

code = """
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
"""



fp = get_fingerprint(code)

