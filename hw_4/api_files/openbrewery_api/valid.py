from pydantic import BaseModel


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: str | None = None
    address_2: str | None = None
    address_3: str | None = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: str | None = None
    latitude: str | None = None
    phone: str | None = None
    website_url: str | None = None
    street: str | None = None


class Metadata(BaseModel):
    total: str
    page: str
    per_page: str
