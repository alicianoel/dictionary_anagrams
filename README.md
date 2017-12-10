# dictionary_anagrams

This program finds all anagrams of each word in a dictionary, given the restrictions that the word has at least 4 letters, and there are at least as many anagrams as there are letters.

The dictionary is a newline separated text file, like the one found in /usr/dict/words or /usr/share/dict/words.

#Assumptions

- Words containing apostrophes are currently not considered.
- Words with the first letter capitalized (proper nouns) can be considered if the optional '--caps' flag is used.
- Words with special characters are not considered.
- Note that the output words are not unique-- if a word is present in the anagram list of another word, it will also have its own anagram list. For example, 'beat' is in the anagram list for 'abet', but 'beat' will still have its own list of anagrams as another line of output.

# Sample usage

```
$ python anagrams.py --dict-file words.txt [--caps]
abet, bate, beat, beta
abets, baste, bates, beast, beats, betas
acts, cast, cats, scat
ales, leas, sale, seal
amen, mane, mean, name
arced, cadre, cared, cedar, raced
ares, ears, eras, sear, sera
arts, rats, star, tars, tsar
asps, pass, saps, spas
aster, rates, stare, tares, tears
bares, baser, bears, saber, sabre
...
```

# How it works

This program uses [Python defaultdict](https://docs.python.org/2/library/collections.html#defaultdict-objects) to group sequences of key-value pairs into a dictionary of lists. 

First it orders every string in the dictionary by its letters. When words that are anagrams of eachother are sorted by letters, they will have the same sorted word. Example: when both the words 'traces' and 'carets' are sorted by their letters, they become 'acerst'.

Then, as the loop traverses through the word dictionary, if the sorted word is already in the defaultdict, it adds the original word to the defaultdict list for that word. Example: the defaultdict would contain 'acerst': ['carets, 'traces'].





