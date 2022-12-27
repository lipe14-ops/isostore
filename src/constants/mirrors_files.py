from dataclasses import dataclass

@dataclass(frozen=True)
class MirrorsFilesConstant:
    PSP = "games-mirror-list-psp.csv"
    PS1 = "games-mirror-list-ps1.csv"
    PS2 = "games-mirror-list-ps2.csv"