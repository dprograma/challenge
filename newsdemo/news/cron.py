from django_cron import CronJobBase, Schedule
import requests
from .models import DemoNewsModel


class NewsCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS,
                        retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'news.my_cron_job'    # a unique code

    def do(self):

        # external endpoint that returns list of ids
        NEWS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(NEWS_URL, headers=headers)

        # in order to trim the last element
        result = response.text.split(',')[1:len(response.text.split(','))-2]
        print("RESULT: ", result)
        # got this from API " 499287535 ] /n" --> reshaped to that below
        last = response.text.split(',')[-1]
        result.insert(len(result), last.strip().split()[0])  # "499287535"

        news = 400  # 100 downward/latest
        res = [int(id.strip())
               for id in result[news+1:]]  # list comprehension

        for id in res:
            news_id = DemoNewsModel(demonews=id)
            news_id.save()
