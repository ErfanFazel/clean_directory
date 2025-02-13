import shutil 
from pathlib import Path 
from src.data import DATA_DIR
from src.utils.io import read_json
from loguru import logger
from typing import Union
import sys
class OrgenizeFiles:
    """
    This class is used to orgenize files in a directory by
    moving files into directories based on extension
    """
    def __init__(self):
        ext_dirs = read_json(DATA_DIR / "extensions.json")
        self.extentions_dest = {}
        for dir_name,ext_list in ext_dirs.items():
            for ext in ext_list:
                self.extentions_dest[ext] = dir_name
    def __call__(self,directory:Union[str,Path]):
        """
        Orgenize files in the directory by moving them to 
        sub directories based on extension
        """
        directory = Path(directory)
        if not directory.exists():
            raise FileNotFoundError(f"{self.directory} does not exist")
        logger.info(f"Orgenizing files in {directory}...")
        file_extensions = []
        for file_path in directory.iterdir():
            #ignored directories
            if file_path.is_dir():
                continue
            #ignored hidden files
            if file_path.name.startswith('.'):
                continue
            file_extensions.append(file_path.suffix)
            if file_path.suffix not in self.extentions_dest:
                DEST_DIR = self.directory / "other"
            else:
                DEST_DIR = self.directory / self.extentions_dest[file_path.suffix]
            logger.info(f"Moving {file_path} to {DEST_DIR}...")
            DEST_DIR.mkdir(exist_ok=True)
            shutil.move(str(file_path),DEST_DIR)

if __name__ == "__main__":
    org_file = OrgenizeFiles()
    org_file(directory=sys.argv[1])
    logger.info("Done")