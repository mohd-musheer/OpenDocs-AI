from fastapi import APIRouter

from pydantic import BaseModel

from app.agent.agent import (
    ask_docs
)

router = APIRouter()


class AskRequest(
    BaseModel
):
    question: str


@router.post("/ask")
def ask(
    req: AskRequest
):

    answer = ask_docs(
        req.question
    )

    return {
        "answer": answer
    }