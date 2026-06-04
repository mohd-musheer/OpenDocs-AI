import json
from pathlib import Path

MEMORY_FILE = Path(
    "data/memory/session.json"
)

memory_store = {}


def load_memory():

    global memory_store

    if MEMORY_FILE.exists():

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            memory_store = json.load(f)


def save_memory(
    key,
    value
):

    memory_store[key] = value

    MEMORY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory_store,
            f,
            indent=2
        )


def get_memory():

    return memory_store


load_memory()