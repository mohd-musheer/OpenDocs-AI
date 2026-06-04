from app.pageindex_engine.storage import load_all_trees

# ============================================================
# TEXT EXTRACTION
# ============================================================

def extract_text(tree):

    parts = []

    def walk(node):

        if not isinstance(node, dict):
            return

        for field in (
            "title",
            "summary",
            "prefix_summary",
            "text"
        ):

            value = node.get(field)

            if value:
                parts.append(str(value))

        for child in node.get(
            "nodes",
            []
        ):
            walk(child)

    parts.append(
        tree.get(
            "doc_name",
            ""
        )
    )

    parts.append(
        tree.get(
            "doc_description",
            ""
        )
    )

    for root in tree.get(
        "structure",
        []
    ):
        walk(root)

    return "\n".join(parts)


# ============================================================
# NODE MATCHING
# ============================================================

def get_best_nodes(
    tree,
    query_words,
    top_nodes=3
):

    candidates = []

    def walk(node):

        if not isinstance(node, dict):
            return

        title = str(
            node.get(
                "title",
                ""
            )
        )

        text = str(
            node.get(
                "text",
                ""
            )
        )

        summary = str(
            node.get(
                "summary",
                ""
            )
        )

        content = (
            title
            + "\n"
            + summary
            + "\n"
            + text
        ).lower()

        score = 0

        for word in query_words:

            if len(word) < 3:
                continue

            score += content.count(word)

            if word in title.lower():
                score += 10

        if score > 0:

            candidates.append(
                (
                    score,
                    {
                        "title": title,
                        "text": text[:2000]
                    }
                )
            )

        for child in node.get(
            "nodes",
            []
        ):
            walk(child)

    for root in tree.get(
        "structure",
        []
    ):
        walk(root)

    candidates.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        node
        for _, node
        in candidates[:top_nodes]
    ]


# ============================================================
# MAIN RETRIEVER
# ============================================================

def retrieve(
    question,
    top_k=5
):

    trees = load_all_trees()

    print(
        f"\nTOTAL TREES LOADED: {len(trees)}"
    )

    query = question.lower()

    query_words = set(
        query.split()
    )

    results = []

    for tree in trees:

        doc_name = tree.get(
            "doc_name",
            ""
        ).lower()

        text = extract_text(
            tree
        ).lower()

        score = 0

        # --------------------------------
        # exact phrase boost
        # --------------------------------

        if query in text:
            score += 100

        if query in doc_name:
            score += 200

        # --------------------------------
        # keyword scoring
        # --------------------------------

        for word in query_words:

            if len(word) < 3:
                continue

            score += text.count(word)

            if word in doc_name:
                score += 20

        if score > 0:

            matched_nodes = get_best_nodes(
                tree,
                query_words
            )

            results.append(
                (
                    score,
                    {
                        "doc_name": tree.get(
                            "doc_name"
                        ),

                        "doc_description":
                        tree.get(
                            "doc_description",
                            ""
                        ),

                        "matched_nodes":
                        matched_nodes
                    }
                )
            )

    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    docs = [
        item[1]
        for item in results[:top_k]
    ]

    confidence = (
        results[0][0]
        if results
        else 0
    )

    print(
        "\nTOP RESULTS:"
    )

    for score, doc in results[:10]:

        print(
            score,
            doc["doc_name"]
        )

    return docs, confidence