from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


item = "zeef jhay rivera sorelia"
counter = Counter(item)
# print(counter)
# common element
print(counter.most_common())

print(list(counter.elements()))

Point = namedtuple('Point', 'x,y') # liked a struct on other language
pt1 = Point(1, 2)


df1 = defaultdict(int)
df1['a'] = 1