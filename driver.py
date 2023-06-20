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
    
# returns the emission status of the chose laser
    def get_emission(self, controller, laser_number=None):
        if (laser_number==None or (laser_number in (1,2)) == False):
            laser = ''
        else:
            laser = f'laser{laser_number}.'
        return self._connection.root.controllers[controller].get(f'{laser}emission')


    # returns the voltage offset of the chose laser
    def get_voltage_offset(self, controller, laser_number):
        assert(laser_number in (1, 2))
        return self._connection.root.controllers[controller].get(f'laser{laser_number}.scan.offset')


    # Sets a laser to a chosen laser offset
    def set_voltage_offset(self, controller, laser_number, voltage_offset):
        assert(laser_number in (1, 2))
        return self._connection.root.controllers[controller].set(f'laser{laser_number}.scan.offset', voltage_offset)
    

