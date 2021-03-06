import logging
import os
import sys

logger = logging.getLogger(__name__)


def run(env: str):
    return 'DONE'

if __name__ == '__main__':
    ENV = os.environ.get('env', 'local')

    logging.basicConfig(
        level=logging.getLevelName(logging.INFO),
        handlers=[logging.StreamHandler(sys.stdout)],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    logger.info(f'***** STARTING JOB *****')
    run(env=ENV)
    logger.info(f'***** FINISHED JOB *****')
