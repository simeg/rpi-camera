import logging
import time
import os
from time import sleep
from picamera import PiCamera

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run():
    try:
        logger.info('Initialising snap script')
        camera = PiCamera()

        logger.info('Snapping picture')
        camera.start_preview()
        sleep(5)

        timestamp = int(time.time())
        current_folder = os.path.dirname(os.path.realpath(__file__))
        file_path = '{}/images/{}.png'.format(current_folder, str(timestamp))

        camera.capture(file_path)
        camera.stop_preview()
        logger.info('Picture successfully snapped')

    except Exception as e:
        logger.exception('Could not snap image due to exception')


if __name__ == '__main__':
    run()

