from rpyc import connect
#import toptica_laserskd

class Laser_driver:

    _connection = None

    #establishes connection
    def __init__(self, name, port_=9000):
        self._connection = connect(name, port=port_)

