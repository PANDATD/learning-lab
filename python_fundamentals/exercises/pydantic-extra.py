from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class WeatherAPI(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")
    air_quality: int
    city: str


class BankAccount(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid")
    account_number: str = Field(
        min_length=12,
        max_length=12,
    )
    account_type: str


class EventLog(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="allow")
    event_id: int
    event_type: str


"""
BaseModel defines `model_config` as a class-level configuration.

Annotating it with `ClassVar[ConfigDict]`
tells static type checkers that this attribute
belongs to the class rather than individual instances.
"""


if __name__ == "__main__":
    print("=" * 60)
    print("EventLog (extra='allow')")
    print("=" * 60)

    try:
        event = EventLog(
            event_id=0,
            event_type="Error",
            event_description="ValidationError",
        )

        print(event.model_dump())

    except ValidationError as exc:
        print(exc)

    print()

    print("=" * 60)
    print("WeatherAPI (extra='ignore')")
    print("=" * 60)

    try:
        pune_weather = WeatherAPI(
            city="Pune",
            air_quality=10,
            humidity="low",  # type: ignore
        )

        print(pune_weather.model_dump())

    except ValidationError as exc:
        print(exc)

    print()

    print("=" * 60)
    print("BankAccount (extra='forbid')")
    print("=" * 60)

    try:
        bank_account = BankAccount(
            account_number="123456789012",
            account_type="Savings",
            is_admin=True,  # type: ignore
        )

        print(bank_account.model_dump())

    except ValidationError as exc:
        print(exc)
