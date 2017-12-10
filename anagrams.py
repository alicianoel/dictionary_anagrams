#!/usr/bin/python

"""This program finds all anagrams of each word in a dictionary.

Example usage: 
```
$ python anagrams.py --dict-file words.txt [--caps]
acts, cast, cats, scat
ales, leas, sale, seal
amen, mane, mean, name
...
```

1) Sort all words in words_list by letters alphabetically.
2) Any words that have the same sorted letters are anagrams.
Using the sorted word as a key, make a defaultdict of all words
that share the same sorted word.
For example, 'trap' has anagrams 'part', 'rapt', and 'tarp', its
dictionary looks like: 
'aprt': ['trap', part', 'rapt', 'tarp']'
"""

from collections import defaultdict
from argparse import ArgumentParser

def LoadDictionary(filepath, caps):
  """Load a word dictionary text file to a list of strings.

  Args:
    filepath: str, path to text file, where each line has a single word.
    caps: bool, whether to consider words with captial leters.
  Returns:
    a list of strings.
  """
  saved_dict = []
  for line in file(filepath):
    if caps:
      line = line.lower()
    saved_dict.append(line.strip())

  return saved_dict

def SortLetters(input_str):
  """Sort leters of a string alphabetically.
  """
  return ''.join(sorted(input_str))

def FormatAnagram(anagrams_list, input_string):
  """Format inputs so that input_string is first, followed by its
  anagrams_list.

  For example, if input_string is 'team', and its anagrams_list is
  ['mate', 'meat',' tame'], this would return
  ['team', 'mate', 'meat',' tame'].

  Args:
    anagrams_list: list of str.
    input_string: str.
  Returns:
    list of str.
  """
  remaining = [x for x in anagrams_list if x != input_string]
  remaining.insert(0, input_string)

  return remaining

def FetchValidWords(words_list, min_letters):
  """Get strings from words_list where length of string is greater
  than min_letters.

  Args:
    words_list: list of str.
    min_letters: int, min length of strings to consider valid.

  Returns:
    list of str.
  """
  valid_words = []
  for word in words_list:
    if len(word) >= min_letters:
      valid_words.append(word)

  return valid_words

def GetAnagrams(words_list, min_letters):
  """Find all anagrams for each valid word in words_list.

  1) Sort all words in words_list by letters alphabetically.
  2) Any words that have the same sorted letters are anagrams.
  Using the sorted word as a key, make a defaultdict of all words
  that share the same sorted word.
  For example, 'trap' has anagrams 'part', 'rapt', and 'tarp', its
  dictionary looks like: 
  'aprt': ['trap', part', 'rapt', 'tarp']'

  Args:
    words_list: list of str.
    min_letters: int, min length of strings to consider valid.

  Returns:
    anagrams: list of lists containing strings.
    num_matches: int, number of matches.
  """
  valid_words_list = FetchValidWords(words_list, min_letters)
  word_dict = defaultdict(list) 
  for word in words_list:
    if word not in word_dict[SortLetters(word)]:
      word_dict[SortLetters(word)].append(word) 

  num_matches = 0
  anagrams = []
  for input_string in valid_words_list:
    sorted_string = SortLetters(input_string)
    # Check if there are at least as many anagrams as there are letters.
    if len(word_dict[sorted_string]) >= len(sorted_string):
      anagrams_list = word_dict[sorted_string]
      input_string_anagrams = FormatAnagram(anagrams_list, input_string)
      anagrams.append(input_string_anagrams)
      num_matches += 1

  return anagrams, num_matches


def main():
  parser = ArgumentParser(description = 'Anagram generator')
  parser.add_argument('--dict-file', required=True,
    help = "newline-separated dictionary file on which to get words.")
  parser.add_argument('--caps', dest='caps', action='store_true')
  parser.add_argument('--no-caps', dest='caps', action='store_false')
  parser.add_argument('--min_letters',type=int,
    help='Minimum number of letters in word to return anagrams.', required=False, default=4)
  parser.set_defaults(feature=True)
  args = parser.parse_args()

  dictionary = LoadDictionary(args.dict_file, args.caps)
  anagrams, num_matches = GetAnagrams(dictionary, args.min_letters)

  for item in anagrams:
    print(','.join(map(str, item)))
  print "Total valid words with at least %s letters  = %s" % (args.min_letters, num_matches)

if __name__ == '__main__':
  main()
