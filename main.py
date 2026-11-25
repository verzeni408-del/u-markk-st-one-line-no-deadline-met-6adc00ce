ENTRY = "I uploaded it to the wrong shared drive, and now a kindergarten class in Ohio is grading our Q3 roadmap."

assert "\n" not in ENTRY
assert 1 <= len(ENTRY) <= 200

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
