from logs import log
import pyudev, threading
import evdev
import ctypes
import extractData as exd


def get_connected_usb_devices():

    '''get usb device'''
    devices = [evdev.InputDevice(device) for device in evdev.list_devices()]
    usb_devices = [device for device in devices if 'usb' in device.phys.lower()]
    return usb_devices

def wait_for_usb_connection_or_disconnection(connected=True):

    '''wait for usb ports updates'''
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    condition = threading.Condition()

    def device_event(observer, device):
        if (connected and device.action == 'add') or (connected and device.action == 'remove'):
            with condition:
                condition.notify()

    observer = pyudev.MonitorObserver(monitor, device_event)
    observer.start()

    with condition:
        condition.wait()

    observer.stop()
    

def terminate_thread(thread):

    '''Terminate a thread forcefully.'''
    if not thread.is_alive():
        return

    thread_id = thread.ident
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)
        log(log_file).info('Failed to terminate thread:', thread)
      
def reset_threads( old_threads_list, new_devices_list ):
    
    '''update thread list'''
    if old_threads_list:
        for thread in old_threads_list:
            terminate_thread(thread)
    
    new_threads_list = []
    
    for device in new_devices_list:
        thread = threading.Thread(target=exd.collectId, args=(device,))
        thread.start()
        new_threads_list.append(thread)
    
    return new_threads_list
