# voicebox

# Project Structure
The classes are structured as follows:

- A corpus has a tree with the frequencies of all n-grams up to a certain size present in a source, and information about which words precede and follow these

# Algorithm Overview
The approach to generating word lists is Markov-esque but is not strictly a Markov process, which would need to be stochastic. Here, the user has the final decision.

At each step of the sentence, the script uses the n most recent words to determine a list of the m most likely words to come next. The Markov determination of this list is a weighted combination of several lists, with higher weights given to lists of words that followed larger n-grams that constitute the immediate context.

For instance, when n=2 and the most recent two words in the sentence are "my big", the following lists factor into supplying the list of m words:

- List of words following "my big" (this is given the highest weight)
- List of words following "big" (next highest weight)
- List of words occurring two after "my" (lower weight)
- List of words occurring most frequently overall in the source (this list never changes and is a fallback when, as often happens with shorter sources, the other three lists are bare)

A similar pattern holds for higher values of n, with larger n-grams emphasized ver smaller n-grams, and closer n-grams emphasized over more distant ones.
