words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

#######################################################
#method 1 :    .get()

counter_dict = {}

for word in words:
    counter_dict[word] = counter_dict.get(word, 0) + 1

print(counter_dict)

#expectd output:  {'apple': 3, 'banana': 2, 'cherry': 1}

# time complexity : O(n)
# space complexity = O(k), where k = number of distinct words (since dictionary stores only unique keys)

###################################################
#method 2 : if-else

counter_dict = {}

for word in words:
    if word in counter_dict:
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1

print(counter_dict)

#expectd output:  {'apple': 3, 'banana': 2, 'cherry': 1}

# time complexity : O(n)
# space complexity = O(k), where k = number of distinct words (since dictionary stores only unique keys)

###########################################################
# method 3: collections.Counter

from collections import Counter

counter_dict = Counter(words)
print(counter_dict)

#expectd output:  {'apple': 3, 'banana': 2, 'cherry': 1}

# time complexity : O(n)
# space complexity = O(k), where k = number of distinct words (since dictionary stores only unique keys)