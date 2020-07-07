import unittest


class TestLinkedListMethods(unittest.TestCase):
    llist = LinkedList()
    llist.add_at_start("A")
    llist.add_at_start("B")
    llist.add_at_start("C")
    llist.add_at_end("X")
    print(llist)
    llist.del_from_start()
    llist.add_after(0, "Q")
    llist.add_before(2, "NEW")
    llist.del_from_end()
    print(llist)
    llist.add_at_end("END")
    llist.add_at_start("START")
    llist.del_after(1)
    llist.del_before(3)
    print(llist)
    # output from this should be:
    # Linked List: C -> B -> A -> X
    # Linked List: B -> Q -> NEW -> A
    # Linked List: START -> B -> A -> END
