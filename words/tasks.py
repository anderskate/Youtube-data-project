from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging
from .models import Key, Video
from .utils import get_video_links_from_youtube_api

import concurrent.futures
import time

logger = logging.getLogger('django')


@shared_task
def update_videos_for_all_keys():
    t1 = time.perf_counter()
    keys = Key.objects.all()
    for key in keys:
        links = get_video_links_from_youtube_api(key.word)
        logger.info(links)
        for link in links:
            Video.objects.get_or_create(
                key=key,
                url=link,
            )
    logger.info('Updated words from youtube API')
    t2 = time.perf_counter()

    logger.info(f'Finished in {t2 - t1} seconds')

