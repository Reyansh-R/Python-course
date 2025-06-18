Indian = {"rice","dal", "roti","Chowmein","Dumplings",}
Chinese = {"rice","Chowmein","Dumplings","Spring rolls","Stir fry"}
print("Absolute cinema: ")
print(Indian)
print(Chinese) 
set(Indian)
set(Chinese)
print("Lets find out whats common :o")
Hakka = Indian.intersection(Chinese)
print(Hakka)
Hakka2 = Chinese.union(Indian)
print(Hakka2)