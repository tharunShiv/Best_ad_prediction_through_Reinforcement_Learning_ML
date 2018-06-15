## Using Re-inforcement Learning to select the Best ad based on live response from the Users

### About the Project

We have 10000 users. We have 10 versions of the same ad. We want to find which version among them is the best ad as soon as possible. We cannot exploit all the 10000 users, because advertising all 10 ads is damn costly.

### The Approach

We will use Re-inforcement learning to solve this problem ASAP. I have used UCB and Thompsons Sampling to solve this problem. The two methods are different from their approach towards the problem. 

### Difference between the UCB and Thompsons Approach

| Upper-Confidence-Bound | Thompson's Approach|
|:--------:| -------------:|
| 1. Deterministic Algorithm| 1. Probabilistic Algorithm |
|2. Requires an update at every round|2. It can accomodate delayed feedback.|
|3. Slower Result in this case | 3. Faster result in this case |

### How to run the code?
Open the respective files and run the code, as easy as that

### Which Algorithm gave the best result?
Thompson's Algorithm did.

### May I contribute?
Yes. You may contribute other Algorithms, Datasets, modification in the existing methods used.
