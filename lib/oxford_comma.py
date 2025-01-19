def oxford_comma(items):
    if len(items) == 1:
        return (items[0])
    elif len(items) == 2:
        return (f"{items[0]} and {items[1]}")
    elif len(items) == 3:
        return (f"{items[0]}, {items[1]}, and {items[2]}")
    elif len(items) >= 4:
        oxford_list = []
        for i in range(len(items)):
            if i < len(items) -1:
                oxford_list.append(f"{items[i]}, ")
            elif i == len(items) -1:
                oxford_list.append(f"and {items[i]}")
        return "".join(oxford_list)

