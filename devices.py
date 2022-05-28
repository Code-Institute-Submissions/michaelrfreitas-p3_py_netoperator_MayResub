"""
This module devices provided all devices and attributes for the system
"""


class ConfSwitchL2:
    """
    This class represent Device Switch L2 to take attributes of configuration.
    """

    def __init__(self):
        self.hostname = ''
        self.username = ''
        self.password = ''
        self.manager_vlan = ''
        self.manager_ip = ''
        self.manager_mask = ''
        self.primary_vlan = ''
        self.default_gateway = ''


class ConfSwitchL3:
    """
    This class represent Device Switch L3 to take attributes of configuration.
    """

    def __init__(self):
        self.hostname = ''
        self.username = ''
        self.password = ''
        self.manager_vlan = ''
        self.manager_ip = ''
        self.manager_mask = ''
        self.primary_int_vlan = ''
        self.primary_int_ip = ''
        self.primary_int_mask = ''
        self.default_gateway = ''


class ConfRouter:
    """
    This class represent Device Router to take attributes of configuration.
    """

    def __init__(self):
        self.hostname = ''
        self.username = ''
        self.password = ''
        self.interface_ip_inside = ''
        self.interface_mask_inside = ''
        self.interface_ip_outside = ''
        self.interface_mask_outside = ''
        self.default_ip = ''


class TshootDevices:
    """
    This class represent Device Layer3 to take attributes for
    Troubleshooting.
    """

    def __init__(self):
        self.ping_dest = ''
        self.status_vlan = ''
        self.routing_tab = ''
        self.proto_stat = ''
        self.mirror_config = ''
