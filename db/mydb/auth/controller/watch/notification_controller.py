from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import notification_service


class NotificationController(GeneralController):
    _service = notification_service

    def find_watches(self, notification_id: int):
        return self._service.find_watches(notification_id)
