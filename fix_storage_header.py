import re

with open('tech-storage-efficiency.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">OHRA-BOND™ GREEN + Local Mulch</th>',
              '<th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">The OHRA-BOND™ System (GREEN, GROW, CAL)</th>')

c = c.replace('<td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>&lt; 0.25 Pallets.</strong> (Approx. 10-15 lbs of highly concentrated polymer binder). Mulch is sourced locally as needed, keeping warehouse space free.</td>',
              '<td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>&lt; 0.5 Pallets.</strong> Even when stocking the full system (GREEN binder, GROW bio-stimulant, CAL conditioner), highly concentrated chemistry takes up minimal space. Mulch is sourced locally as needed.</td>')

c = c.replace('<td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Extremely Low.</strong> You are only paying freight for advanced chemistry, not bulky wood fiber or excess water weight.</td>',
              '<td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Extremely Low.</strong> You are only paying freight for advanced chemistry and concentrated soil biology, not bulky wood fiber or excess water weight.</td>')

c = c.replace('<td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Minimal.</strong> A single worker can easily carry enough binder for a multi-acre job in the cab of a truck.</td>',
              '<td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Minimal.</strong> A single worker can easily carry enough GREEN, GROW, and CAL for a multi-acre job in the cab of a truck.</td>')

with open('tech-storage-efficiency.html', 'w', encoding='utf-8') as f:
    f.write(c)
