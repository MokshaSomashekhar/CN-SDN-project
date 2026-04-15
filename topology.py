from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Create 2 switches and 2 hosts
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        # Connect switches (This link will be tested for failure)
        self.addLink(s1, s2)

topos = {'mytopo': (lambda: MyTopo())}