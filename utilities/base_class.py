import inspect
import logging
import pytest


@pytest.mark.usefixtures("invoke_browser")
class BaseClass:

    def logger_object(self):
        test_case_name = inspect.stack()[1][3]
        logger = logging.getLogger(test_case_name)
        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler("/home/georgi/PycharmProjects/forSales/utilities/logfile.log")
        formatter = logging.Formatter("%(asctime)s => %(levelname)s => %(name)s => %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

        return logger
