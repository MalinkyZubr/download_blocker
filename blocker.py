import os
import time
import logging


class DownloadBlocker:
    def __init__(self, file_names: list[str], download_path: str, background: bool=False):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        if not background:
            self.logger.info("Started")
        self.names = file_names
        self.download_path = download_path
        os.chdir(self.download_path)

    def check_and_delete(self):
        while True:
            try:
                dir_list = os.listdir(".")
                if any(map(lambda v: v in self.names, dir_list)):
                    for file in self.names:
                        if file in dir_list:
                            os.remove(file)
                            self.logger.info(f"File {file} deleted successfully!")
                time.sleep(3)
            except Exception as e:
                self.logger.error(str(e))



if __name__ == "__main__":
    blocker=DownloadBlocker(['silly.bmp', 'silly.txt'], r'download_directory_here')
    blocker.check_and_delete()