import subprocess

class IPTablesManager:
    """
    A class used to manage IPTables rules

    ...

    Methods
    -------
    block_ip(ip)
        Adds a new rule to IPTables to block the given IP address.

    unblock_ip(ip)
        Removes the rule blocking the given IP address from IPTables.

    list_blocked_ips()
        Returns a list of all IP addresses currently blocked by IPTables.
    """

    def block_ip(self, ip):
        """
        Adds a new rule to IPTables to block the given IP address.

        Parameters
        ----------
        ip : str
            The IP address to block.
        """
        subprocess.call(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

    def unblock_ip(self, ip):
        """
        Removes the rule blocking the given IP address from IPTables.

        Parameters
        ----------
        ip : str
            The IP address to unblock.
        """
        subprocess.call(["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"])

    def list_blocked_ips(self):
        """
        Returns a list of all IP addresses currently blocked by IPTables.

        Returns
        -------
        list
            A list of IP addresses currently blocked by IPTables.
        """
        output = subprocess.check_output(["iptables", "-L", "INPUT", "-v", "-n"])
        lines = output.split('\n')
        blocked_ips = [line.split()[7] for line in lines if 'DROP' in line]
        return blocked_ips