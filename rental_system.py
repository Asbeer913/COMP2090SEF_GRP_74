from cd import MovieCD
from customer import Customer
class RentalSystem:
    """Movie CD Rental System"""
    def __init__(self):
        self._cds = []
        self._customers = {}
        self.next_cd_id = 101
        self.next_customer_id = 1

    def add_cd(self, title):
        cd = MovieCD(self.next_cd_id, title)
        self._cds.append(cd)
        self.next_cd_id += 1
        print(f"Movie CD added: {cd.get_details()}")
        return cd

    def list_all_cds(self):
        print("\n=== All Movie CDs ===")
        if not self._cds:
            print("No Movie CDs yet")
            return
        for cd in self._cds:
            print(cd.get_details())

    def get_available_cds(self):
        print("\n=== Available Movie CDs ===")
        available = [cd for cd in self._cds if cd.is_available()]
        if not available:
            print("No Movie CDs available right now")
            return
        for cd in available:
            print(cd.get_details())

    def add_customer(self, name):
        cust = Customer(f"C{self.next_customer_id}", name)
        self._customers[cust.customer_id] = cust
        self.next_customer_id += 1
        print(f"Customer added: {cust.name} (ID: {cust.customer_id})")
        return cust

    def get_customer(self, cust_id):
        return self._customers.get(cust_id)

    def borrow(self, cust_id, cd_id):
        customer = self.get_customer(cust_id)
        cd = next((c for c in self._cds if c.cd_id == cd_id), None)
        if not customer or not cd:
            print("Customer or Movie CD does not exist")
            return False
        if customer.borrow_cd(cd):
            print(f"{customer.name} successfully borrowed {cd.title}")
            return True
        print("Borrow failed (limit reached or already borrowed)")
        return False

    def return_cd(self, cust_id, cd_id):
        customer = self.get_customer(cust_id)
        cd = next((c for c in self._cds if c.cd_id == cd_id), None)
        if not customer or not cd:
            print("Customer or Movie CD does not exist")
            return False
        if customer.return_cd(cd):
            print(f"{customer.name} successfully returned {cd.title}")
            return True
        print("Return failed")
        return False

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _heapify_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.heap[i][0] > self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def insert(self, cd):
        self.heap.append((cd.borrow_count, cd))
        self._heapify_up(len(self.heap) - 1)

    def get_top_n(self, n):
        if not self.heap:
            return []
        heap_copy = self.heap[:]
        result = []
        for _ in range(min(n, len(heap_copy))):
            max_item = max(heap_copy, key=lambda x: x[0])
            result.append(max_item[1])
            heap_copy.remove(max_item)
        return result


def heap_sort_cds(cds):
    if not cds:
        return []
    return sorted(cds, key=lambda cd: cd.borrow_count, reverse=True)
