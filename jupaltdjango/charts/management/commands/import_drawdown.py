import csv
from ...models import Solution
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        Solution.objects.all().delete()

        with open("drawdown-stats.csv", "r+") as f:
            for index, row in enumerate(csv.reader(f)):
                if index == 0 or index == 83:
                    continue
                ss = Solution()
                ss.rank = row[0]
                ss.solution = row[1]
                ss.sector = row[2]
                ss.co2_reduction = row[3]
                ss.net_cost = row[4]
                ss.savings = row[5]
                ss.save()

