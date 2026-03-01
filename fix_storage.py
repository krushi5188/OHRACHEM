import re

with open('tech-storage-efficiency.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's completely remove the generic table that was just injected.
start_str = "<h2>Comparative Analysis: OHRA-BOND™ GREEN vs. Conventional Alternatives</h2>"
end_str = "</div>\n<h2>Frequently Asked Questions (FAQ)</h2>"

# We'll just replace the entire block with a perfectly tailored one.
if start_str in c:
    start_idx = c.find(start_str)
    # The end of the injected table should be the </div> right before the FAQ
    end_idx = c.find("<h2>Frequently Asked Questions", start_idx)

    if end_idx != -1:
        old_block = c[start_idx:end_idx]

        tailored_table = """<h2>Comparative Logistics & Storage: OHRA-BOND™ vs. BFM</h2>
                <p>To truly understand the warehouse impact, we must compare the storage requirements of OHRA-BOND™ GREEN against Pre-Packaged Bonded Fiber Matrices (BFMs) and conventional Agricultural Guar. The data below illustrates the dramatic difference in footprint required to store materials capable of covering 10 acres of moderate slope.</p>

                <div style="overflow-x: auto; margin-top: 30px; margin-bottom: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <table style="width: 100%; border-collapse: collapse; background-color: #fff; text-align: left;">
                        <thead>
                            <tr style="background-color: var(--primary); color: #fff;">
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Logistical Metric (per 10 Acres)</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">OHRA-BOND™ GREEN + Local Mulch</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Pre-Packaged BFM</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Conventional Guar Gum</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Warehouse Footprint (Pallets Required)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>&lt; 0.25 Pallets.</strong> (Approx. 10-15 lbs of highly concentrated polymer binder). Mulch is sourced locally as needed, keeping warehouse space free.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>15 to 20 Pallets.</strong> (Pre-mixed 50lb bags of wood fiber and binder). Consumes massive floor space and vertical racking.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>1 to 2 Pallets.</strong> (Approx. 400-600 lbs of agricultural powder). Still requires sourcing separate mulch.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Freight Costs (Inbound Shipping)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Extremely Low.</strong> You are only paying freight for advanced chemistry, not bulky wood fiber or excess water weight.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>Astronomical.</strong> You are paying cross-country LTL or Full Truckload rates primarily to ship heavy, bulky wood fiber.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Heavier than OHRA-BOND, requiring higher LTL classification rates.</td>
                            </tr>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Inventory Spoilage Risk</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Near Zero.</strong> Engineered for extreme multi-year shelf life in standard dry conditions. Does not degrade or attract pests.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Bulky paper/plastic bags are prone to forklift punctures and moisture wicking from concrete floors.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">High. Agricultural byproducts degrade rapidly, lump upon moisture exposure, and can attract rodents/insects.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Handling Labor (Touches)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Minimal.</strong> A single worker can easily carry enough binder for a multi-acre job in the cab of a truck.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>Intensive.</strong> Requires constant forklift operation to unload, store, and reload dozens of pallets onto flatbeds for the job site.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Requires forklift handling and pallet jacks.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
"""
        c = c.replace(old_block, tailored_table)
        with open('tech-storage-efficiency.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Tailored tech-storage-efficiency.html")
