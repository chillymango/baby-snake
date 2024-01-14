from typing import Any

from pydantic import BaseModel, Field


class GameDto(BaseModel):
    id: str
    ruleset: dict[str, Any]
    map: str
    timeout: float
    source: str


class RulesetDto(BaseModel):
    name: str
    version: str
    settings: dict[str, Any]


class RulesetSettingsDto(BaseModel):
    foodSpawnChance: float
    minimumFood: 1
    hazardDamagePerTurn: float
    royale: dict[str, float]
    squad: dict[str, Any]


class Position(BaseModel):
    x: int
    y: int


class BattleSnakeDto(BaseModel):
    id: str
    name: str
    health: float
    body: list[Position] = Field(default_factory=list)
    latency: str
    head: Position
    length: int
    shout: str
    squad: 1
    customizations: dict[str, Any]


class BoardDto(BaseModel):
    height: int
    width: int
    food: list[Position]
    hazards: list[Position]
    snakes: list[BattleSnakeDto]
