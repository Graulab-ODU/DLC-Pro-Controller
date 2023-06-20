from rpyc import connect

class Laser:

    _controller = None

    # establishes connection
    def __init__(self, name, controller, port_=9000):
        self._controller = connect(name, port=port_).root.controllers[controller]

    # returns the emission status of the chose laser
    def get_emission(self, laser_number=None):
        if (laser_number==None or (laser_number in (1,2)) == False):
            laser = ''
        else:
            laser = f'laser{laser_number}.'
        return self._controller.get(f'{laser}emission')


    # returns the voltage offset of the chose laser
    def get_voltage_offset(self, laser_number):
        assert(laser_number in (1, 2))
        return self._controller.get(f'laser{laser_number}.scan.offset')


    # Sets a laser to a chosen laser offset
    def set_voltage_offset(self, laser_number, voltage_offset):
        assert(laser_number in (1, 2))
        return self._controller.set(f'laser{laser_number}.scan.offset', voltage_offset)