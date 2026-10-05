from src.hashing import hash_file
from src.storage import add_file
from src.history import file_history
from src.diff import diff

# add_file("src/test.txt")
print(file_history("src/test.txt"))
print(diff("src/test.txt"))