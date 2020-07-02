"""Set Does not allowd duplicate"""

s = {1,5,'hey whats up'}
print(s)

s.update([76,98])
print(s)

s.remove(5)

print(s)

f = frozenset(s)
# we can't update or delete in frozen set
#f.update(12)