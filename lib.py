class Paginator:
    def __init__(self, content: list, num_pages: int):
        if not content:
            raise ValueError('Cannot pass empty list of content')
        else:
            self.content = content

        if num_pages < 1:
            raise ValueError('Number of pages must be 1 or more')
        else:
            self.num_pages = num_pages
