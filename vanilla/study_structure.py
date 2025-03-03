from enum import Enum, auto


class StudyFolder(Enum):
    DATA = auto()
    TMP = auto()
    DOCS = auto()
    INPUT = auto()
    OUTPUT = auto()
    PRESENTATIONS = auto()
    RESOURCES = auto()
    SIM_RUNS = auto()
    NOTEBOOKS = auto()
    SCRIPTS = auto()
    SRC = auto()

    def __str__(self) -> str:
        return self.get_path()

    def get_path(self) -> str:
        paths = {
            StudyFolder.DATA: "data",
            StudyFolder.TMP: "non_versioned/_tmp",
            StudyFolder.DOCS: "non_versioned/docs",
            StudyFolder.INPUT: "non_versioned/input",
            StudyFolder.OUTPUT: "non_versioned/output",
            StudyFolder.PRESENTATIONS: "non_versioned/presentations",
            StudyFolder.RESOURCES: "non_versioned/resources",
            StudyFolder.SIM_RUNS: "non_versioned/sim_runs",
            StudyFolder.NOTEBOOKS: "notebooks",
            StudyFolder.SCRIPTS: "scripts",
            StudyFolder.SRC: "src"
        }
        return paths[self]
