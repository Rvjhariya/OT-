import ipaddress
import yaml




def is_private(ip):
try:
return ipaddress.ip_address(ip).is_private
except Exception:
return False




class RuleEngine:
def __init__(self, rules_path="rules/modbus.yml"):
with open(rules_path) as f:
self.rules = yaml.safe_load(f)


def eval_event(self, event):
alerts = []
for rule in self.rules:
if self._match(event, rule.get('when', {})):
alerts.append({
'rule_id': rule.get('id'),
'severity': rule.get('severity', 'medium'),
'title': rule.get('description') or rule.get('id'),
})
return alerts


def _match(self, event, when):
if when.get('proto') and event.get('proto') != when['proto']:
return False
if 'op_in' in when and event.get('op') not in set(when['op_in']):
return False
if when.get('src_not_private') and is_private(event.get('src','')):
return False
return True