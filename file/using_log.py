import logging

if __name__ == '__main__':

    logger = logging.getLogger("main")

    
    print("do not set log level ")
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")

    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.INFO)

    print("set log level ")
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
