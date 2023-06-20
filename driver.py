from rpyc import connect
#import toptica_laserskd

class Laser_driver:

    _connection = None

    #establishes connection
    def __init__(self, name, port_=9000):
        self._connection = connect(name, port=port_)


    #returns dict_item list of the laser DLC pro controllers
    def get_controller_items(self): #maybe rename
        return self._connection.root.controllers.items()
    
