import logging


logging.basicConfig(level=logging.INFO, filename='bot_log_file.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')


def bot_logging(msg):
    logging.info(msg=msg)
