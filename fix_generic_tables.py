import os

# Define the old generic table we want to replace
old_table_start = "<h2>Comparative Analysis: OHRA-BOND™ GREEN vs. Conventional Alternatives</h2>"

# Define the new, 5-column comprehensive table that includes all 3 OHRA-BOND products vs all 3 Competitors
new_table = """<h2>Comparative Analysis: The OHRA-BOND™ System vs. Global Alternatives</h2>
                <p>When selecting a hydroseeding binder, the performance delta between advanced modular polymer chemistry and legacy agricultural byproducts or rigid pre-packaged mixes is substantial. The table below outlines the key operational differences between the complete OHRA-BOND™ System (GREEN, GROW, CAL), Pre-Packaged BFMs, Guar Gum, and Basic PAM.</p>

                <div style="overflow-x: auto; margin-top: 30px; margin-bottom: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <table style="width: 100%; border-collapse: collapse; background-color: #fff; text-align: left; min-width: 900px;">
                        <thead>
                            <tr style="background-color: var(--primary); color: #fff;">
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Performance Metric</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">The OHRA-BOND™ System (GREEN, GROW, CAL)</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Pre-Packaged BFM / FGM</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Conventional Guar Gum</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Basic Synthetic PAM</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Rheology & Tacking Power</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>High Yield.</strong> GREEN (Micro-Activated Hydrocolloid) provides intense shear-thinning lubricity and instant 3D cross-linking at just 20-70 lbs/acre.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">High Tacking. Relies on massive volumes of wood fiber pre-mixed with binder to create a crust. Heavy and difficult to pump long distances.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Can become sticky/gummy in pumps. Requires high volumes (40-60+ lbs/acre).</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Variable. Often requires precise mixing to avoid "fish-eyes" or clumping in the tank.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Biological Soil Amendment</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Integrated.</strong> GROW combines hydrocolloids with 50% Potassium Humate to instantly increase soil CEC and feed microbes on sterile dirt.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Low/Moderate. Provides organic matter (wood), but often lacks humic acid for immediate Cation Exchange Capacity improvement.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Low. Provides basic organic carbon as it breaks down, but does not actively rebuild soil structure.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">None. 100% synthetic. Zero biological value added to the soil.</td>
                            </tr>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Soil Flocculation & pH Control</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Immediate.</strong> CAL utilizes micronized Agricultural Gypsum to chemically flocculate hardpan clay, improving water infiltration instantly.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">None. BFMs blanket the soil but cannot chemically alter or loosen tight clay profiles beneath the crust.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">None. Relies purely on surface adhesion.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Some anionic PAMs flocculate soil, but lack the physical structure-building properties of gypsum.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Curing Time & Rainfastness</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Rapid Cure.</strong> Forms a water-insoluble matrix quickly, resisting washout even in heavy rain events.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate to Slow. The massive volume of water absorbed by the wood fiber requires significant drying time before it becomes rainfast.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Slow cure. Highly susceptible to re-wetting and washing away in subsequent rain.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Fast, but crusting can impede delicate seed germination if applied too heavily.</td>
                            </tr>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Total Installed Cost (Materials + Freight)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Highly Cost-Effective.</strong> You pay zero freight for pre-packaged wood fiber or water. Source mulch locally and mix with our highly concentrated chemistry.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>Premium/Expensive.</strong> You are paying a high markup and massive cross-country freight rates for pre-mixed binder and wood fiber in the same bag.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Low initial cost, but high failure rate often necessitates costly, labor-intensive resprays.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Low freight cost, but requires purchasing and shipping separate fertilizers and humates to match OHRA-BOND GROW's performance.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
"""

files = [f for f in os.listdir('.') if f.startswith('tech-') and f.endswith('.html')]
# Exclude the ones we already manually tailored
exclude = ['tech-freight-analysis.html', 'tech-water-usage.html', 'tech-storage-efficiency.html']

updated_count = 0
for filename in files:
    if filename in exclude:
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to find the start and end of the old table.
    # The old table started with the h2 and ended with a </div>.
    # But to be safe, we can look for the start h2, and then the next h2 (which is usually "Regulatory Compliance" or "Frequently Asked").

    if old_table_start in content:
        start_idx = content.find(old_table_start)
        # Find the end of the div that contains the table
        end_idx = content.find("</div>", content.find("</table>", start_idx)) + 6

        old_block = content[start_idx:end_idx]

        content = content.replace(old_block, new_table)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

print(f"Updated {updated_count} blogs with the comprehensive 5-column competitive table.")
