import os

RESULTS_FILE = os.path.join("data", "result.txt")

def show_stats():
    if not os.path.exists(RESULTS_FILE):
        print("No game results found.")
        return

    data = {}
    with open(RESULTS_FILE, "r") as file:
        for row in file.readlines():
            name, score = row.strip().split(", ")
            try:
                data[name] = int(score)
            except ValueError:
                pass

    sorted_data = sorted(data.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    print("\n=== Player Statistics ===")
    for name, score in sorted_data:
        print(f"{name} -> {score}")