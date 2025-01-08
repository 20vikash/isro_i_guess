from enum import Enum
import h, c
import time

KB = 1024
MB = 1024 * KB

class Stress(Enum):
    LIGHT_STRESS = MB  # 1MB
    MEDIUM_STRESS = 50 * MB  # 50MB
    HEAVY_STRESS = 500 * MB  # 500MB

def time_taken(stress):
    steps = []
    hHex = []
    cHex = []

    if stress == Stress['LIGHT_STRESS']:
        steps = [KB, 10 * KB, 100 * KB, 200 * KB, 500 * KB, MB]
    elif stress == Stress['MEDIUM_STRESS']:
        steps = [MB, 5 * MB, 10 * MB, 20 * MB, 30 * MB, 40 * MB, 50 * MB]
    elif stress == Stress['HEAVY_STRESS']:
        steps = [MB, 5 * MB, 10 * MB, 20 * MB, 30 * MB, 40 * MB, 50 * MB, 100 * MB, 200 * MB, 300 * MB, 400 * MB, 500 * MB]

    for i in steps:
        temp = b"A" * i

        start_time = time.time()
        h.getHmac(temp)
        hmac_duration = time.time() - start_time
        hHex.append(hmac_duration)

        start_time = time.time()
        c.getCmac(temp)
        cmac_duration = time.time() - start_time
        cHex.append(cmac_duration)

    print(hHex)
    print("\n")
    print(cHex)

    return hHex, cHex, steps
