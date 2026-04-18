import logging
import inspect


class Loggen:

    @staticmethod
    def read_logger():
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            log_file = logging.FileHandler("C:\\Users\\aksha\\PycharmProjects\\PythonProject1\\Logs\\test_login_TC01.log")
            log_formater = logging.Formatter(
                " %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
            log_file.setFormatter(log_formater)
            logger.addHandler(log_file)

        return logger
