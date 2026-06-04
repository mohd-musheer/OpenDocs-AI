from app.index.storage import load_tree

tree = load_tree()

print("Documents:", len(tree))

print("\nFirst document:\n")

print(tree[0].keys())

print(tree[0]["title"])
print(tree[0]["url"])

print(tree[0]["content"][:500])