import re

text = """
Contact: Aira
Email: aira123@gmail.com
Phone: 017-123-4567

Contact: Nadia
Email: nadia.dev@company.com
Phone: 018-987-6543

Contact: Sara
Email: sara99@example.com
Phone: 019-555-1234
"""
pattern = re.compile(r"[a-z0-9.]+@[a-z0-9.]+\.[a-z]+")
matches = pattern.finditer(text)
for match in matches:
    print(match.group())