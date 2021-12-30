def list_manipulation(nums, command, location, value = None):
    if command == "remove" and location == "end":
        return nums.pop(-1)
    elif command == "remove" and location == "beginning":
        return nums.pop(0)
    elif command == "add" and location == "beginning":
        nums.insert(0, value)
        return nums
    elif command == "add" and location == "end":
        nums.append(value)
        return nums
print(list_manipulation([1, 2, 3, 4], "add", "end", 6))
print(list_manipulation([4, 6, 8, 5], "remove", "end"))

        