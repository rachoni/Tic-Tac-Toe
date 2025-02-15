import os

DRAW_STATS_FILE = os.path.join("data", "draw_stats.txt")

def show_stats_draw():
    if not os.path.exists(DRAW_STATS_FILE):
        print("No draw statistics found.")
        return

    with open(DRAW_STATS_FILE, "r") as file:
        draw_count = file.readline().strip()

    print(f"\n=== Draw Statistics ===\nTotal Draws: {draw_count}")