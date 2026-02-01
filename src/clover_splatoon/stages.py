from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional, List
from src.clover_splatoon.tools import parse_iso_z


"""
涂地
"""
@dataclass(frozen=True)
class Image:
    url: str

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Image":
        return cls(url=d["url"])


@dataclass(frozen=True)
class VsStage:
    vsStageId: int
    name: str
    image: Image
    id: str

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "VsStage":
        return cls(
            vsStageId=int(d["vsStageId"]),
            name=d["name"],
            image=Image.from_dict(d["image"]),
            id=d["id"],
        )


@dataclass(frozen=True)
class VsRule:
    name: str
    rule: str
    id: str

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "VsRule":
        return cls(
            name=d["name"],
            rule=d["rule"],
            id=d["id"],
        )


@dataclass(frozen=True)
class RegularMatchSetting:
    isVsSetting: str
    typename: str
    vsStages: List[VsStage]
    vsRule: VsRule

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "RegularMatchSetting":
        stages = [VsStage.from_dict(x) for x in d.get("vsStages", [])]
        return cls(
            isVsSetting=d.get("__isVsSetting", ""),
            typename=d.get("__typename", ""),
            vsStages=stages,
            vsRule=VsRule.from_dict(d["vsRule"]),
        )


@dataclass(frozen=True)
class RegularScheduleItem:
    startTime: datetime
    endTime: datetime
    regularMatchSetting: Optional[RegularMatchSetting]
    festMatchSettings: Optional[Any]

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "RegularScheduleItem":
        rms = d.get("regularMatchSetting")
        return cls(
            startTime=parse_iso_z(d["startTime"]),
            endTime=parse_iso_z(d["endTime"]),
            regularMatchSetting=RegularMatchSetting.from_dict(rms) if rms else None,
            festMatchSettings=d.get("festMatchSettings"),
        )


"""
打工
"""
@dataclass(frozen=True)
class Image:
    url: str

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Image":
        return cls(url=d["url"])


@dataclass(frozen=True)
class Boss:
    name: str
    id: str

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Boss":
        return cls(name=d["name"], id=d["id"])


@dataclass(frozen=True)
class CoopStage:
    name: str
    thumbnailImage: Image
    image: Image
    id: str

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "CoopStage":
        return cls(
            name=d["name"],
            thumbnailImage=Image.from_dict(d["thumbnailImage"]),
            image=Image.from_dict(d["image"]),
            id=d["id"],
        )


@dataclass(frozen=True)
class Weapon:
    splatoon3ink_id: str
    name: str
    image: Image

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Weapon":
        return cls(
            splatoon3ink_id=d.get("__splatoon3ink_id", ""),
            name=d["name"],
            image=Image.from_dict(d["image"]),
        )


@dataclass(frozen=True)
class CoopNormalSetting:
    typename: str
    isCoopSetting: str
    boss: Boss
    coopStage: CoopStage
    weapons: List[Weapon]

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "CoopNormalSetting":
        return cls(
            typename=d.get("__typename", ""),
            isCoopSetting=d.get("__isCoopSetting", ""),
            boss=Boss.from_dict(d["boss"]),
            coopStage=CoopStage.from_dict(d["coopStage"]),
            weapons=[Weapon.from_dict(w) for w in d.get("weapons", [])],
        )


@dataclass(frozen=True)
class CoopScheduleItem:
    startTime: datetime
    endTime: datetime
    setting: CoopNormalSetting
    king_salmonid_guess: Optional[str]

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "CoopScheduleItem":
        return cls(
            startTime=parse_iso_z(d["startTime"]),
            endTime=parse_iso_z(d["endTime"]),
            setting=CoopNormalSetting.from_dict(d["setting"]),
            king_salmonid_guess=d.get("__splatoon3ink_king_salmonid_guess"),
        )


"""
蛮颓
"""
@dataclass(frozen=True)
class BankaraMatchSetting:
    isVsSetting: str
    typename: str
    vsStages: List[VsStage]
    vsRule: VsRule
    bankaraMode: str  # "CHALLENGE" / "OPEN"

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "BankaraMatchSetting":
        return cls(
            isVsSetting=d.get("__isVsSetting", ""),
            typename=d.get("__typename", ""),
            vsStages=[VsStage.from_dict(x) for x in d.get("vsStages", [])],
            vsRule=VsRule.from_dict(d["vsRule"]),
            bankaraMode=d["bankaraMode"],
        )


@dataclass(frozen=True)
class BankaraScheduleItem:
    startTime: datetime
    endTime: datetime
    bankaraMatchSettings: List[BankaraMatchSetting]
    festMatchSettings: Optional[Any]

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "BankaraScheduleItem":
        return cls(
            startTime=parse_iso_z(d["startTime"]),
            endTime=parse_iso_z(d["endTime"]),
            bankaraMatchSettings=[
                BankaraMatchSetting.from_dict(x)
                for x in d.get("bankaraMatchSettings", [])
            ],
            festMatchSettings=d.get("festMatchSettings"),
        )