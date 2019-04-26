class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord):
            return 0

        # Making a dictionary of key value pairs and key being the from of *ot or h*t for example
        # and value being the list of words in the wordList that matches the key regex
        hmap = {}
        for word in wordList:
            for charIndex in range(0, len(word)):
                temp = word[:charIndex] + '*' + word[charIndex + 1:]
                if temp not in hmap:
                    hmap[temp] = [word]
                else:
                    hmap[temp].append(word)

        # Executing breadth first search from beginWord to find the endWord, if cannnot, then return 0
        visited = []
        queue = [beginWord]
        level = 1
        while queue:
            length = len(queue)
            while length > 0:
                word = queue.pop(0)
                for charIndex in range(0, len(word)):
                    temp = word[:charIndex] + '*' + word[charIndex + 1:]
                    if temp not in hmap:
                        continue
                    nextWords = hmap[temp]
                    for nextWord in nextWords:
                        if endWord == nextWord:
                            return level + 1
                        elif nextWord in visited:
                            continue
                        else:
                            visited.append(nextWord)
                            queue.append(nextWord)
                length -= 1
            level += 1
        return 0
            
                
        