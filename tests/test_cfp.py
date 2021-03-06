import pytest

from datetime import date, timedelta

from django.urls import reverse

from cfp.models import CallForPaper, PaperApplication, AudienceSkillLevel
from config.utils import get_active_event
from tests.factories import ApplicantFactory, CallForPaperFactory, UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def applicant(user):
    return ApplicantFactory(user=user)


@pytest.fixture
def active_cfp():
    event = get_active_event()
    begin_date = date.today() - timedelta(1)
    end_date = date.today() + timedelta(1)
    return CallForPaperFactory(event=event, begin_date=begin_date, end_date=end_date)


@pytest.fixture
def past_cfp():
    event = get_active_event()
    begin_date = date.today() - timedelta(10)
    end_date = date.today() - timedelta(5)
    return CallForPaperFactory(event=event, begin_date=begin_date, end_date=end_date)


@pytest.mark.django_db
def test_cfp_announcement_view_active(client, active_cfp):
    url = reverse('cfp_announcement')

    response = client.get(url)
    content = response.content.decode(response.charset)

    assert response.status_code == 200
    assert "Submit a talk" in content
    assert active_cfp.announcement in content


@pytest.mark.django_db
def test_cfp_announcement_view_inactive(client, past_cfp):
    url = reverse('cfp_announcement')

    response = client.get(url)
    content = response.content.decode(response.charset)

    assert response.status_code == 200
    assert "The CFP is now closed" in content
    assert past_cfp.announcement in content


@pytest.mark.django_db
def test_cfp_announcement_view_when_no_cfp_exists(client):
    url = reverse('cfp_announcement')

    response = client.get(url)
    content = response.content.decode(response.charset)

    assert response.status_code == 200
    assert CallForPaper.objects.count() == 0
    assert "There are no active calls for paper" in content


@pytest.mark.django_db
def test_GET_create_application(user, applicant, client, active_cfp):
    url = reverse('application_create')

    response = client.get(url)
    content = response.content.decode(response.charset)

    # User needs to log in for this page
    assert response.status_code == 302
    assert response.url.startswith(reverse('account_login'))

    client.login(username=user.email, password='webcamp')
    response = client.get(url)
    content = response.content.decode(response.charset)

    assert response.status_code == 200
    assert "Submit your talk for {}".format(active_cfp.event.title) in content
    assert active_cfp.description in content


@pytest.mark.django_db
def test_GET_create_application_when_cfp_is_inactive(user, applicant, client, past_cfp):
    url = reverse('application_create')

    # Forbidden when not logged in
    response = client.get(url)
    content = response.content.decode(response.charset)

    assert response.status_code == 403
    assert "Call for proposals is not active" in content

    # Also forbidden when logged in
    client.login(username=user.email, password='webcamp')
    response = client.get(url)
    content = response.content.decode(response.charset)

    assert response.status_code == 403
    assert "Call for proposals is not active" in content


@pytest.mark.django_db
def test_POST_create_application(user, applicant, client, active_cfp):
    url = reverse('application_create')

    client.login(username=user.email, password='webcamp')

    assert PaperApplication.objects.count() == 0

    data = {
        "title": "Hello dolly",
        "about": "Hello dolly",
        "abstract": "Hello dolly",
        "skill_level": "10",
        "duration": "25",
        "extra_info": "Hello dolly",
        "about_applicant": applicant.about + "mod", # Changed to test the change
        "biography": applicant.biography + "mod",
        "speaker_experience": applicant.speaker_experience + "mod",
        "image": "",
    }

    response = client.post(url, data)

    assert response.status_code == 302
    assert response.url == reverse('user_profile')
    assert PaperApplication.objects.count() == 1

    pa = PaperApplication.objects.first()
    assert pa.applicant == applicant

    assert pa.title == data['title']
    assert pa.about == data['about']
    assert pa.abstract == data['abstract']
    assert pa.skill_level == AudienceSkillLevel.objects.get(pk=data['skill_level'])
    assert pa.duration == data['duration']
    assert pa.extra_info == data['extra_info']

    applicant.refresh_from_db()

    assert applicant.about == data['about_applicant']
    assert applicant.biography == data['biography']
    assert applicant.speaker_experience == data['speaker_experience']
