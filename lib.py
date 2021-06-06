class Paginator:
    def __init__(self, content: list, items_per_page: int):
        if not content:
            raise ValueError('Cannot pass empty list of content')
        else:
            self.content = content

        if items_per_page < 1:
            raise ValueError('Number of pages must be 1 or more')
        else:
            self.items_per_page = items_per_page

    def num_items(self):
        return len(self.content)
