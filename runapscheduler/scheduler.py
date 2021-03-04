from runapscheduler import scheduled_job

@scheduled_job('interval', seconds=5)
def test():
    print('asfas')