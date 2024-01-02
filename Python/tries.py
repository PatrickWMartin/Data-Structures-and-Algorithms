class Trie:

    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def exists(self, word):
        current = self.root
        for letter in word:
            if letter in current:
                current = current[letter]
            else:
                return False
        if self.end_symbol in current:
            return True
        return False

    def words_with_prefix(self, prefix):
        word_list = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]
        return self.search_level(current, prefix, word_list)

    def search_level(self, curr, curr_prefix, words):
        if self.end_symbol in curr:
            words.append(curr_prefix)
        for key in sorted(curr):
            if key != self.end_symbol:
                word_list = []
                self.search_level(curr[key], curr_prefix + key, word_list)
                words += word_list
        return words

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i:j + 1])
        return matches

