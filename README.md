## Using Re-inforcement Learning to select the Best ad based on live response from the Users

### About the Project

We have 10000 users. We have 10 versions of the same ad. We want to find which version among them is the best ad as soon as possible. We cannot exploit all the 10000 users, because advertising all 10 ads is damn costly.

### The Approach

We will use Re-inforcement learning to solve this problem ASAP. I have used UCB and Thompsons Sampling to solve this problem. The two methods are different from their approach towards the problem. 

### Difference between the UCB and Thompsons Approach

|------------------------------------------------------------|
|  Upper-Confidence-Bound    |  Thompson's Approach          |
|----------------------------|-------------------------------|
| 1.Deterministic Algorithm  | 1. Probabilistic Algorithm    |
|----------------------------|-------------------------------|
| 2. Requires an update at   | 2. It can accomodate delayed  |
|update round.               | feedback.                     |
|                            |                               |
|------------------------------------------------------------|