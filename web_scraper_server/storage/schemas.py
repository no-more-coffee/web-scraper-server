from pydantic import BaseModel


class Apartment(BaseModel):
    id: int
    title: str
    image: str

    class Config:
        orm_mode = True
