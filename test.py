file_path = input("Path to metrics file (e.g., raw_metrics.txt): ").strip()
term      = input("Search term (e.g., LOC, SLOC, Comments): ").strip()
ignore_cs = input("Ignore case? [y/N]: ").lower().startswith("y")

try:
    with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
        needle = term.lower() if ignore_cs else term
        for line in fh:
            haystack = line.lower() if ignore_cs else line
            if needle in haystack:
                print(line.rstrip())
except FileNotFoundError:
    print(f" File not found: {file_path}")
except OSError as exc:
    print(f" Cannot open {file_path}: {exc}")