from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.notification import watch_notification, Notification
from mydb.auth.domain.watch.watch import Watch


class WatchDao(GeneralDAO):
    _domain_type = Watch

    def find_notifications(self, watch_id: int):
        session = self._session()

        notifications_ids = (
            session.query(watch_notification.c.watch_id)
            .filter(watch_notification.c.watch_id == watch_id)
            .all()
        )

        notification_ids = [notification_id for (notification_id,) in notifications_ids]

        notifications = session.query(Notification).filter(Notification.id.in_(notification_ids)).all()

        return [notification.put_into_dto() for notification in notifications]


