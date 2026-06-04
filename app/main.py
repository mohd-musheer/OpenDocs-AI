from app.agent.agent import (
    ask_docs
)


if __name__ == "__main__":

    while True:

        q = input(
            "\nQuestion: "
        )

        if q.lower() == "exit":
            break

        answer = ask_docs(
            q
        )

        print(
            "\nAnswer:\n"
        )

        print(answer)