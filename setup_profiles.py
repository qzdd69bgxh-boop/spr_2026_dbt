import shutil
from pathlib import Path

PLACEHOLDERS = [
    "account: ORG-ACCOUNT",
    "user: YOUR_SNOWFLAKE_USERNAME",
    "schema: dbt_YOUR_USERNAME",
    "private_key_path: C:/Users/your-username/.ssh/dbt_key.p8",
]

repo_dir = Path(__file__).parent
source = repo_dir / "profiles.yml"
example = repo_dir / "profiles.yml.example"
target = Path.home() / ".dbt" / "profiles.yml"

# Step 1 — create profiles.yml from example if it doesn't exist yet
if not source.exists():
    shutil.copy2(example, source)
    print("Created profiles.yml from the example template.")
    print("Open profiles.yml and fill in these values:")
    for p in PLACEHOLDERS:
        print(f"  - {p}")
    print("\nThen run this script again.")
    raise SystemExit(0)

# Step 2 — check that all placeholders have been replaced
content = source.read_text()
remaining = [p for p in PLACEHOLDERS if p in content]
if remaining:
    print("profiles.yml still has unfilled values:")
    for p in remaining:
        print(f"  - {p.split(': ', 1)[1]}")
    print("\nUpdate those in profiles.yml and run this script again.")
    raise SystemExit(1)

# Step 3 — copy to ~/.dbt/profiles.yml
if target.exists():
    answer = input(f"{target} already exists. Overwrite? [y/N] ").strip().lower()
    if answer != "y":
        print("Aborted.")
        raise SystemExit(0)

target.parent.mkdir(exist_ok=True)
shutil.copy2(source, target)
print(f"Copied to {target}")
print("Run 'dbt debug' to verify your connection.")
