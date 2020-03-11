# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # set the ahs value to 5381
        hash_value = 5381
        # iterate over each char in the key
        for char in key:
        # set the hash value to the bit shift left by 5 of the hash value and sum of the hash value then add the value for the char 
            hash_value = ((hash_value << 5) + hash_value) + char
        # return the hash value
        return hash_value


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # overwrite matching key if key already exists
        if self.retrieve(key):
            self.remove(key)
        # get index and node at index
        index = self._hash_mod(key)
        node = self.storage[index]
        # no node 
        if node is None:
            self.storage[index] = LinkedPair(key,value)
            return
        # if collision loop through linked list
        while node is not None:
            prev = node
            node = node.next
            # last node added to .next
        prev.next = LinkedPair(key,value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash the key
        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None
        # loop through linked list
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # if no node
        if node is None:
            print("key cannot be found")
        else:
            # if node 
            removed = node.value
            # delete
            if prev is None:
                # or next possible match
                self.storage[index] = node.next
            else:
                # point to next node and remove
                prev.next = prev.next.next
            return removed


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        # loop through
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            # return if node
            return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create new storage
        newStorage = [None] * 2 * self.capacity

        # loop through and assign all nodes to new storage
        for i in range(self.capacity):
            newStorage[i] = self.storage[i]

        self.storage = newStorage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
