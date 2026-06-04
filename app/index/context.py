from app.index.storage import load_tree


def get_context(node_ids):

    tree = load_tree()

    contexts = []

    for node in tree:

        if node["node_id"] in node_ids:

            contexts.append(
                f"""
Title:
{node['title']}

Content:
{node['content']}
"""
            )

    return "\n\n".join(contexts)