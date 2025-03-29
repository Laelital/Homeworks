from pydantic import BaseModel


class BreedsList(BaseModel):
    message: dict
    status: str


class BreedsImage(BaseModel):
    message: list[str] | str
    status: str
