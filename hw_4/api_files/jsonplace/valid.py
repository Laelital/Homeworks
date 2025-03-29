from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    body: str
    userId: int


class Todos(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str
