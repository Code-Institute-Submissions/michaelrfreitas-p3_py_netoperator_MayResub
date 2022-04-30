"""
This module devices provided all devices and attributes for the system
"""


class ConfSwitchL2:
    """
    This class represent Device Switch L2 to take attributes of configuration.
    """

    def __init__(self, hostname, username, password, manager_vlan, manager_ip,
                 manager_mask, primary_vlan, default_gateway):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.manager_vlan = manager_vlan
        self.manager_ip = manager_ip
        self.manager_mask = manager_mask
        self.primary_vlan = primary_vlan
        self.default_gateway = default_gateway


class ConfSwitchL3:
    """
    This class represent Device Switch L3 to take attributes of configuration.
    """

    def __init__(self, hostname, username, password, manager_vlan, manager_ip,
                 manager_mask, primary_int_vlan, primary_int_ip,
                 primary_int_mask, default_gateway):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.manager_vlan = manager_vlan
        self.manager_ip = manager_ip
        self.manager_mask = manager_mask
        self.primary_int_vlan = primary_int_vlan
        self.primary_int_ip = primary_int_ip
        self.primary_int_mask = primary_int_mask
        self.default_gateway = default_gateway


class ConfRouter:
    """
    This class represent Device Router to take attributes of configuration.
    """

    def __init__(self, hostname, username, password, interface_inside,
                 interface_ip_inside, interface_mask_inside, interface_outside,
                 interface_ip_outside, interface_mask_outside, protocol,
                 default_ip):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.interface_inside = interface_inside
        self.interface_ip_inside = interface_ip_inside
        self.interface_mask_inside = interface_mask_inside
        self.interface_outside = interface_outside
        self.interface_ip_outside = interface_ip_outside
        self.interface_mask_outside = interface_mask_outside
        self.protocol = protocol
        self.default_ip = default_ip


class TshootLayer3Devices:
    """
    This class represent Device Layer3 to take attributes for
    Troubleshooting.
    """

    def __init__(self, ping_destination, status_vlan, check_mask, check_ip,
                 status_interface, destination_ip, check_mac_table,
                 check_arp_table, status_routing_table, protocol_status,
                 mirror_config):
        self.ping_destination = ping_destination
        self.status_vlan = status_vlan
        self.check_mask = check_mask
        self.check_ip = check_ip
        self.status_interface = status_interface
        self.destiation_ip = destination_ip
        self.check_mac_table = check_mac_table
        self.check_arp_table = check_arp_table
        self.status_routing_table = status_routing_table
        self.protocol_status = protocol_status
        self.mirror_config = mirror_config


class TshootSwitchL2:
    """
    This class represent Device Switch L2 to take attributes for
    Troubleshooting.
    """

    def __init__(self, ping_destination, status_vlan, check_mask, check_ip,
                 destination_ip, check_mac_table, check_arp_table,
                 mirror_config):
        self.ping_destination = ping_destination
        self.status_vlan = status_vlan
        self.check_mask = check_mask
        self.check_ip = check_ip
        self.destiation_ip = destination_ip
        self.check_mac_table = check_mac_table
        self.check_arp_table = check_arp_table
        self.mirror_config = mirror_config
