from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventMixin
import logging

log = core.getLogger()
topology = []

class TopologyDetector(EventMixin):
    def __init__(self):
        core.openflow.addListeners(self)
        core.openflow_discovery.addListeners(self)
        log.info("Topology Detector & Forwarding Logic Started")

    def _handle_ConnectionUp(self, event):
        log.info("Switch %s has connected.", event.dpid)

    def _handle_LinkEvent(self, event):
        global topology
        link = tuple(sorted([event.link.dpid1, event.link.dpid2]))
        if event.added:
            if link not in topology:
                topology.append(link)
                log.info("Link Added: %s <-> %s", link[0], link[1])
        elif event.removed:
            if link in topology:
                topology.remove(link)
                log.info("Link Removed: %s <-> %s", link[0], link[1])
 
    def _handle_PacketIn(self, event):
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(event.parsed)
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        event.connection.send(msg)
        # log.debug("Flow rule installed for switch %s", event.dpid)

def launch():
    core.registerNew(TopologyDetector)
