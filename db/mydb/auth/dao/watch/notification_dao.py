from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.notification import Notification, watch_notification


class NotificationDao(GeneralDAO):
    _domain_type = Notification

    def find_watches(self, notification_id: int):
        session = self._session()

        watches_ids = (
            session.query(watch_notification.c.watch_id)
            .filter(watch_notification.c.watch_id == notification_id)
            .all()
        )

        watch_ids = [watch_id for (watch_id,) in watches_ids]

        from mydb.auth.domain.watch.watch import Watch
        watches = session.query(Watch).filter(Watch.id.in_(watch_ids)).all()

        return [watch.put_into_dto() for watch in watches]
