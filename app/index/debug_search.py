from app.index.storage import load_tree


def keyword_search(query):

    tree = load_tree()

    results = []

    query = query.lower()

    for node in tree:

        score = 0

        title = node["title"].lower()
        content = node["content"].lower()

        score += title.count(query) * 10
        score += content.count(query)

        if score > 0:

            results.append(
                (
                    score,
                    node["title"],
                    node["url"]
                )
            )

    results.sort(reverse=True)

    return results[:10]


while True:

    q = input("\nSearch: ")

    results = keyword_search(q)

    print(f"\nFound {len(results)} results\n")

    for score, title, url in results:

        print("=" * 80)
        print(f"Score: {score}")
        print(f"Title: {title}")
        print(f"URL: {url}")