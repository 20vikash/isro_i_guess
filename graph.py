import matplotlib.pyplot as plt  # type: ignore

KB = 1024
MB = 1024 * KB

def plot_results(hHex, cHex, stress):
    steps = []

    if stress == "light":
        steps = ["1KB", "10KB", "100KB", "200KB", "500KB", "1MB"]
    elif stress == "medium":
        steps = ["1MB", "5MB", "10MB", "20MB", "30MB", "40MB", "50MB"]
    elif stress == "heavy":
        steps = ["1MB", "5MB", "10MB", "20MB", "30MB", "40MB", "50MB", "100MB", "200MB", "300MB", "400MB", "500MB"]

    hmac_sizes = [step for step in steps]
    hmac_times = [item for item in hHex]

    cmac_sizes = [step for step in steps]
    cmac_times = [item for item in cHex]

    plt.figure(figsize=(10, 6))
    plt.plot(hmac_sizes, hmac_times, label="HMAC", marker='o', color='blue')
    plt.plot(cmac_sizes, cmac_times, label="CMAC", marker='x', color='red')

    plt.xlabel('Input Size', fontsize=12)
    plt.ylabel('Time Taken (seconds)', fontsize=12)
    plt.title('Time Taken for HMAC vs CMAC', fontsize=14)
    
    plt.grid(True)
    
    plt.legend()

    plt.show()
