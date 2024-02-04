from Python_292120_Timing.model.da.database_manager import DatabaseManager
from Python_292120_Timing.model.entity.visit import Visit


class VisitDa(DatabaseManager):
    def find_by_timing(self, timing):
        self.make_engine()
        result = self.session.query(Visit).filter(Visit.timing == timing)
        return result
