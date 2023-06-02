from bs4 import BeautifulSoup


def toc_creator(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    heading_tags = ["h2", "h3", "h4"]
    for tags in soup.find_all(heading_tags):
        print(tags.text.strip())
 
article = """ put article here """

toc_creator(article)
