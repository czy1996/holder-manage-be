from models import Mongua
from datetime import datetime
from utils import log


class Board(Mongua):
    # 子类必须实现 _fields 类方法来定义字段
    # TODO expire
    @classmethod
    def _fields(cls):
        fields = [
            ('title', str, ''),
            ('content', str, ''),
        ]
        fields.extend(super()._fields())
        return fields


if __name__ == '__main__':
    # Board.new(title='公告', content='Hello')
    b = Board.find_one(id='1')
    log(b.json())