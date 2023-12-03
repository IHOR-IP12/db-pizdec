from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import owner_service


class OwnerController(GeneralController):
    _service = owner_service

    _service = owner_service

    def find_watches_by_index(self, owner_id: int):
        return self._service.find_watches_by_index(owner_id)