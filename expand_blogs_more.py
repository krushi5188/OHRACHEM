import os
import re

files = [f for f in os.listdir('.') if f.startswith('tech-') and f.endswith('.html') and f not in ['tech-freight-analysis.html', 'tech-storage-efficiency.html', 'tech-shelf-life.html']]

def expand_content_more(content):
    expansion = """
                <h2>Strategic Implementation and Site Preparation</h2>
                <p>Prior to application, the successful deployment of hydroseeding technologies demands meticulous site preparation. This involves analyzing soil composition to understand its chemical and physical properties, which dictates the necessary amendments required for optimal plant growth. Compaction must be alleviated to promote robust root penetration and enhance water infiltration rates.</p>

                <h3>Advanced Erosion Control Techniques</h3>
                <p>When dealing with extreme topographies, such as near-vertical cuts or slopes exposed to high-velocity water flow, standard hydroseeding methods are often insufficient. In these scenarios, Flexible Growth Mediums (FGMs) and High-Performance Formulated Matrices (HP-FBMs) become indispensable. These advanced systems combine refined wood fibers, interlocking crimped synthetic fibers, and highly cross-linked polymers to form an intimate, erosion-resistant matrix immediately upon application.</p>

                <h3>Analyzing Cost-to-Performance Metrics</h3>
                <p>A frequent error in project planning is focusing solely on the initial material cost per bag. The true economic metric is the installed cost per acre and the probability of a successful outcome without the need for rework. High-performance binders, though commanding a premium price, significantly reduce labor hours, equipment wear, and water usage, leading to a drastically lower total project cost while ensuring regulatory compliance.</p>

                <h2>Regulatory Compliance and Best Practices</h2>
                <p>In today's stringent regulatory environment, ensuring that all materials used in reclamation and erosion control projects comply with local and federal guidelines is non-negotiable. This includes verifying the biodegradability profile of polymers and ensuring they do not introduce harmful microplastics into delicate ecosystems.</p>
    """

    # Insert before the FAQ section
    content = content.replace('<h2>Frequently Asked Questions (FAQs)</h2>', f'{expansion}\n<h2>Frequently Asked Questions (FAQs)</h2>')

    return content

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    expanded_content = expand_content_more(content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(expanded_content)

print(f"Expanded {len(files)} files more.")
