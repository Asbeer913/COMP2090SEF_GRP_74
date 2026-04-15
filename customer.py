class Customer:
    """Customer class"""
    def __init__(self, customer_id, name):
        self._customer_id = customer_id
        self._name = name
        self._borrowed_cds = []

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    def borrow_cd(self, cd):
        if cd.is_available() and self.can_borrow():
            if cd.borrow(self):
                self._borrowed_cds.append(cd)
                return True
        return False

    def return_cd(self, cd):
        if cd in self._borrowed_cds:
            if cd.return_item():
                self._borrowed_cds.remove(cd)
                return True
        return False

    def can_borrow(self):
        return len(self._borrowed_cds) < 3

    def get_borrowed_list(self):
        if not self._borrowed_cds:
            return "No borrowed Movie CDs currently"
        result = "\n".join([cd.get_details() for cd in self._borrowed_cds])
        return result
