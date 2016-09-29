import sys

from django.core.management.base import BaseCommand
from django.core.validators import URLValidator, ValidationError
from django.utils import timezone as tz

from conferences.models import Conference, Ticket
from datetime import datetime
from json import loads
from urllib2 import urlopen, URLError

class Command(BaseCommand):
    help = "Loads tickets from Entrio"

    def add_arguments(self, parser):
        parser.add_argument('conference_id')
        parser.add_argument('source_url')

    def handle(self, *args, **options):
        conference_id = options.get('conference_id')
        source_url = options.get('source_url')
        self.validate_options(conference_id, source_url)

        print "Loading data from %s" % source_url
        data = self.fetch_entrio_data(source_url)

        print "Loaded %d tickets" % len(data)

        for item in data:
            ticket = self.to_ticket(item, conference_id)
            exists = Ticket.objects.filter(code=ticket.code, conference_id=conference_id).exists()
            if not exists:
                ticket.save()
                print "Created ticket #%s" % str(ticket)

        print "Done"

    def to_ticket(self, item, conference_id):
        purchased_at = item.get('purchase_datetime')
        if purchased_at:
            purchased_at = datetime.strptime(purchased_at, "%Y-%m-%d %H:%M:%S")
            purchased_at = tz.make_aware(purchased_at)

        twitter = item.get('Twitter').replace("@", "").replace("https://twitter.com/", "")

        parsed = {
            "conference_id": conference_id,
            "code": item.get('ticket_code'),
            "email": item.get('E-mail'),
            "first_name": item.get('First name'),
            "last_name": item.get('Last name'),
            "country": item.get('Country'),
            "twitter": twitter,
            "company": item.get('Company'),
            "category": item.get('ticket_category'),
            "promo_code": item.get('promo_discount_group'),
            "purchased_at": purchased_at,
            "dietary_preferences": item.get('Dietary preferences'),
        }

        # Convert None values to empty strings
        sanitized = {k: v if v is not None else '' for k, v in parsed.items()}

        return Ticket(**sanitized)

    def validate_options(self, conference_id, source_url):
        try:
            validator = URLValidator()
            validator(source_url)
        except ValidationError:
            print self.style.ERROR("Given source_url is not a valid URL.")
            sys.exit(1)

        try:
            conference_id = int(conference_id)
        except ValueError:
            print self.style.ERROR("Given conference_id must be an integer.")
            sys.exit(1)

        if not Conference.objects.filter(pk=conference_id).exists():
            print self.style.ERROR("Conference with id %d does not exist." % conference_id)
            sys.exit(1)

    def fetch_entrio_data(self, source_url):
        try:
            response = urlopen(source_url)
            return loads(response.read())
        except URLError as e:
            print(self.style.ERROR("Failed loading entrio data: %r" % e))