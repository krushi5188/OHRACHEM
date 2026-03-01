import os

files = [f for f in os.listdir('.') if f.startswith('tech-') and f.endswith('.html')]

# We'll replace the existing table's headers and add a new column for BFM (Bonded Fiber Matrix).
# We'll inject this by modifying the previously inserted HTML string.

def update_table(content):
    # This is a bit tricky since we just inserted the HTML. Let's find the start and end of the table div.
    start_tag = '<div style="overflow-x: auto; margin-top: 30px; margin-bottom: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">'
    end_tag = '</div>'

    if start_tag in content and end_tag in content:
        start_index = content.find(start_tag)
        # Find the next closing div after the start tag
        end_index = content.find(end_tag, start_index) + len(end_tag)

        old_table_html = content[start_index:end_index]

        new_table_html = """
                <div style="overflow-x: auto; margin-top: 30px; margin-bottom: 40px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    <table style="width: 100%; border-collapse: collapse; background-color: #fff; text-align: left;">
                        <thead>
                            <tr style="background-color: var(--primary); color: #fff;">
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Performance Metric</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">OHRA-BOND™ GREEN + Standard Mulch</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Pre-Packaged BFM (Bonded Fiber Matrix)</th>
                                <th style="padding: 16px; border: 1px solid #ddd; font-weight: 600;">Conventional Guar Gum</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Material Cost (Per Acre)</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Highly Cost-Effective.</strong> Procure local mulch separately and add highly concentrated binder. Drastically lowers material overhead.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>Premium Pricing.</strong> You are paying a high markup for pre-mixed binder and wood fiber in the same bag.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Low initial cost, but high failure rate often necessitates costly resprays.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Freight & Logistics</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>Efficient.</strong> Ship concentrated chemistry on a few pallets; source bulky mulch locally. Saves thousands in freight.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>Inefficient.</strong> Shipping pre-packaged BFM means paying heavy freight rates to transport bulky wood fiber across the country.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Standard shipping, but requires large volumes of powder (40-60 lbs/acre).</td>
                            </tr>
                            <tr>
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Erosion Control Effectiveness</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>FGM-Level Performance.</strong> Advanced cross-linking polymers create a permanent, water-insoluble 3D matrix instantly.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">High performance. Forms a strong crust, but can sometimes inhibit delicate seed emergence if applied too heavily.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Low to Moderate. Susceptible to re-wetting and washout in heavy rain events.</td>
                            </tr>
                            <tr style="background-color: #fcfcfc;">
                                <td style="padding: 16px; border: 1px solid #eee; font-weight: 600;">Mixing & Tank Payload</td>
                                <td style="padding: 16px; border: 1px solid #eee; background-color: rgba(46, 204, 113, 0.1);"><strong>High Payload.</strong> Supreme lubricity allows for higher mulch-to-water ratios. Cover more area per tank.</td>
                                <td style="padding: 16px; border: 1px solid #eee;"><strong>Low Payload.</strong> BFMs absorb massive amounts of water, drastically limiting the square footage covered per tank load.</td>
                                <td style="padding: 16px; border: 1px solid #eee;">Moderate payload. Can become gummy and cause pump cavitation if over-mixed.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
"""
        return content.replace(old_table_html, new_table_html)
    return content

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    updated_content = update_table(content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)

print("Updated comparison tables to include BFM metrics (Cost, Freight, Performance, Payload).")
