class RedisQueue:
    """Simple Queue with Redis Backend"""

    def __init__(self, session_maker):
        print("Created Redis!")
        self.session_maker = session_maker
        self.key = '%s:%s' %("namespace", "name")

    def push_data(self, data):
        result = self.session_maker.rpush(self.key, data)
        return result

    def __next__(self):
        result = self.session_maker.lpop(self.key)
        if not result:
            raise StopIteration
        return result

    def __iter__(self):
        return self
