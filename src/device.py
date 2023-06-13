from logs import log
import pyudev, threading
import evdev


def get_connected_usb_devices():
    devices = [evdev.InputDevice(device) for device in evdev.list_devices()]
    usb_devices = [device for device in devices if 'usb' in device.phys.lower()]
    return usb_devices

def wait_for_usb_connection_or_disconnection(connected=True):
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