# List vs Tuple Performance Comparison

## 📊 Quick Reference Table

| Operation | List | Tuple | Winner | Why? |
|-----------|------|-------|--------|------|
| **Creation** | Slower | **Faster** ⚡ | Tuple | Immutable = less overhead |
| **Memory** | More | **Less** 💾 | Tuple | No growth space needed |
| **Access (indexing)** | Fast | **Slightly faster** | Tuple | Less struct complexity |
| **Iteration** | Fast | **Slightly faster** | Tuple | Optimized by interpreter |
| **Slicing** | Fast | **Slightly faster** | Tuple | Same reason |
| **Append** | **Fast** ⚡ | Very slow | List | Tuple creates new object |
| **Insert** | **Fast** ⚡ | Very slow | List | Tuple creates new object |
| **Remove** | **Fast** ⚡ | Very slow | List | Tuple creates new object |
| **Concatenation** | Slower | **Faster** | Tuple | Both create new objects |
| **Contains (`in`)** | Same | Same | Tie 🤝 | O(n) for both |
| **Count** | Same | Same | Tie 🤝 | O(n) for both |
| **Index** | Same | Same | Tie 🤝 | O(n) for both |

