import re


def linkify(text):
    url_pattern = re.compile(
        r'(\b(https?|ftp|file)://[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+&@#/%=~_|])', re.IGNORECASE)
    return re.sub(url_pattern, r'<a href="\1">\1</a>', text)


input_text = "Check out this website: https://www.example.com"
linked_text = linkify(input_text)
print(linked_text)  # Output: Check out this website: <a href="https://www.example.com">https://www.example.com</a>
