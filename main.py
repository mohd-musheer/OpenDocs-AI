from app.index.storage import load_tree

tree = load_tree()

print(f"Total Documents: {len(tree)}")

print("\nFirst Document:\n")

print(tree[0]["title"])
print(tree[0]["url"])
print(tree[0]["content"][:500])


from app.index.storage import load_tree

tree = load_tree()

total_chars = 0

for node in tree:
    total_chars += len(node["content"])

print(total_chars)


