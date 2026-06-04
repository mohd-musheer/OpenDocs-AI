from app.index.storage import load_tree


def keyword_retrieve(query, top_k=5):

    tree = load_tree()

    query = query.lower()

    results = []

    for node in tree:

        score = 0

        title = node["title"].lower()
        content = node["content"].lower()

        words = query.split()

        for word in words:

            score += title.count(word) * 20
            score += content.count(word)

        if score > 0:

            results.append(
                (
                    score,
                    node
                )
            )

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        x[1]
        for x in results[:top_k]
    ]