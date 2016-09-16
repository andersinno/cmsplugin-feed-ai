# -*- coding: utf-8 -*-
from datetime import datetime

import pytest

from cmsplugin_feed_ai.feed import _fetch_profile_feed, get_feed_settings
from cmsplugin_feed_ai.providers.exceptions import FeedException
from cmsplugin_feed_ai.providers.facebook import FacebookFeedDisplayItem
from cmsplugin_feed_ai.providers.twitter import TwitterFeedDisplayItem
from test_data import facebook as facebook_test_data
from test_data import twitter as twitter_test_data


@pytest.mark.parametrize("service", ["facebook", "twitter"])
def test_get_feed_settings(service):
    feed_settings = get_feed_settings(service)
    assert feed_settings["profile_name"]


def test_get_twitter_feed_raises_without_proper_credentials():
    with pytest.raises(FeedException):
        _fetch_profile_feed("twitter", "test_profile", 1)


def test_get_facebook_feed_raises_without_proper_credentials():
    with pytest.raises(FeedException):
        _fetch_profile_feed("facebook", "test_profile", 1)


def test_feed_display_item_created_from_twitter_feed():
    """
    Test FeedDisplayItem properties with test data
    """
    feed_item = twitter_test_data.TWITTER_FEED[0]
    item = TwitterFeedDisplayItem(feed_item, twitter_test_data.PROFILE_NAME)
    assert item.source == "twitter"
    assert isinstance(item.created_at, datetime)
    assert item.profile_url == "https://twitter.com/POTUS"
    assert item.text_content == feed_item["text"]


def test_feed_display_item_created_from_facebook_feed():
    """
    Test FeedDisplayItem properties with test data
    """
    feed_item = facebook_test_data.FACEBOOK_FEED["data"][0]
    item = FacebookFeedDisplayItem(feed_item, facebook_test_data.PROFILE_NAME)
    assert item.source == "facebook"
    assert isinstance(item.created_at, datetime)
    assert item.profile_url == "https://facebook.com/POTUS"
    assert item.text_content == feed_item["message"]
