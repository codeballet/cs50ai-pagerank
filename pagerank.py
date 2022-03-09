import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    model = dict()
    links_list = corpus[page]
    links_len = len(links_list)
    corpus_list = list(corpus.keys())
    corpus_len = len(list(corpus.keys()))

    # if page has no outgoing links return equal probabilities
    if links_len == 0:
        for item in corpus_list:
            model[item] = 1 / corpus_len

        return model

    # calculate probability of links from page
    pl = (1 / links_len) * damping_factor

    # calculate probability of all pages
    pa = (1 / corpus_len) * (1 - damping_factor)

    # generate probability distribution as dict
    for item in corpus_list:
        if item in links_list:
            model[item] = pl + pa
        else:
            model[item] = pa

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    print('Inside sample_pagerank')

    page = ''
    page_rank = dict()

    for i in range(n):
        # check if first run
        if i == 0:
            # randomly get a page
            page = random.choice(list(corpus.keys()))
            # update rank count of page
            page_rank[page] = 1

        # get a transition model for the page
        trans_model = transition_model(corpus, page, damping_factor)

        # turn keys, values from transition model into ordered lists
        pages = []
        probabilities = []
        for key, value in trans_model.items():
            pages.append(key)
            probabilities.append(value)

        # randomly get a new page using transition model lists
        page = random.choices(pages, weights=probabilities, k=1)[0]

        # update rank count of page
        if not page_rank.get(page):
            page_rank[page] = 0
        page_rank[page] += 1

    # normalize page_rank count to probability distribution
    for key, value in page_rank.items():
        page_rank[key] = value / n

    print(f'page rank: {page_rank}')

    # check sum of probability distribution of page rank
    total = 0
    for value in page_rank.values():
        total += value
    print(f'sum of probability distribution: {total}')

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # assign each page a rank of 1 / (total number of pages in corpus)
    page_rank = dict()

    for page in corpus:
        print(f'page in corpus: {page}')
    # calculate new rank values based on all of the current rank values
    # repeat process until no values changes by more than 0.001

    raise NotImplementedError


if __name__ == "__main__":
    main()
