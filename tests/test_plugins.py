# -*- coding: utf-8 -*-
import pytest
from cms.api import add_plugin
from cms.models import Placeholder

from cmsplugin_feed_ai.cms_plugins import ProfileFeedPlugin


def init_plugin(plugin_type, lang="en", **plugin_data):
    """
    Creates a plugin attached into a placeholder
    Returns an instance of plugin_type
    """
    placeholder = Placeholder.objects.create(slot="test")
    return add_plugin(placeholder, plugin_type, lang, **plugin_data)


@pytest.mark.django_db
def test_feed_plugin_html():
    """
    Test feed plugin rendering doesn't raise errors.
    """
    plugin = init_plugin(ProfileFeedPlugin)
    html = plugin.render_plugin({})
    assert html
