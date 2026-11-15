def calculate(user_px: int, buttons: dict[int, list[int]]):

    import math

    min_distance = math.inf
    best_button = -1

    for bt in buttons:

        for px in buttons[bt]:

            distance = abs(px - user_px)

            if distance < len(buttons[bt]):

                if distance < min_distance:
                    min_distance = distance
                    best_button = bt

    return best_button

def main():

    USER_PIXEL = int(get_data())
    NUM_BUTTONS = int(get_data())

    BUTTONS : dict[int, list[int]] = {}

    for _ in range(NUM_BUTTONS):
        ID_BUTTON = int(get_data())
        NUM_PIXELS = int(get_data())
        pixs = []

        for __ in range(NUM_PIXELS):
            pixs.append(int(get_data()))

        BUTTONS[ID_BUTTON] = pixs

    print(calculate(user_px=USER_PIXEL, buttons=BUTTONS))

if __name__ == "__main__":
    main()