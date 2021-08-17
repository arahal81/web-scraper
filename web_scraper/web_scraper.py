import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    wiki_page = requests.get(url)
    results = BeautifulSoup(wiki_page.content, "html.parser").find_all(
        text="citation needed")
    return len(results)


def get_citations_needed_report(url):
    array_of_content = []
    wiki_page = requests.get(url)
    text = BeautifulSoup(wiki_page.content, "html.parser").find_all("p")

    for p in text:
        paragraphs = p.find_all(
            "sup", class_="noprint Inline-Template Template-Fact")

        if len(paragraphs) > 0:
            for i in paragraphs:
                array_of_content.append(p.text.strip())

    return "\n\n".join(array_of_content)


if __name__ == "__main__":
    print(get_citations_needed_count(
        "https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(get_citations_needed_report(
        "https://en.wikipedia.org/wiki/History_of_Mexico"))
