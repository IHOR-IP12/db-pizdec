from mydb.auth.dao import owner_dao
from mydb.auth.service.general_service import GeneralService


class OwnerService(GeneralService):
    _dao = owner_dao

    def find_watches_by_index(self, owner_id: int):
        return self._dao.find_watches_by_index(owner_id)
