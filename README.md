# Introduction to PageRank

PageRank is and Artificial Intelligence to rank web pages by importance. The program uses the concept of "The Random Surfer Model", applied to two different methods:

1. A Markov Chain of samples.
2. An Iterative Algorithm.

The PageRank AI was created as part of the CS50 Artificial Intelligence with Python course at the Harvard University.

## The Markov Chain of samples

The Random Surfer Model considers the behavior of a hypothetical surfer on the internet who clicks on links at random. The method is here implemented as a Markov Chain, where each page represents a state, and each page has a transition model that chooses among its links at random. At each time step, the state switches to one of the pages linked to by the current state.

By sampling states randomly from the Markov Chain, the AI gets an estimate for each page’s PageRank. To ensure the AI always can get to somewhere else in the corpus of web pages, the model uses a damping factor `d`. With probability `d`, the Random Surfer will choose from one of the links on the current page at random. But otherwise (with probability `1 - d`), the Random Surfer chooses one out of all of the pages in the corpus at random (including the one they are currently on).

Keeping track of how many times each page has shown up as a sample, the AI can treat the proportion of states that were on a given page as its page rank.

## The Iterative Algorithm

The Iterative Algorithm uses a recursive mathematical expression to iteratively calculate the page rank.

Let $PR(p)$ be the probability of the Random Surfer being at a given page $p$, $d$ is the damping factor, $N$ is the total number of pages in the corpus, $i$ ranges over all pages that link to page $p$, $PR(i)$ is the probability that the Random Surfer are on page $i$ at any given time, and $NumLinks(i)$ is the number of links present on page $i$:

$$
PR(p)=\frac{1-d}{N}+d\sum\frac{PR(i)}{NumLinks(i)}
$$

The formula takes into account that there are two ways in which the Random Surfer could end up on a page:

1.  With probability $1 - d$, the Surfer chose a page at random and ended up on page $p$.
2.  With probability $d$, the Surfer followed a link from a page $i$ to page $p$.

The program iteratively calculates the pages probabilities, until the probability converges to be less than $0.001$. The starting point for the calculation assumes that every page has a probability of $1/N$.

# Running the program

After downloading the files in the repository, the program may be run with the command:

```
python pagerank.py corpus0
```

If running the above command, using `corpus0`, you will get an output similar to the below (but with slightly different values):

```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```

There are three sample corpuses provided in the repository, which you can use to test the AI: `corpus0`, `corpus1`, and `corpus2`. You may of course compile your own corpus of webpages to test as well.

# Intellectual Property Rights

MIT
