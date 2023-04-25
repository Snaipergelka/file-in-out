import asyncio
from multiprocessing import Process, set_start_method

from dependency_injector.wiring import inject, Provide


from backend.containers import Container
from backend.database.db import Database
from backend.rqueue.rq import RedisQueue
from backend.src.processor import ProcessImage
from backend.src.storage import ImageStorage
from backend.config import get_settings
from backend import logger

logger = logger.get_logger(__name__)


@inject
def enqueue_image(rq: RedisQueue = Provide[Container.queue],
                  directory: str = None):
    """
    Push photos from directory to Redis queue.
    :param rq:
    :param directory:
    :return:
    """
    counter = 0
    for photo in ImageStorage.list(directory):
        rq.push_data(photo)
        counter += 1
    logger.info(f"Pushed {counter} images to queue!")


@inject
async def process_image(db: Database = Provide[Container.database],
                        queued_images: RedisQueue = Provide[Container.queue]):
    """
    Get size of an images from Redis queue and save to postgres
    :param db:
    :param queued_images:
    :return:
    """
    counter = 0
    for image in queued_images:
        size = ProcessImage(image).get_size()
        await db.create_instance(size)
        counter += 1
    logger.info(f"Processed and saved to Postgres {counter} images!")


if __name__ == "__main__":
    # need to pass injector container results to new processes
    set_start_method('fork')
    container = Container()
    container.wire(modules=[__name__])

    # start 1st process
    p1 = Process(target=enqueue_image,
                 kwargs={"directory": get_settings().TEST_DIRECTORY})
    p1.start()
    p1.join()

    # start 2nd process
    p2 = Process(target=lambda: asyncio.run(process_image()))
    p2.start()
    p2.join()
