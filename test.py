import string


def create_index(filenames):
    dic = {}
    titles = {}
    for filename in filenames:
        with open(filename) as f:
            titles[filename] = f.readline().strip()
            f.seek(0)
            list1 = f.read().split()
            for i in list1:
                k = i.strip(string.punctuation).lower()
                if k not in dic:
                    dic[k] = [filename]
                elif filename in dic[k]:
                    continue
                else:
                    dic[k].append(filename)
    if dic.get("") is not None:
        del dic['']
    return filenames, dic, titles


def search(index, query):
    lst = []
    lst2 = []
    query = query.lower().split()
    for i in query:
        if index.get(i) is not None:
            lst.extend(index[i])
    for i in lst:
        if lst.count(i) == len(query) and i not in lst2:
            lst2.append(i)
    return lst2


a, b, c = create_index(["test1.txt", "test2.txt"])
d = search(b, "apple ball nope")
print(d)