"""Utility functions for Reddit scraper."""
from datetime import datetime
from typing import Any

import praw


def extract_media_urls(submission: praw.models.Submission) -> list[str]:
    """
    Extract media URLs from a Reddit submission.
    
    Args:
        submission: PRAW submission object
        
    Returns:
        List of media URLs (images, videos, etc.)
    """
    urls = []
    
    # Direct image/video URL
    if hasattr(submission, 'url') and submission.url:
        url = submission.url
        # Check if it's a media file
        if any(url.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.webm']):
            urls.append(url)
    
    # Reddit-hosted media
    if hasattr(submission, 'media') and submission.media:
        if 'reddit_video' in submission.media:
            video_url = submission.media['reddit_video'].get('fallback_url')
            if video_url:
                urls.append(video_url)
    
    # Gallery items
    if hasattr(submission, 'is_gallery') and submission.is_gallery:
        if hasattr(submission, 'media_metadata'):
            for item_id, item_data in submission.media_metadata.items():
                if 's' in item_data and 'u' in item_data['s']:
                    # Unescape HTML entities in URL
                    image_url = item_data['s']['u'].replace('&amp;', '&')
                    urls.append(image_url)
    
    # Preview images
    if hasattr(submission, 'preview') and 'images' in submission.preview:
        for image in submission.preview['images']:
            if 'source' in image and 'url' in image['source']:
                preview_url = image['source']['url'].replace('&amp;', '&')
                if preview_url not in urls:
                    urls.append(preview_url)
    
    return urls


def timestamp_from_utc(utc_timestamp: float) -> datetime:
    """
    Convert UTC timestamp to datetime object.
    
    Args:
        utc_timestamp: Unix timestamp in UTC
        
    Returns:
        datetime object
    """
    return datetime.fromtimestamp(utc_timestamp)


def safe_get_author(obj: Any) -> str:
    """
    Safely get author name from a Reddit object.
    
    Args:
        obj: PRAW object (submission, comment, etc.)
        
    Returns:
        Author username or '[deleted]' if not available
    """
    try:
        if hasattr(obj, 'author') and obj.author:
            return str(obj.author.name)
    except AttributeError:
        pass
    return '[deleted]'


def format_search_results(results: list[dict]) -> str:
    """
    Format search results for display.
    
    Args:
        results: List of result dictionaries
        
    Returns:
        Formatted string
    """
    if not results:
        return "No results found."
    
    output = []
    for i, result in enumerate(results, 1):
        output.append(f"\n{i}. {result.get('title', 'N/A')}")
        output.append(f"   Author: {result.get('author', 'N/A')}")
        output.append(f"   Subreddit: r/{result.get('subreddit', 'N/A')}")
        output.append(f"   Score: {result.get('score', 0)}")
        output.append(f"   URL: {result.get('url', 'N/A')}")
        output.append(f"   Timestamp: {result.get('timestamp', 'N/A')}")
    
    return "\n".join(output)
    return "\n".join(output)
