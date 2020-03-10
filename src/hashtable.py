import hashlib
# '''
# Linked List hash table key/value pair
# '''

# this is a full, complete linked list, this is all we need for chaining


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# our hash table that has capacity buckets that accept string keys...emulating the functionality of allocating memory, by making use of a python list


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    # capacity is how much we can fit in our hash table

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

# leading underscore means do not use it outside of the class...its private

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hashlib.sha256(key.encode())

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    # hash mod calls hash and returns the capacity
    # to get an index

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with 
        Linked List Chaining.

        Fill this in.
        '''
        # first we turn the key into an index in our array
        index = self._hash_mod(key)
        # check for an error
        if self.storage[index]:
            print("ERROR: Key in use")
        # key becomes our value
        else:
            self.storage[index] = value

        #     hash_table = LinkedPair(key, value)
        #     hash_table = self.storage[index]

        #     self.storage[index] = hash_table
        #     return
        # else:
        #     print('Collision')
        #     return

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # first we turn the key into an index in our array
        index = self._hash_mod(key)
        # were not printing the error this time,
        # we set self.storage to none first
        if self.storage[index]:
            self.storage[index] = None
        # then print the error since its removed
        else:
            print("ERROR: Key not found")

        # hash_table = self.storage[index]

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # once again get the index
        index = self._hash_mod(key)
        # then were just returning storage at the index,
        # it returns none if key isnt found since we've
        # initialized our storage array and set
        # everything to None to begin with
        return self.storage[index]

        # hash_table = self.storage[index]
        # if hash_table:
        #     return hash_table.value
        # return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # pave our way for a new storage
        old_storage = self.storage.copy()
        # double the capacity
        self.capacity = self.capacity * 2
        # make new storage (none * capacity)
        self.storage = [None] * self.capacity
        # make our for each loop
        for bucket_item in old_storage:
            # re-insert everything in new key
            self.insert(bucket_item)

        # self.capacity *= 2
        # new_storage = [None] * self.capacity
        # for i in range(self.count):
        #     new_storage[i] = self.storage[i]
        # self.storage = new_storage


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
