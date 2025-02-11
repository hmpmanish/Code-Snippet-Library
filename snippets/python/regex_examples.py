import re

# Find all email addresses in a string
text = "Contact us at support@example.com and info@example.com"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

print("Emails found:", emails)
