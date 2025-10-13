class GetEmissions:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, filters=None):
        return self.repo.list(filters)
