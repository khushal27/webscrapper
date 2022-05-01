
class logFile:
    import logging
    logging.basicConfig(filename='web.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
