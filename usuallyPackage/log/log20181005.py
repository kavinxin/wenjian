import logging
import datetime
import logging.handlers
logger=logging.getLogger("mylogger");
logger.setLevel(logging.DEBUG);
rf_hander=logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7,atTime=None);
rf_hander.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"));

r_hander=logging.FileHandler("error.log");
r_hander.setLevel(logging.ERROR);
r_hander.setFormatter((logging.Formatter("%(asctime)s===%(levelname)s===%(message)s")));

logger.addHandler(rf_hander);
logger.addHandler(r_hander);

logger.debug("this is a debug logg!");
logger.error("this is a error log!");
logger.critical("this is a criticla log!");
logger.info("this is a info log!");
logger.warning("this is a waring log!");
