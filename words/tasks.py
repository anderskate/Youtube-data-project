from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging
from .models import Key, Video
from .utils import get_video_links_from_youtube_api
import concurrent.futures

logger = logging.getLogger('django')


@shared_task
def update_videos_for_all_keys():
    """Update links to video keys received from Youtube API."""

    keys = Key.objects.all()
    key_words = [key.word for key in keys]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        urls_for_keys = executor.map(
            get_video_links_from_youtube_api,
            key_words,
        )
        results = dict(zip(keys, urls_for_keys))

        for key, urls in results.items():
            for url in urls:
                Video.objects.get_or_create(
                    key=key,
                    url=url,
                )
    logger.info(f'Update urls to words')
