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

    def num_items(self) -> int:
        return len(self.content)

    def num_pages(self) -> int:
        return ceil(self.num_items() / self.items_per_page) 

    def page_item_count(self, page_index: int) -> int:
        """
        Takes a zero-index page index and returns the number of items on that page
        """
        if self.num_items() % self.items_per_page == 0:
            return self.items_per_page
        elif page_index == self.num_pages() - 1:
            return self.num_items() % (self.num_pages() - 1)
        else:
            return self.items_per_page

    def item_page_index(self, item_index: int) -> int: 
        """
        Takes in a zero-index item index and returns a zero-index page index on which the item appears
        """
        mods = divmod(item_index + 1, self.items_per_page)
        if mods[1] == 0:
            return mods[0] - 1
        else: 
            return mods[0]
