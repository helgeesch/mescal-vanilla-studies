import pathlib
from dataclasses import dataclass

from vanilla.study_structure import StudyFolder


@dataclass
class PathManager:
    """Manages paths for a study project, providing easy access to standard folders.

    This class helps maintain consistent access to the study's folder structure.
    It validates the existence of the study folder and its subfolders,
    creating them if necessary.

    Args:
        study_path: Path to the study root folder. Can be relative or absolute.

    Raises:
        ValueError: If the provided study folder does not exist.

    Examples:
        >>> pm = PathManager("./my_study")
        >>> input_file = pm.input("data.csv")
        >>> output_path = pm.output("results.csv")
        >>> custom_path = pm.any_path("custom", "path.txt")
    """
    study_path: str

    def __post_init__(self) -> None:
        self._base_path = pathlib.Path(self.study_path).resolve()
        if not self._base_path.exists():
            raise ValueError(f"Study folder does not exist: {self._base_path}")

        self._ensure_folders()

    def _ensure_folders(self) -> None:
        for folder in StudyFolder:
            folder_path = self._base_path / folder.get_path()
            folder_path.mkdir(parents=True, exist_ok=True)

    def _get_path(self, folder: StudyFolder, filename: str = "") -> pathlib.Path:
        path = self._base_path / folder.get_path()
        if filename:
            path = path / filename
        return path

    def ensure_dir(self, path: pathlib.Path | str) -> pathlib.Path:
        """
        Ensures a directory exists, creating it if necessary.
        Path must be within the study base path. Use any_path() to construct
        paths relative to the study base.

        Args:
            path: Path to ensure exists

        Returns:
            The ensured path
        """
        if isinstance(path, str):
            path = pathlib.Path(path)

        if not str(path).startswith(str(self._base_path)):
            raise ValueError(
                f"Path '{path}' is not within study base path '{self._base_path}'. \n"
                f"This method is only intended for paths inside the study base path. \n"
                "Use any_path() to construct paths relative to the study base."
            )

        path.mkdir(parents=True, exist_ok=True)
        return path

    def data(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.DATA, filename)

    def tmp(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.TMP, filename)

    def docs(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.DOCS, filename)

    def input(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.INPUT, filename)

    def output(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.OUTPUT, filename)

    def presentations(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.PRESENTATIONS, filename)

    def resources(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.RESOURCES, filename)

    def sim_runs(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.SIM_RUNS, filename)

    def scripts(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.SCRIPTS, filename)

    def src(self, filename: str = "") -> pathlib.Path:
        return self._get_path(StudyFolder.SRC, filename)

    def any_path(self, *parts: str) -> pathlib.Path:
        """Constructs an arbitrary path within the study folder.

        Args:
            *parts: Path components to join to the study base path

        Returns:
            Complete path combining the base path and provided parts
        """
        return self._base_path.joinpath(*parts)
