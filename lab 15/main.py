from fastapi import FastAPI, HTTPException, Depends
import wikipedia
from pydantic import BaseModel, Field, PositiveInt
from typing import Optional

app = FastAPI()


class TitleSearchParams(BaseModel):
    word: str
    num: Optional[PositiveInt] = Field(None)


class PageRequest(BaseModel):
    title: str


class PageResponse(BaseModel):
    title: str
    references: list[str]
    categories: list[str]


@app.get("/titles/{word}")
def search_titles(params: TitleSearchParams = Depends()) -> list[str]:
    return (wikipedia.search(params.word, results=params.num)
            if params.num else wikipedia.search(params.word))


@app.post("/page/")
def get_page(request: PageRequest) -> PageResponse:
    try:
        page = wikipedia.page(request.title)
    except wikipedia.DisambiguationError as e:
        raise HTTPException(
            400, detail=f"Уточните запрос. Варианты: {e.options[:5]}")
    except wikipedia.PageError:
        raise HTTPException(404, detail="Страница не найдена")
    except Exception as e:
        raise HTTPException(500, detail=f"Ошибка сервера: {str(e)}")

    return PageResponse(
        title=page.title,
        references=page.references,
        categories=page.categories
    )
