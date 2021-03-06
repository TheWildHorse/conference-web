from random import shuffle

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse

from config.utils import get_active_event
from sponsors.choices import SPONSOR_TYPES
from sponsors.models import Sponsor
from usergroups.models import UserGroup


def navigation(request):
    return {
        "navigation": [
            ("Info", "/info/"),
            ("Venue", "/venue/"),
            # ("Talks", reverse('talks_list_talks')),
            # ("Schedule", reverse('schedule_list_schedule')),
            ("News", reverse('blog_list_posts')),
            # ("Jobs", reverse('jobs_list_jobs')),
            ("Code", "/code/"),
            ("Team", "/team/"),
        ]
    }


def sponsors(request):
    active = Sponsor.objects.active()

    diamond = active.filter(type=SPONSOR_TYPES.DIAMOND).order_by('id')
    track = active.filter(type=SPONSOR_TYPES.TRACK).order_by('id')
    foodanddrinks = active.filter(type=SPONSOR_TYPES.FOOD_AND_DRINKS).order_by('id')
    standard = active.filter(type=SPONSOR_TYPES.STANDARD).order_by('id')
    supporter = active.filter(type=SPONSOR_TYPES.SUPPORTER).order_by('id')
    mainmedia = active.filter(type=SPONSOR_TYPES.MAIN_MEDIA).order_by('order')
    media = active.filter(type=SPONSOR_TYPES.MEDIA).order_by('order')

    return {
        "sponsors": {
            'diamond': diamond,
            'track': track,
            'foodanddrinks': foodanddrinks,
            'standard': standard,
            'supporter': supporter,
            'mainmedia': mainmedia,
            'media': media
        }
    }


def usergroups(request):
    return {
        "usergroups": UserGroup.objects.order_by("name").filter(is_active=True)
    }


def event(request):
    event = get_active_event()

    return {
        'event': event,
        'cfp': event.get_cfp(),
    }


def webcamp(request):
    """Conference-related strings"""
    # TODO: move to database?

    abs_uri = request.build_absolute_uri

    return {
        "base_url": abs_uri('/').rstrip('/'),
        "links": {
            "sponsors_pdf": abs_uri('/media/wczg_2017_sponsors_brochure.pdf'),
            "volunteer_application": "http://goo.gl/forms/1LYfr3TEGs",
            "entrio": "https://www.entrio.hr/en/event/webcamp-zagreb-2017-4261",
            "facebook": "https://www.facebook.com/WebCampZagreb/",
            "twitter": "https://twitter.com/webcampzagreb/",
            "youtube": "https://www.youtube.com/user/WebCampZg",
            "linkedin": "https://www.linkedin.com/company-beta/6397140/",
            "github": "https://github.com/webcampzg",
            "google_plus": "https://plus.google.com/+WebcampzgOrgHR",
        },
        "webcamp": {
            "og_image": {
                "url": abs_uri(static("images/og-image.png")),
                "width": 1200,
                "height": 630
            }
        }
    }


def team(request):
    team = [
        {
            "name": "Luka Mužinić",
            "image": "images/team/luka.jpg",
            "twitter": "lmuzinic",
            "job": "Glorious leader"
        },
        {
            "name": "Maja Trepšić",
            "image": "images/team/maja.jpg",
            "twitter": "",
            "job": "Speakers",
        },
        {
            "name": "Martina Dumančić",
            "image": "images/team/martina.jpg",
            "twitter": "",
            "job": "Procurement",
        },
        {
            "name": "Nikola Plejić",
            "image": "images/team/nikola.jpg",
            "twitter": "nikolaplejic",
            "job": "Sponsor wrangler",
        },
        {
            "name": "Filip Gjurin",
            "image": "images/team/filip.jpg",
            "twitter": "FilipGjurin",
            "job": "Graphic design",
        },
        {
            "name": "Ivan Habunek",
            "image": "images/team/ivan.jpg",
            "twitter": "ihabunek",
            "job": "Tech support"
        },
    ]

    shuffle(team)

    return {
        "team": team
    }
