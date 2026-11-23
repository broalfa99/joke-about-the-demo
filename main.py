"""The joke about the demo: a one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (1-280 Unicode code points, UTF-8).
Runs with no network.
"""

JOKE = "My AI agent's demo went flawlessly \u2014 until, live in front of the whole room, it confidently deleted the database."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
