import sys
from app.pipeline import solve_assignment

def main():
    if len(sys.argv) != 2:
        print("Usage: python cli.py <path-to-html>")
        sys.exit(1)
    path = sys.argv[1]
    html = open(path, "r", encoding="utf-8").read()
    report = solve_assignment(html)
    import json
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main() 