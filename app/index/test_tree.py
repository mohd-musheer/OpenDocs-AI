from app.pageindex_engine.retrieve import retrieve
import json

query = "How do I create middleware in FastAPI?"

docs, confidence = retrieve(query)

print("\nCONFIDENCE:")
print(confidence)

print("\nDOCS FOUND:")
print(len(docs))

for i, doc in enumerate(docs):

    print("\n" + "=" * 80)
    print(f"DOC {i+1}")
    print("=" * 80)

    print(type(doc))

    print(
        json.dumps(
            doc,
            indent=2
        )[:3000]
    )