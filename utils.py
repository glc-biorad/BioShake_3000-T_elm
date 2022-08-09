import serial
import sys
import glob
import socket

def get_serial_port_names():
    '''
    Obtains a list of serial port names.
    '''
    # Get the ports
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    # Return the results
    results = []
    for port in ports:
        try:
            sp = serial.Serial(port)
            sp.close()
            results.append(port)
        except (OSError, serial.SerialException):
            pass
    return results

def check_serial_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def flush_buffers(serial_port):
    serial_port.reset_input_buffer()
    serial_port.reset_output_buffer()