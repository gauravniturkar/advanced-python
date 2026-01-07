import timeit
import sys

# ============================================
# 1. CREATION TIME
# ============================================
print("=" * 50)
print("1. CREATION TIME")
print("=" * 50)

# List creation
list_time = timeit.timeit("x = [1, 2, 3, 4, 5]", number=1000000)
print(f"List creation: {list_time:.4f} seconds")

# Tuple creation
tuple_time = timeit.timeit("x = (1, 2, 3, 4, 5)", number=1000000)
print(f"Tuple creation: {tuple_time:.4f} seconds")

print(f"Tuple is {list_time / tuple_time:.2f}x faster for creation\n")

# ============================================
# 2. MEMORY USAGE
# ============================================
print("=" * 50)
print("2. MEMORY USAGE")
print("=" * 50)

list_obj = [1, 2, 3, 4, 5]
tuple_obj = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_obj)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_obj)} bytes")
print(f"Tuple uses {sys.getsizeof(list_obj) - sys.getsizeof(tuple_obj)} bytes less\n")

# ============================================
# 3. ITERATION
# ============================================
print("=" * 50)
print("3. ITERATION")
print("=" * 50)

list_data = list(range(1000))
tuple_data = tuple(range(1000))

# Iterate through list
list_iter = timeit.timeit(
    "for i in x: pass",
    setup="x = list(range(1000))",
    number=10000
)

# Iterate through tuple
tuple_iter = timeit.timeit(
    "for i in x: pass",
    setup="x = tuple(range(1000))",
    number=10000
)

print(f"List iteration: {list_iter:.4f} seconds")
print(f"Tuple iteration: {tuple_iter:.4f} seconds")
print(f"Tuple is {list_iter / tuple_iter:.2f}x faster for iteration\n")

# ============================================
# 4. INDEXING (ACCESS)
# ============================================
print("=" * 50)
print("4. INDEXING/ACCESS")
print("=" * 50)

list_access = timeit.timeit(
    "x[500]",
    setup="x = list(range(1000))",
    number=1000000
)

tuple_access = timeit.timeit(
    "x[500]",
    setup="x = tuple(range(1000))",
    number=1000000
)

print(f"List access: {list_access:.4f} seconds")
print(f"Tuple access: {tuple_access:.4f} seconds")
print(f"Tuple is {list_access / tuple_access:.2f}x faster for access\n")

# ============================================
# 5. CONCATENATION
# ============================================
print("=" * 50)
print("5. CONCATENATION")
print("=" * 50)

list_concat = timeit.timeit(
    "x = [1, 2, 3] + [4, 5, 6]",
    number=1000000
)

tuple_concat = timeit.timeit(
    "x = (1, 2, 3) + (4, 5, 6)",
    number=1000000
)

print(f"List concatenation: {list_concat:.4f} seconds")
print(f"Tuple concatenation: {tuple_concat:.4f} seconds")
print(f"Tuple is {list_concat / tuple_concat:.2f}x faster\n")

# ============================================
# 6. WHERE LISTS ARE FASTER - APPEND
# ============================================
print("=" * 50)
print("6. WHERE LISTS ARE FASTER - APPENDING")
print("=" * 50)

def list_append():
    x = []
    for i in range(100):
        x.append(i)

def tuple_append():
    x = ()
    for i in range(100):
        x = x + (i,)  # Creates new tuple each time

list_append_time = timeit.timeit(list_append, number=10000)
tuple_append_time = timeit.timeit(tuple_append, number=10000)

print(f"List append: {list_append_time:.4f} seconds")
print(f"Tuple append: {tuple_append_time:.4f} seconds")
print(f"List is {tuple_append_time / list_append_time:.2f}x faster for appending\n")


# List overhead
list_obj = []
print(f"Empty list: {sys.getsizeof(list_obj)} bytes")  # 56 bytes

# Tuple overhead
tuple_obj = ()
print(f"Empty tuple: {sys.getsizeof(tuple_obj)} bytes")  # 40 bytes

# Lists need more metadata for mutability

#============================================
#===================================================================
#============================================
#===================================================================




# Tuples can be used as dict keys (hashable)
my_dict = {
    (1, 2): "value"  # ✅ Works
}

# Lists cannot (not hashable)
my_dict = {
    [1, 2]: "value"  # ❌ TypeError: unhashable type: 'list'
}

# Hashing is fast operation for tuples
hash((1, 2, 3))  # Fast




#----------------------------------------
# when to use tuple
#----------------------------------------

# 1. Function returns (coordinates, RGB, database records)
def get_coordinates():
    return (10, 20)  # Tuple - won't change

# 2. Dictionary keys
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A"
}

# 3. Unpacking
x, y = get_coordinates()  # Fast with tuples

# 4. Constants
WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# 5. Multiple return values
def divide(a, b):
    return (a // b, a % b)  # quotient, remainder

# 6. Database records
user = (1, "Alice", "alice@email.com", 25)




#---------------------------------------------------
# When to Use List (Faster for Modifications)
#---------------------------------------------------



# 1. Building collections dynamically
numbers = []
for i in range(100):
    numbers.append(i)  # Fast with list

# 2. Modifying data
tasks = ["Task 1", "Task 2"]
tasks.append("Task 3")      # Fast
tasks.remove("Task 1")      # Fast
tasks.insert(0, "Urgent")   # Fast

# 3. Stack operations
stack = []
stack.append(1)  # Push
stack.pop()      # Pop

# 4. Queue operations (with deque, but list works)
queue = []
queue.append(1)      # Enqueue
queue.pop(0)         # Dequeue

# 5. Sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # In-place, fast



#============================================
# Additional Benchmarks
#============================================


# Test 1: Creating 1 million times
print("Creating 1 million times:")
print(f"List: {timeit.timeit('x = [1,2,3,4,5]', number=1000000):.4f}s")
print(f"Tuple: {timeit.timeit('x = (1,2,3,4,5)', number=1000000):.4f}s")
print()

# Test 2: Large data
size = 10000
print(f"Creating with {size} elements:")
print(f"List: {timeit.timeit(f'x = list(range({size}))', number=10000):.4f}s")
print(f"Tuple: {timeit.timeit(f'x = tuple(range({size}))', number=10000):.4f}s")
print()

# Test 3: Constant lookup
print("Looking up constant data:")
setup = """
lst = [1, 2, 3, 4, 5] * 100
tpl = tuple(lst)
"""
print(f"List: {timeit.timeit('lst[250]', setup=setup, number=1000000):.4f}s")
print(f"Tuple: {timeit.timeit('tpl[250]', setup=setup, number=1000000):.4f}s")