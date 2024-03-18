from pydantic import BaseModel

class StudentNumber(BaseModel):
    studentNumber: str


class Name(BaseModel):
    name: str


class Date(BaseModel):
    date: str


class Serial(BaseModel):
    serial: str


class City(BaseModel):
    city: str


class Province(BaseModel):
    province: str


class Address(BaseModel):
    address: str


class Post(BaseModel):
    post: str


class Phone(BaseModel):
    phone: str


class Landline(BaseModel):
    landline: str


class Faculty(BaseModel):
    faculty: str


class Field(BaseModel):
    field: str


class Marriage(BaseModel):
    marriage: str


class Code(BaseModel):
    code: str