from django.conf import settings

from googleapiclient.discovery import build


def get_video_links_from_youtube_api(key, service='youtube', version='v3'):
    """Get video links from a Youtube API for a specific key

    Args:
        key (str): The key by which the search will occur.
        service (str): service that is used.
        version (str): Youtube API Version.
    """
    youtube = build(service, version, developerKey=settings.YOUTUBE_API_KEY)

    request = youtube.search().list(
        part='snippet',
        type='video',
        order='date',
        q=key,
    )

    response = request.execute()

    video_urls = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f'{settings.YOUTUBE_VIDEO_URL}?v={video_id}'
        video_urls.append(video_url)
    return video_urls
