class Paginator:
    def __init__(self, content: list, items_per_page: int):
        if not content:
            raise ValueError('Cannot pass empty list of content')
        else:
            self.content = content

        if num_pages < 1:
            raise ValueError('Number of pages must be 1 or more')
        else:
            self.items_per_page = items_per_page
