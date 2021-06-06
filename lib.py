from math import ceil
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

    def num_pages(self):
        return ceil(self.num_items() / self.items_per_page) 

    def page_item_count(self, page_index):
        """
        Takes a zero-index page index and returns the number of items on that page
        """
        if self.num_items() % self.items_per_page == 0:
            return items_per_page
        elif page_index == self.num_pages() - 1:
            return self.num_items() % (self.num_pages() - 1)
        else:
            return self.items_per_page
