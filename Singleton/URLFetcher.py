import urllib.parse
import urllib.request

from Singleton.SingleType import SingletonType


class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)

                urls = self.urls
                urls.append(url)
                self.urls = urls

    def dump_url_registry(self):
        return ', '.join(self.urls)


def main():
    MY_URLS = ['http://www.voidspace.org.uk',
               'http://google.com',
               'http://python.org',
               'https://www.python.org/error',
               ]
    print(URLFetcher() is URLFetcher())
    fetcher = URLFetcher()
    fetcher.fetch('http://facebook.com')
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)

    print('-------')
    done_urls = fetcher.dump_url_registry()
    print(f'Done URLs: {done_urls}')

    f1 = URLFetcher()
    f2 = URLFetcher()
    print(f1 is f2)


if __name__ == '__main__':
    main()
