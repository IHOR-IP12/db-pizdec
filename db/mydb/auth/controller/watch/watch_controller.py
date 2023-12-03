from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import watch_service


class WatchController(GeneralController):
    _service = watch_service

    def find_notifications(self, watch_id: int):
        return self._service.find_notifications(watch_id)
