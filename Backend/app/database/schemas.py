from fastapi import Form
from datetime import datetime, date
from pydantic import BaseModel, validator, EmailStr, constr
from pydantic.types import PositiveInt
from typing import Optional, List, Union


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls


class UserCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    password: str
    confirm_password: str
    birth: str
    email_enable: bool

    @validator('name', 'phone', 'email', 'password', 'confirm_password', 'birth')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Cannot be empty')
        return v

    @validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    birth: Optional[str] = None
    email_enable: Optional[bool] = None
    first_judging_permission: Optional[bool] = None
    second_judging_permission: Optional[bool] = None

    @validator('name', 'phone', 'birth')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Cannot be empty')
        return v


class User(BaseModel):
    id: int
    name: str
    phone: str
    email: EmailStr
    birth: str
    is_admin: bool
    email_enable: bool
    first_judging_permission: bool
    second_judging_permission: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserList(BaseModel):
    total: int
    users: list[User]


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str


class BoardCreate(BaseModel):
    name: str


class Board(BoardCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


@form_body
class PostCreate(BaseModel):
    title: str
    board_id: int
    content: str

    @validator('title', 'board_id', 'content')
    def not_empty(cls, v):
        if not v or (type(v) == type("") and not v.strip()):
            raise ValueError('Cannot be empty')
        return v


class PostEdit(BaseModel):
    title: str
    content: str
    board_id: int

    @validator('title', 'board_id', 'content')
    def not_empty(cls, v):
        if not v or (type(v) == type("") and not v.strip()):
            raise ValueError('Cannot be empty')
        return v


class PostUpdate(BaseModel):
    content: str


class Post(BaseModel):
    id: int
    title: str
    board_id: int
    content: str
    board: Board
    author: Optional[User] = None
    author_name: str
    files: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PostList(BaseModel):
    total: int
    posts: list[Post]


@form_body
class BannerCreate(BaseModel):
    name: str
    link: str
    year: int = 2023
    banner_end_at: datetime


class BannerEdit(BaseModel):
    name: str
    link: str
    banner_end_at: datetime


class Banner(BaseModel):
    id: int
    name: str
    filename: str
    link: str
    year: int = 2023
    banner_end_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class BannerList(BaseModel):
    total: int
    banners: list[Banner]


@form_body
class MouCreate(BaseModel):
    name: str
    link: str


class MouUpdate(BaseModel):
    name: str
    link: str


class Mou(BaseModel):
    id: int
    name: str
    link: str
    filename: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SponsorCreate(BaseModel):
    name: str
    phone: str
    address: str
    identification_number: str
    usage: str
    detail: str

    @validator('name', 'phone', 'address', 'identification_number', 'usage', 'detail')
    def not_empty(cls, v):
        if not v or (type(v) == type("") and not v.strip()):
            raise ValueError('Cannot be empty')
        return v


class SponsoringCompanyUpdate(BaseModel):
    name: str
    link: str
    year: int


class Sponsor(SponsorCreate):
    id: int
    user: Union[User, dict,  None]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


@form_body
class SponsoringCompanyCreate(BaseModel):
    name: str
    link: str
    year: int


class SponsoringCompany(BaseModel):
    id: int
    name: str
    filename: str
    link: str
    year: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SponsoringCompanyList(BaseModel):
    total: int
    sponsoring_companies: list[SponsoringCompany]


@form_body
class AdvisorCreate(BaseModel):
    name: str
    type: str
    description: str


class AdvisorUpdate(BaseModel):
    name: str
    type:  str
    description: str


class Advisor(BaseModel):
    id: int
    name: str
    type: str
    description: str
    filename: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AdvisorList(BaseModel):
    total: int
    advisors: list[Advisor]


@form_body
class PublicEventCreate(BaseModel):
    name: str
    english_name: str
    description: str
    start_date: date
    end_date: date
    join_start_date: date
    join_end_date: date


class PublicEventContentUpdate(BaseModel):
    name: str
    english_name: str
    description: str
    start_date: date
    end_date: date
    join_start_date: date
    join_end_date: date


class PublicEvent(BaseModel):
    id: PositiveInt
    name: str
    english_name: str
    description: str
    thumbnail_filename: Optional[str] = None
    start_date: date
    end_date: date
    join_start_date: date
    join_end_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PublicEventList(BaseModel):
    total: int
    events: list[PublicEvent]


class ParticipantCreate(BaseModel):
    name: str
    english_name: Optional[str] = None
    gender: Optional[str] = None
    birth: Optional[date] = None
    phone: str
    email: EmailStr
    organization_type: Optional[str] = None
    organization_name: str
    organization_english_name: Optional[str]
    job_position: str
    address: Optional[str] = None
    final_degree: Optional[str] = None
    engagement_type: Optional[str] = None
    participant_motivation: Optional[str] = None
    participant_type: Optional[str] = None
    interest_disease: Optional[str] = None
    interest_field: Optional[str] = None
    interest_field_detail: Optional[str] = None


class Participant(BaseModel):
    id: PositiveInt
    public_event_id: PositiveInt
    public_event: Optional[PublicEvent] = None
    name: str
    english_name: Optional[str] = None
    gender: Optional[str] = None
    birth: Optional[date] = None
    phone: str
    email: EmailStr
    organization_type: Optional[str] = None
    organization_name: str
    organization_english_name: Optional[str]
    job_position: str
    address: Optional[str] = None
    final_degree: Optional[str] = None
    engagement_type: Optional[str] = None
    participant_motivation: Optional[str] = None
    participant_type: Optional[str] = None
    interest_disease: Optional[str] = None
    interest_field: Optional[str] = None
    interest_field_detail: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ParticipantList(BaseModel):
    total: int
    participants: list[Participant]


class AdEmailCreate(BaseModel):
    user_id: Optional[PositiveInt] = None
    email: EmailStr
    subscribe: bool
    etc_info: Optional[str] = None



class AdEmail(BaseModel):
    id: PositiveInt
    user_id: Optional[PositiveInt] = None
    email: EmailStr
    subscribe: bool
    etc_info: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AdEmailList(BaseModel):
    total: int
    ad_emails: list[AdEmail]


@form_body
class AdEmailContent(BaseModel):
    email: Optional[EmailStr] = None
    title: str
    content: str


class HistoryCreate(BaseModel):
    title: str = ""
    content: str = ""


class HistoryUpdate(BaseModel):
    title: str = ""
    content: str = ""


class History(BaseModel):
    id: PositiveInt
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class HistoryList(BaseModel):
    total: int
    histories: List[History]


class SupportingStartupCreate(BaseModel):
    name: str
    content: str
    link: Optional[str] = None


class SupportingStartupUpdate(BaseModel):
    name: str
    content: str
    link: Optional[str] = None


class SupportingStartup(BaseModel):
    id: PositiveInt
    name: str
    content: str
    link: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SupportingStartupList(BaseModel):
    total: int
    supporting_startups: List[SupportingStartup]


class PrivateEventCreate(BaseModel):
    name: str
    join_start_date: date
    join_end_date: date
    description: str


class PrivateEventUpdate(BaseModel):
    name: str
    join_start_date: date
    join_end_date: date
    description: str


class PrivateEvent(BaseModel):
    id: PositiveInt
    name: str
    join_start_date: date
    join_end_date: date
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PrivateEventList(BaseModel):
    total: int
    events: list[PrivateEvent]


class PrivateParticipantCreate(BaseModel):
    event_id: PositiveInt
    name: str
    english_name: str
    gender: str
    birth: date
    phone: str
    email: EmailStr
    organization_type: str
    organization_name: str
    organization_english_name: str
    job_position: str
    address: str
    final_degree: str
    participant_motivation: str
    profile_filename: str
    zip_filename: str


class PrivateParticipant(BaseModel):
    id: PositiveInt
    user_id: Optional[PositiveInt] = None
    event_id: PositiveInt
    name: str
    english_name: str
    gender: str
    birth: date
    phone: str
    email: EmailStr
    organization_type: str
    organization_name: str
    organization_english_name: str
    job_position: str
    address: str
    final_degree: str
    participant_motivation: str
    profile_filename: str
    zip_filename: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PrivateParticipantList(BaseModel):
    total: int
    participants: List[PrivateParticipant]


@form_body
class JudgingEventCreate(BaseModel):
    name: str
    join_start_date: date
    join_end_date: date
    judging_1st_start_date: date
    judging_1st_end_date: date
    judging_2nd_start_date: date
    judging_2nd_end_date: date
    description: str


class JudgingEvent(BaseModel):
    id: PositiveInt
    name: str
    join_start_date: date
    join_end_date: date
    judging_1st_start_date: date
    judging_1st_end_date: date
    judging_2nd_start_date: date
    judging_2nd_end_date: date
    description: str
    thumbnail_filename: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class JudgingEventList(BaseModel):
    total: int
    events: list[JudgingEvent]


class JudgingParticipantCreate(BaseModel):
    event_id: PositiveInt
    name: str
    english_name: str
    gender: str
    birth: date
    phone: str
    email: EmailStr
    organization_type: str
    organization_name: str
    organization_english_name: str
    job_position: str
    address: str
    final_degree: str
    participant_motivation: str
    profile_filename: str
    zip_filename: str


class JudgingParticipant(BaseModel):
    id: PositiveInt
    user_id: Optional[PositiveInt] = None
    event_id: PositiveInt
    first_judging_result: object
    second_judging_result: object
    name: str
    english_name: str
    gender: str
    birth: date
    phone: str
    email: EmailStr
    organization_type: str
    organization_name: str
    organization_english_name: str
    job_position: str
    address: str
    final_degree: str
    participant_motivation: str
    profile_filename: str
    zip_filename: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class JudgingParticipantList(BaseModel):
    total: int
    participants: List[JudgingParticipant]


class JudgingResultCreate(BaseModel):
    judging_event_id: PositiveInt
    participant_id: PositiveInt
    nth: int
    technical_score1: int
    technical_score2: int
    technical_score3: int
    technical_score4: int
    technical_score5: int
    technical_score6: int
    marketability_score1: int
    marketability_score2: int
    marketability_score3: int
    marketability_score4: int
    business_score1: int
    business_score2: int
    business_score3: int
    business_score4: int
    business_score5: int
    business_score6: int
    business_score7: int
    business_score8: int
    other_score1: int
    other_comment: str = ""


class JudgingResult(JudgingResultCreate):
    id: PositiveInt
    user: Optional[User] = None
    total_score: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class JudgingResultList(BaseModel):
    total: int
    results: List[JudgingResult]


@form_body
class PopupCreate(BaseModel):
    title: str
    link: str
    popup_start_date: date
    popup_end_date: date


class PopupUpdate(BaseModel):
    title: str
    link: str
    popup_start_date: date
    popup_end_date: date


class Popup(BaseModel):
    id: PositiveInt
    title: str
    image_filename: str
    link: str
    popup_start_date: date
    popup_end_date: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PopupList(BaseModel):
    total: int
    popups: List[Popup]
