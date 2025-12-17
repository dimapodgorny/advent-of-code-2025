def wrap(value, min_value, max_value):
    return min_value + (value - min_value) % (max_value - min_value)

def get_input(file_name: str) -> list:
    _inp: list = []
    with open(file_name, "r") as file:
        for line in file:
            _inp.append(line.strip())
    return _inp

def fix_input_value(value) -> int:
    as_int = int(value.removeprefix(value[0]))
    if value[0] == "L":
        as_int = -as_int
    return as_int


def part1(inp) -> int:
    pw: int = 0
    dial_position: int = 50
    print("Starting dial position:", dial_position)
    for inp_value in inp:
        print("NEXT")

        diff = fix_input_value(inp_value)
        dial_position += diff
        dial_position = wrap(dial_position, 0, 100)

        print("  inp = ", inp_value)
        print("  diff = ", diff)
        print("  dial = ", dial_position)
        if dial_position == 0:
            pw += 1

    print("pw = ", pw)
    return pw

def part2(inp) -> int:
    pw: int = 0
    dial_position: int = 50
    print("Starting dial position:", dial_position)
    for inp_value in inp:
        print("NEXT")
        diff = fix_input_value(inp_value)
        print("  diff =", diff)
        for i in range(abs(diff)):
            if diff < 0:
                dial_position += -1
            elif diff > 0:
                dial_position += 1
            dial_position = wrap(dial_position, 0, 100)
            if dial_position == 0:
                pw += 1
            print("    dial =", dial_position)

    print("pw = ", pw)
    return pw




from time import sleep
if __name__ == "__main__":
    #part1(get_input("input.txt"))
    part2(get_input("input.txt"))
