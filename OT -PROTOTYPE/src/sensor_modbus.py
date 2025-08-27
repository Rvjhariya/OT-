"""
Passive Modbus/TCP sensor (starter).
Requires: pyshark and system tshark.
"""
import pyshark
import json, time, ipaddress
from datetime import datetime
from collections import defaultdict


CAP_IFACE = "eth0" # change to your mirror interface or use a pcap file
BPF = "tcp port 502" # Modbus/TCP


assets = {}
last_seen = defaultdict(lambda: 0)




def enrich_asset(ip):
return {"vendor": None, "model": None, "firmware": None}




def handle_packet(pkt):
try:
ip = pkt.ip.src
dst = pkt.ip.dst
fc = int(pkt.modbus.func_code) if hasattr(pkt, 'modbus') and hasattr(pkt.modbus, 'func_code') else None
except Exception:
return


now = time.time()
for p in (ip, dst):
if p not in assets:
assets[p] = {"first_seen": now, "last_seen": now, "modbus": True, **enrich_asset(p)}
else:
assets[p]["last_seen"] = now


event = {
"ts": datetime.utcfromtimestamp(now).isoformat() + "Z",
"src": ip, "dst": dst, "proto": "modbus",
"op": f"fc_{fc}" if fc is not None else "unknown",
}
print(json.dumps({"type": "observation", **event}))


write_fcs = {5,6,15,16}
try:
if fc in write_fcs and not ipaddress.ip_address(ip).is_private:
alert = {
"ts": event["ts"],
"severity": "high",
"title": f"External Modbus write (FC {fc})",
"asset": dst, "src": ip, "rule": "modbus_external_write"
}
print(json.dumps({"type": "alert", **alert}))
except Exception:
main()