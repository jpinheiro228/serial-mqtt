import logging

log_format_default = "[%(asctime)s] - %(name)-30s - %(levelname)-8s - %(message)s"
log_format_debug = "[%(asctime)s] - %(name)-30s - %(levelname)-8s - %(funcName)s - %(message)s"
loglevel_dict = {"INFO": logging.INFO,
                 "DEBUG": logging.DEBUG,
                 "ERROR": logging.ERROR,
                 "CRITICAL": logging.CRITICAL,
                 "WARNING": logging.WARNING,
                 "NOTSET": logging.NOTSET}


def default_logger(logger_name="MyLog", level="INFO", silent=False, log_file=None):
    log = logging.getLogger(logger_name)

    log.setLevel(level=level)

    if log.getEffectiveLevel() == logging.DEBUG:
        formatter = logging.Formatter(log_format_debug)
    else:
        formatter = logging.Formatter(log_format_default)

    if not silent:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        log.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

    return log


if __name__ == "__main__":
    l = default_logger(silent=False, level="DEBUG", log_file="test.log")
    l.log(level=l.getEffectiveLevel(), msg="----- Starting Logger -----")
    l.log(level=l.getEffectiveLevel(), msg=f"LOG LEVEL = {l.getEffectiveLevel()}")
    l.debug("Hello world (DEBUG)")
    l.info("Hello world (INFO)")
    l.warning("Hello world (WARNING)")
    l.error("Hello world (ERROR)")
    l.critical("Hello world (CRITICAL)")
