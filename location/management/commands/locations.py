from django.core.management.base import BaseCommand

from location.models import Province, City, District


class Command(BaseCommand):
    help = 'Import all locations...'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        import json
        with open('location/management/commands/locations.json', encoding='utf-8') as file:
            lines = json.load(file)
        provinces = lines[0]
        cities = lines[1]
        districts = lines[2]

        bulk = []
        for province in provinces:
            p = Province(name=province[0], code=province[1])
            bulk.append(p)
            if len(bulk) > 20:
                Province.objects.bulk_create(bulk)
                bulk = []
        Province.objects.bulk_create(bulk)

        bulk = []
        for city in cities:
            province = Province.objects.get(name=city[2])
            c = City(name=city[0], code=city[1], province=province)
            bulk.append(c)
            if len(bulk) > 20:
                City.objects.bulk_create(bulk)
                bulk = []
        City.objects.bulk_create(bulk)

        bulk = []
        for district in districts:
            city = City.objects.get(name=district[2])
            d = District(name=district[0], code=district[1], city=city)
            bulk.append(d)
            if len(bulk) > 20:
                District.objects.bulk_create(bulk)
                bulk = []
        District.objects.bulk_create(bulk)
