class SuperSort:
    """
        Sort list during 7 checking.
    """

    @classmethod
    def sort(cls, items):
        if len(items) != 5 or not isinstance(items, list):
            raise AttributeError("Invalid items provided.")

        if items[0] > items[1]:  # 1
            items[1], items[0] = items[0], items[1]

        if items[2] > items[3]:  # 2
            items[2], items[3] = items[3], items[2]

        if items[0] > items[2]:  # 3
            items[2], items[0] = items[0], items[2]
            items[2], items[1] = items[1], items[2]
        else:
            items[2], items[1] = items[1], items[2]
            items[2], items[3] = items[3], items[2]

        if items[1] > items[4]:  # 4
            if items[0] > items[4]:  # 5
                SuperSort.__swap(items, 4)
            else:
                SuperSort.__swap(items, 3)
        elif items[1] <= items[4]:  # 4
            if items[2] > items[4]:  # 5
                SuperSort.__swap(items, 2)

        if items[2] > items[4]:  # 6
            if items[1] > items[4]:  # 7
                SuperSort.__swap(items, 3)
            else:
                SuperSort.__swap(items, 2)
        else:
            if items[3] > items[4]:  # 7
                SuperSort.__swap(items, 1)

    @classmethod
    def __swap(cls, items: list, times: int = 0):
        if times > 3:
            raise ValueError("Swapping count must be less than 4")
        for i in range(times):
            items[4 - i], items[3 - i] = items[3 - i], items[4 - i]
