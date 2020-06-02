import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    # sort by votes, use lambda function
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        # if no href, set href as None
        href = links[idx].get('href', None)
        # if no one vote means no point, it will go wrong: idx out of range
        # links and votes no match
        # the solution is crawl subtext, then check if it has points
        # select score tag
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def main():
    page_num = 0
    while True:
        res = requests.get(f'https://news.ycombinator.com/news?p={page_num}')
        # use BeautifulSoup to parse HTML file
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        if not links:
            print(page_num)
            print('All done!')
            break
        print('[page_num]', page_num)
        subtext = soup.select('.subtext')
        pprint.pprint(create_custom_hn(links, subtext))
        page_num += 1


if __name__ == '__main__':
    main()
