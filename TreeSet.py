import bisect


class TreeSet(object):
    """
    当添加新元素时，Treeset自动排序
    """
    def __init__(self, elements):
        self._treeset = []
        self.addAll(elements)

    def addAll(self, elements):
        for element in elements:
            if element in self: continue
            self.add(element)

    def add(self, element):
        if element not in self:
            bisect.insort(self._treeset, element)

    def __getitem__(self, num):
        return self._treeset[num]

    def __len__(self):
        return len(self._treeset)

    def clear(self):
        self._treeset = []

    def remove(self, element):
        try:
            self._treeset.remove(element)
        except ValueError:
            return False
        return True

    def __iter__(self):
        """
        为Treeset进行升序迭代
        """
        for element in self._treeset:
            yield element

    def __str__(self):
        return str(self._treeset)


    def __contains__(self, e):
        """
        通过bisect进行快速判断
        """
        try:
            return e == self._treeset[bisect.bisect_left(self._treeset, e)]
        except:
            return False

if __name__ == '__main__':
    ts = TreeSet([3,7,7,1,3])
    print(ts)
    re = ts.remove(3)
    print(ts)
    add = ts.add(4)
    print(ts)