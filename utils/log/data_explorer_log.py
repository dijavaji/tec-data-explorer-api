import logging
import time

class DataExplorerLog():

    _instance = None
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[logging.StreamHandler()])

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DataExplorerLog, cls).__new__(cls)
        return cls._instance

    def getLog(self):
        return self._instance

    def info(self, parameter):
        return logging.info(parameter)

    def debug(self, parameter):
        return logging.debug(parameter)

    def warning(self, parameter):
        return logging.warning(parameter)

    def error(self, parameter):
        return logging.error(parameter)

    def critical(self, parameter):
        return logging.critical(parameter)

    def print_time(self, start_time, end_time):
        logging.debug(
            f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")

if __name__ == "__main__":
    start_time = time.time()
    s1 = DataExplorerLog()
    s1.getLog().debug("Esto es un mensaje de DEBUG")
    s1.info("Esto es un mensaje de INFO")
    s1.warning("Esto es un mensaje de WARNING")
    s1.error("Esto es un mensaje de ERROR")
    s1.critical("Esto es un mensaje de CRITICAL")
    end_time = time.time()
    s1.print_time(start_time, end_time)