#LINK TO THE PROBLEM - https://www.geeksforgeeks.org/problems/print-anagrams-together/1

# words = ['act', 'god', 'cat', 'dog', 'tac']
# print(words)
class PrintAnagramsTogether:
    def Anagrams(self,words, n):
        # create a dict where the key will be the sorted word and the value should be the list of matched words in original list
        anagrams = {}

        for word in words:
            sort_word = ''.join(sorted(word))
            # if the sorted word is not present in the dict then add it to the dict
            if sort_word not in anagrams:
                anagrams[sort_word] = [word]
            #if the sorted word is already present then add the word to the key in the form of list
            else:
                anagrams[sort_word].append(word)

        # print(anagrams)
        for i in anagrams.values():
            print(' '.join(i))

n = int(input("Enter the no.of elements:"))
words = eval(input("Enter the words:"))
p1 = PrintAnagramsTogether()
p1.Anagrams(words, n)


#OUTPUT

# Enter the words['act', 'god', 'cat', 'dog', 'tac']
# act cat tac
# god dog

####################################################################################################

# words = ['act', 'god', 'cat', 'dog', 'tac']

# sort = sorted(words)
#
# print(f"The sorted set in alphabetical order is {sort}")
#
# l = []
# for i in sort:
#     l.append(''.join(sorted(i)))
#
# print(f"The list after sorting the letters of each word is: {l}")
#
# # create a dictionary where the key should be the original word and the value should be the sorted word
#
# d = {}
# for i in sort:
#     d[i] = ''.join(sorted(i))
#
# print(f"The dictionary: {d}")
#
# ####################################################################################################
# c=[]
# w = []
# first = d['act']
# for i in d:
#      #act
#     if d[i] == first:
#         c.append(i)
#     else:
#         first = d[i]
#         #create a new list
#         if d[i] == first:
#             w.append(i)
#
# print(c,w)

###########################################################################






