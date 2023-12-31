import pprint
doc = """Dictionaries contain key-value pairs. Keys are like a list's indexes.
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
The get() method can return a default value if a key doesn't exist.
The setdefault() method can set a value if a key doesn't exist.
The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output."""
count = {}
for char in doc:
    count.setdefault(char,0)
    count[char] += 1

pprint.pprint(count)