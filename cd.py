from abc import ABC, abstractmethod

class RentableItem(ABC):
    """Abstract class"""
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

class MovieCD(RentableItem):
    """Movie CD class"""
    def __init__(self, cd_id, title):
        self._cd_id = cd_id
        self._title = title
        self._is_borrowed = False
        self._borrower = None
        self._borrow_count = 0

    @property
    def cd_id(self):
        return self._cd_id

    @property
    def title(self):
        return self._title

    @property
    def is_borrowed(self):
        return self._is_borrowed

    @property
    def borrow_count(self):
        return self._borrow_count

    def borrow(self, customer):
        if not self._is_borrowed:
            self._is_borrowed = True
            self._borrower = customer
            self._borrow_count += 1
            return True
        return False

    def return_item(self):
        if self._is_borrowed:
            self._is_borrowed = False
            self._borrower = None
            return True
        return False

    def get_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Movie CD{self.cd_id} | {self.title} | Status: {status} | Borrowed {self.borrow_count} times"

    def is_available(self):
        return not self._is_borrowed
