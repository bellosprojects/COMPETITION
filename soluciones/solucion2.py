def get_data(_=[iter(())]):
 while 1:
  try:return next(_[0])
  except StopIteration:_[0]=iter(input().strip().split())


channels = {}
TARGET_CHANNEL : None | int = None
TARGET_TICK = 0

class Channel:

    def __init__(self, t, i1, i2, o):
        self.TYPE: str = t
        self.IN1: int = i1
        self.IN2: int | None = i2
        self.OUT: int = o

CDOORS : list[Channel] = []

def compute():

    olds_channles = channels.copy()

    for cd in CDOORS:

        if cd.TYPE == "N":
            channels[cd.OUT] = not olds_channles.get(cd.IN1, False)

        elif cd.TYPE == "A":
            channels[cd.OUT] = olds_channles.get(cd.IN1, False) and olds_channles.get(cd.IN2, False)

        elif cd.TYPE == "O":
            channels[cd.OUT] = olds_channles.get(cd.IN1, False) or olds_channles.get(cd.IN2, False)
        
def main():

    global TARGET_TICK, TARGET_CHANNEL

    TARGET_TICK, TARGET_CHANNEL, TOTAL_CDOORS = get_data(), get_data(), get_data()

    for _ in range(int(TOTAL_CDOORS)):
        in1 = int(get_data())
        cdoor = get_data()
        in2 = None

        if str(cdoor).isdigit():
            in2 = int(cdoor)
            cdoor = get_data()

        out = int(get_data())

        CDOORS.append(Channel(cdoor, in1, in2, out))

    for _ in range(int(TARGET_TICK)):
        compute()

    final_val = channels.get(int(TARGET_CHANNEL), False)
    print(1 if final_val else 0)

if __name__ == "__main__":
 main()