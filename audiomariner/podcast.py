from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    name: str
    social_media: str

@dataclass
class Host(Person):
    biography: str

@dataclass
class Guest(Person):
    expertise: str


@dataclass
class Episode:
    title: str
    guests: List[Guest]
    duration: int  # duration in seconds
    release_date: str
    description: str

@dataclass
class Podcast:
    title: str
    host: Host
    description: str
    category: str
    episodes: List[Episode] = field(default_factory=list)