from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.watch.owner import Owner
from mydb.auth.domain.watch.watch import Watch


class OwnerDao(GeneralDAO):
    _domain_type = Owner

    def find_watches_by_index(self, index: int):

        owner = self._session.query(Owner).filter(Owner.id == index).first()

        if owner:
            watches = self._session.query(Watch).filter(Watch.owner_id == owner.id).all()
            return [watch.put_into_dto() for watch in watches]
        return []
