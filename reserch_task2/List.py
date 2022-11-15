
class List(list):
    """
        This class allows access list with 3 argument like that List[6,7,8].
        returns the item in the given position .
    """

    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, pos):
        row, arr, item = pos
        r = List(self.lst[row])
        a = List(r.lst[arr])
        return a.lst[item]



