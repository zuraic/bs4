from bs4 import BeautifulSoup
import lxml

with open("Website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
all_anchor_text = soup.find_all(name="a")
# print(all_anchor_text)

# for tag in all_anchor_text:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="#name")
print(company_url)

