import re
import urllib.request

# url = "https://bit.ly/3rxQFS4"
# html = urllib.request.urlopen(url)

# html_contents = str(html.read())

# id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

# for result in id_results :
#     print(result)

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"
html = urllib.request.urlopen(url)

html_contents = str(html.read().decode("utf-8"))

id_results = re.findall(r"(http)(.+)(zip)", html_contents)

for result in id_results :
    print(result)