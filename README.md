# Analytics Engineering with dbt + Snowflake

This repo is a Snowflake adaptation of the free [Analytics Engineering for Students](https://learn.getdbt.com/learn/learning-path/analytics-engineering-for-students) learning path on dbt Learn. The course was designed for Google BigQuery — this guide swaps BigQuery for **Snowflake** and uses **dbt CLI (dbt Fusion)** + **VS Code** throughout.

---

## Prerequisites

- VS Code installed
- Git installed and a GitHub account
- Python 3.9+ installed
- A Snowflake account (provided by your instructor)
- Your SSH key pair registered with Snowflake (see below)

Install the dbt Fusion CLI:

```bash
# Mac / Linux
pip install dbt-core dbt-snowflake
# If that fails on Mac, try:
pip3 install dbt-core dbt-snowflake

# Windows
python -m pip install dbt-core dbt-snowflake
```

---

## Step 1 — Generate your SSH key pair

Key-pair auth is required for connecting to Snowflake. Password and browser-based auth are not supported in this setup.

### Windows (use Git Bash, not PowerShell)
```bash
mkdir -p ~/.ssh
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out ~/.ssh/dbt_key.p8 -nocrypt
cat ~/.ssh/dbt_key.p8 | clip
```
Your key is now on your clipboard. Send it to your instructor.

### Mac
```bash
mkdir -p ~/.ssh
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out ~/.ssh/dbt_key.p8 -nocrypt
cat ~/.ssh/dbt_key.p8 | pbcopy
```
Your key is now on your clipboard. Send it to your instructor.

### Linux
```bash
mkdir -p ~/.ssh
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out ~/.ssh/dbt_key.p8 -nocrypt
cat ~/.ssh/dbt_key.p8 | xclip -selection clipboard
```
If `xclip` is not installed: `sudo apt install xclip`. Your key is now on your clipboard. Send it to your instructor.

---

## Step 2 — Clone your copy of this repo

Use this repo as a template to create your own copy on GitHub, then clone it:

```bash
git clone <YOUR_REPO_URL>
cd <YOUR_REPO_NAME>
```

---

## Step 3 — Configure `profiles.yml`

Run the setup script and follow its prompts:

```bash
python setup_profiles.py
```

The first run creates `profiles.yml` in the repo and tells you exactly which values to fill in. Fill them in, then run the script again — it validates everything is set and copies it to the right place (`~/.dbt/profiles.yml`).

> ⚠️ Never commit `profiles.yml` to git — it contains your private key path. It's already in `.gitignore`.

---

## Step 4 — Verify your connection

```bash
dbt debug
```

`dbt debug` should return `All checks passed!`. If it fails, double-check your `profiles.yml` values and that your instructor has registered your key.

---

## Step 5 — Follow the learn.getdbt.com course

Work through the [Analytics Engineering for Students](https://learn.getdbt.com/learn/learning-path/analytics-engineering-for-students) modules. Wherever the course instructs you to:

| Course says (BigQuery) | Do this instead (Snowflake) | Already have |
|---|---|:---:|
| Create a BigQuery project | Use your Snowflake account (instructor provides it) | ✓ |
| Set up a BigQuery connection in dbt Cloud | Use `profiles.yml` with `type: snowflake` | ✓ |
| Use the dbt Cloud IDE | Use VS Code + dbt Fusion CLI in the terminal | ✓ |
| `dataset:` in profiles.yml | `schema:` in profiles.yml | ✓ |
| Run `dbt init` to create a new project | Skip — `dbt_project.yml` is pre-configured for Snowflake | ✓ |
| Find or create seed data | Seed CSVs are in `seeds/` — just run `dbt seed` when the video says to | ✓ |

---

## Common dbt commands

```bash
dbt debug          # verify Snowflake connection
dbt seed           # load raw CSV data into Snowflake
dbt run            # run all models
dbt test           # run all tests
dbt build          # seed + run + test in one step
dbt run -s <model> # run a single model
dbt test -s <model> # test a single model
dbt docs generate && dbt docs serve  # browse project docs
```

---

## Project structure

```
├── models/
│   ├── staging/        # views that clean + standardize raw source tables
│   └── analytics/      # tables built for analysis (you build these)
├── macros/             # reusable SQL functions
├── seeds/              # raw source CSVs loaded into Snowflake via dbt seed
├── tests/              # custom data tests (you add these)
├── analyses/           # ad-hoc SQL scratchpad
├── dbt_project.yml     # project config — profile name must match profiles.yml
└── profiles.yml.example
```

---

## Capstone checklist

- [ ] Analytics question(s) defined
- [ ] At least one analytics model built that answers your question
- [ ] Schema tests on primary keys (`unique`, `not_null`)
- [ ] At least one business-logic test
- [ ] Key models and columns have descriptions
- [ ] `dbt build` passes cleanly
- [ ] README includes: insights backed by data + next steps

---

## Resources

- [dbt Learn course](https://learn.getdbt.com/learn/learning-path/analytics-engineering-for-students)
- [Capstone template repo](https://github.com/atrivedi-dbtlabs/capstone_template)
- [Snowflake key-pair auth docs](https://docs.snowflake.com/en/user-guide/key-pair-auth)
