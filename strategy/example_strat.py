from run_strategy import AccountContext
from utils.logger_tools import get_general_logger
from utils import abspath
from config import STRATEGY_NAME

logger = get_general_logger(STRATEGY_NAME, path=abspath('logs'))

def main(context: AccountContext):
    logger.info(123)
    # logger.info(f'{context.positions}')