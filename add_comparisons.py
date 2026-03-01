import os
import re

files = [f for f in os.listdir('.') if f.startswith('tech-') and f.endswith('.html')]

comparison_html = """
                <h2>Comparative Analysis: OHRA-BOND™ GREEN vs. Conventional Alternatives</h2>
                <p>When selecting a hydroseeding binder, the performance delta between advanced polymer chemistry and legacy agricultural byproducts is substantial. The table below outlines the key operational differences between OHRA-BOND™ GREEN, standard guar gum tackifiers, and basic synthetic polyacrylamide (PAM) blends.</p>

                <div style="overflow-x: auto; margin-top: 30px; margin-bottom: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <table style="width: 100%; border-collapse: collapse; background-color: #fff; text-align: left;">
                        <thead>
                            <tr style="background-color: var(--primary); color: #fff;">
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Performance Metric</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">OHRA-BOND™ GREEN</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Conventional Guar Gum</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Basic Synthetic Blends</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Rheology (Viscosity under shear)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>High pseudoplasticity.</strong> Excellent pump lubricity; builds immediate viscosity upon exit.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Can become gummy or stringy in high-shear pumps.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Variable. Often requires precise mixing to avoid "fish-eyes" or clumping.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Cross-Linking Capability</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Advanced 3D Matrix.</strong> Binds soil particles and mulch fibers instantly.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Weak to none. Relies primarily on surface adhesion (gluing).</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate. Depends heavily on the specific charge density of the polymer.</td>
                            </tr>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Application Rate (per acre)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Highly concentrated.</strong> Lower volume required (e.g., 3-5 lbs/acre depending on slope).</td>
                                <td style="padding: 16px; border: 1px solid #eee;">High volume required (often 40-60+ lbs/acre) to achieve basic tacking.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Low volume, but often requires supplemental tackifiers for heavy mulch loads.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Curing Time & Rainfastness</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Rapid cure.</strong> Forms a water-insoluble bond quickly, resisting washout.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Slow cure. Highly susceptible to re-wetting and washing away in heavy rain.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate to fast, but crusting can impede delicate seed germination.</td>
                            </tr>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Environmental & Microbial Profile</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Bio-enhanced.</strong> Supports soil microbes; non-toxic to aquatic life.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Biodegradable, but rapid breakdown can lead to premature failure.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Slow degradation. Some basic PAMs raise concerns over residual monomers.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
"""

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to insert this comparison table before the "Regulatory Compliance and Best Practices" section or the FAQ section.
    # Let's target the "Regulatory Compliance and Best Practices" heading that we added in the previous expansion.

    target_heading_1 = "<h2>Regulatory Compliance and Best Practices</h2>"
    target_heading_2 = "<h2>Frequently Asked Questions"

    if target_heading_1 in content:
        content = content.replace(target_heading_1, f'{comparison_html}\n{target_heading_1}')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with comparison table.")
    elif target_heading_2 in content:
         # Fallback if Regulatory Compliance isn't there
         content = content.replace(target_heading_2, f'{comparison_html}\n{target_heading_2}')
         with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
         print(f"Updated {filename} with comparison table using fallback.")

print("Done injecting comparison tables.")
