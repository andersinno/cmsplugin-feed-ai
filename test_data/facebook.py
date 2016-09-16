# -*- coding: utf-8 -*-
# flake8: noqa
"""
Example data got from facebook-sdk's GraphAPI.get_object method.
"""
PROFILE_NAME = "POTUS"

FACEBOOK_FEED = {
    'data': [{
        'message': "Heard some great news this morning that I wanted to share. We've made remarkable progress since I took office in the midst of the worst recession the country had seen in decades. Thanks to the grit and determination of the American people, we averted a second Great Depression, created more than 15 million private-sector jobs, and have seen real wages rising at their fastest rate in any business cycle since the 1970s.\n \nThat's remarkable progress, and today, we have more to report. Last year, across every race and age group, incomes rose and the poverty rate fell.  Folks' typical household income rose by $2,800 -- the single biggest one-year increase on record. We lifted 3.5 million people out of poverty -- the largest one-year drop in the poverty rate since 1968. And the pay gap for women shrank to its lowest level ever. All the work we've done is finally paying off in a big way.\n \nMore work remains to make sure we keep up with this progress in reducing inequality and growing wages for hardworking families. But today, it's worth taking stock of how far we've come together. This morning, I spoke with Jason Furman, who chairs my Council of Economic Advisers, to learn the latest on where our economy stands today.",
        'id': '424207551102424_533791280144050',
        'created_time': '2016-09-13T17:04:59+0000'
    }, {
        'story': 'President Obama added 2 new photos.',
        'message': "Every day, the White House receives thousands of letters from Americans across the country. Every night, I read 10 of them. These letters are my chance to hear directly from the people I serve -- and it's one of my favorite parts of the day.\n\nA few weeks ago, we launched a new way for people to share their thoughts with me, through Facebook Messenger. The first message from Facebook to reach my desk was from a young woman named Kathleen. Here's what I wrote back: http://go.wh.gov/TnMjbC \n\nKathleen, I'm so proud of everything you've accomplished. Keep it up!",
        'id': '424207551102424_526527297537115',
        'created_time': '2016-08-26T23:22:37+0000'
    }],
    'paging': {
        'previous': 'https://graph.facebook.com/v2.7/424207551102424/feed?limit=2&since=1473786299&access_token=abc|abcabc&__paging_token=enc_abc&__previous=1',
        'next': 'https://graph.facebook.com/v2.7/424207551102424/feed?limit=2&access_token=abc|abcabc&until=1472253757&__paging_token=enc_abc'
    }
}
