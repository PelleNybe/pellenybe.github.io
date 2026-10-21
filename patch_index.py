import re

with open('index.html', 'r') as f:
    content = f.read()

# Add Python badge
badge_section = """<span class="inline-flex items-center px-3 py-1 rounded-full bg-surface-container border border-outline-variant/50 text-label-sm font-label-sm text-outline text-on-surface-variant">
            Python
          </span>"""
content = re.sub(r'(<span class="inline-flex items-center[^>]*>\s*Zero-Knowledge State\s*</span>\s*)</div>', r'\1' + badge_section + '\n</div>', content)


python_section = """
<!-- Python Backend & Data Engineering Section -->
<section class="space-y-4" id="python-projects">
<div class="flex items-baseline justify-between">
<div>
<span class="text-label-sm font-label-sm text-outline uppercase tracking-wider block">Backend &amp; Data Infrastructure</span>
<h2 class="text-headline-md font-headline-md text-primary font-semibold">Python Systems Engineering</h2>
</div>
<span class="text-label-sm font-label-sm text-secondary px-2.5 py-0.5 rounded border border-secondary/30 bg-surface-container-high hidden sm:inline-block">Open Source</span>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
  <!-- Python Project 1 -->
  <div class="rounded-xl border border-outline-variant/60 bg-surface-container-low p-5 space-y-4 hover:border-outline hover:bg-surface-container transition-all duration-300">
    <div class="flex items-center space-x-3 pb-3 border-b border-outline-variant/30">
      <div class="w-10 h-10 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center">
        <span class="material-symbols-outlined text-secondary" data-icon="schema">schema</span>
      </div>
      <div>
        <h3 class="text-headline-sm font-headline-sm text-primary font-medium">DataStream Processing Engine</h3>
      </div>
    </div>
    <p class="text-body-md font-body-md text-on-surface-variant leading-relaxed">
      A high-throughput ETL pipeline built with Python and Apache Kafka, capable of processing millions of events per second with sub-millisecond latency. Features automatic schema validation and dead-letter queues.
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Python 3.11</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Kafka</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">FastAPI</span>
    </div>
    <div class="pt-2">
      <a href="https://github.com" target="_blank" class="inline-flex items-center text-label-sm font-label-sm text-primary hover:text-secondary transition-colors">
        <span class="material-symbols-outlined text-sm mr-1">code</span> View on GitHub
      </a>
    </div>
  </div>

  <!-- Python Project 2 -->
  <div class="rounded-xl border border-outline-variant/60 bg-surface-container-low p-5 space-y-4 hover:border-outline hover:bg-surface-container transition-all duration-300">
    <div class="flex items-center space-x-3 pb-3 border-b border-outline-variant/30">
      <div class="w-10 h-10 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center">
        <span class="material-symbols-outlined text-secondary" data-icon="memory">memory</span>
      </div>
      <div>
        <h3 class="text-headline-sm font-headline-sm text-primary font-medium">Predictive ML Microservice</h3>
      </div>
    </div>
    <p class="text-body-md font-body-md text-on-surface-variant leading-relaxed">
      A deployed machine learning model serving infrastructure utilizing PyTorch and Docker. Implements A/B testing routing, model versioning, and real-time inference monitoring dashboards.
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">PyTorch</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Docker</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Redis</span>
    </div>
    <div class="pt-2">
      <a href="https://github.com" target="_blank" class="inline-flex items-center text-label-sm font-label-sm text-primary hover:text-secondary transition-colors">
        <span class="material-symbols-outlined text-sm mr-1">code</span> View on GitHub
      </a>
    </div>
  </div>
</div>
</section>
"""

content = content.replace('<!-- 4. Insights / Technical Writing Section -->', python_section + '\n<!-- 4. Insights / Technical Writing Section -->')

with open('index.html', 'w') as f:
    f.write(content)
