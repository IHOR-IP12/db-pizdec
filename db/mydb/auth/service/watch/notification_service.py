from http import HTTPStatus
from flask import abort
from mydb.auth.dao import notification_dao
from mydb.auth.service.general_service import GeneralService


class NotificationService(GeneralService):
    _dao = notification_dao

    def find_watches(self, notification_id: int):
        return self._dao.find_watches(notification_id)
