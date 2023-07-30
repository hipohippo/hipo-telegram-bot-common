import logging
import time
from typing import List

from telegraph import Telegraph


def publish_single(telegraph_publisher: Telegraph, title: str, html_content: str) -> str:
    response = telegraph_publisher.create_page(title=title, html_content=html_content)
    url = response["url"]
    logging.info(f"published to {url}")
    return url


def chop_str_group(str_list: List[str], chunk_size: int) -> List[int]:
    """

    :param html_content_group:  a list of str
    :return: list of index i0, i1, i2 such that, each string between neighbor index satisfies that
             len("".join(str_list[i0:i1])) <= chunk_size

             presumably the length of each string in the list is less than the chunk_size
    """
    cutoff_index = [0]
    prev_len = 0
    for idx, cur_str in enumerate(str_list):
        if prev_len + len(cur_str) > chunk_size:
            cutoff_index.append(idx)
            prev_len = len(cur_str)
        else:
            prev_len += len(cur_str)
    cutoff_index.append(len(str_list))
    return cutoff_index


def publish_chunk(telegraph_publisher: Telegraph, title: str, html_content_group: List[str]) -> List[str]:
    cutoff_index = chop_str_group(html_content_group, chunk_size=62000)
    url_list = []
    for idx in range(len(cutoff_index) - 1):
        url_list.append(
            publish_single(
                telegraph_publisher,
                title + f" ({idx+1}/{len(cutoff_index)-1})",
                "".join(html_content_group[cutoff_index[idx] : cutoff_index[idx + 1]]),
            )
        )
        time.sleep(10)
    return url_list
