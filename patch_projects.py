import re

with open('index.html', 'r') as f:
    content = f.read()

new_projects = """
  <!-- Python Project 3 -->
  <div class="rounded-xl border border-outline-variant/60 bg-surface-container-low p-5 space-y-4 hover:border-outline hover:bg-surface-container transition-all duration-300">
    <div class="flex items-center space-x-3 pb-3 border-b border-outline-variant/30">
      <div class="w-10 h-10 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center">
        <span class="material-symbols-outlined text-secondary" data-icon="robot_2">robot_2</span>
      </div>
      <div>
        <h3 class="text-headline-sm font-headline-sm text-primary font-medium">Corax Crypto Autonomous Actor</h3>
      </div>
    </div>
    <p class="text-body-md font-body-md text-on-surface-variant leading-relaxed">
      Enterprise-grade Autonomous Economic Actor by Corax CoLAB. Powered by a 100% Polars-native pipeline for blistering speed and LLM-driven regime-switching. Features self-custodied on-chain settlement.
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Python</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Polars</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">LLM</span>
    </div>
    <div class="pt-2">
      <a href="https://github.com/PelleNybe/Corax-Crypto-by-CoraxCoLAB" target="_blank" class="inline-flex items-center text-label-sm font-label-sm text-primary hover:text-secondary transition-colors">
        <span class="material-symbols-outlined text-sm mr-1">code</span> View on GitHub
      </a>
    </div>
  </div>

  <!-- Python Project 4 -->
  <div class="rounded-xl border border-outline-variant/60 bg-surface-container-low p-5 space-y-4 hover:border-outline hover:bg-surface-container transition-all duration-300">
    <div class="flex items-center space-x-3 pb-3 border-b border-outline-variant/30">
      <div class="w-10 h-10 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center">
        <span class="material-symbols-outlined text-secondary" data-icon="trending_up">trending_up</span>
      </div>
      <div>
        <h3 class="text-headline-sm font-headline-sm text-primary font-medium">Crypto Momentum Detector</h3>
      </div>
    </div>
    <p class="text-body-md font-body-md text-on-surface-variant leading-relaxed">
      A high-performance Streamlit & CLI suite by Corax CoLAB. Features concurrent multi-ticker analysis, ATR-based risk management, and MTF validation. Powered by yfinance and ta.
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Python</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Streamlit</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Pandas</span>
    </div>
    <div class="pt-2">
      <a href="https://github.com/PelleNybe/crypto-momentum-detector" target="_blank" class="inline-flex items-center text-label-sm font-label-sm text-primary hover:text-secondary transition-colors">
        <span class="material-symbols-outlined text-sm mr-1">code</span> View on GitHub
      </a>
    </div>
  </div>

  <!-- Python Project 5 -->
  <div class="rounded-xl border border-outline-variant/60 bg-surface-container-low p-5 space-y-4 hover:border-outline hover:bg-surface-container transition-all duration-300">
    <div class="flex items-center space-x-3 pb-3 border-b border-outline-variant/30">
      <div class="w-10 h-10 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center">
        <span class="material-symbols-outlined text-secondary" data-icon="precision_manufacturing">precision_manufacturing</span>
      </div>
      <div>
        <h3 class="text-headline-sm font-headline-sm text-primary font-medium">PythonRobotics</h3>
      </div>
    </div>
    <p class="text-body-md font-body-md text-on-surface-variant leading-relaxed">
      Python sample codes and textbook for robotics algorithms. Includes various SLAM, navigation, and path planning algorithm implementations used in practical autonomous systems.
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Python</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Robotics</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Algorithms</span>
    </div>
    <div class="pt-2">
      <a href="https://github.com/PelleNybe/PythonRobotics" target="_blank" class="inline-flex items-center text-label-sm font-label-sm text-primary hover:text-secondary transition-colors">
        <span class="material-symbols-outlined text-sm mr-1">code</span> View on GitHub
      </a>
    </div>
  </div>

  <!-- Python Project 6 -->
  <div class="rounded-xl border border-outline-variant/60 bg-surface-container-low p-5 space-y-4 hover:border-outline hover:bg-surface-container transition-all duration-300">
    <div class="flex items-center space-x-3 pb-3 border-b border-outline-variant/30">
      <div class="w-10 h-10 rounded-lg bg-surface-container-high border border-outline-variant flex items-center justify-center">
        <span class="material-symbols-outlined text-secondary" data-icon="account_balance">account_balance</span>
      </div>
      <div>
        <h3 class="text-headline-sm font-headline-sm text-primary font-medium">Accounting by Corax CoLAB</h3>
      </div>
    </div>
    <p class="text-body-md font-body-md text-on-surface-variant leading-relaxed">
      Free and Open Source Enterprise Resource Planning (ERP) written in Python. A complete, robust suite managing everything from ledgers to robust data integrity.
    </p>
    <div class="flex flex-wrap gap-2 pt-2">
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Python</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">ERP</span>
      <span class="text-label-sm font-label-sm px-2 py-0.5 rounded bg-surface-dim border border-outline-variant/40 text-on-surface">Finance</span>
    </div>
    <div class="pt-2">
      <a href="https://github.com/PelleNybe/Accounting-by-Corax-CoLAB" target="_blank" class="inline-flex items-center text-label-sm font-label-sm text-primary hover:text-secondary transition-colors">
        <span class="material-symbols-outlined text-sm mr-1">code</span> View on GitHub
      </a>
    </div>
  </div>
"""

content = content.replace('</div>\n</section>\n\n<!-- 4. Insights / Technical Writing Section -->', new_projects + '\n</div>\n</section>\n\n<!-- 4. Insights / Technical Writing Section -->')

# Update github links on existing python projects
content = content.replace('<!-- Python Project 1 -->\n  <div class="rounded-xl', '<!-- Python Project 1 -->\n  <div class="rounded-xl')
content = re.sub(r'<!-- Python Project 1 -->(.*?)<a href="https://github.com"', r'<!-- Python Project 1 -->\1<a href="https://github.com/PelleNybe/datasets"', content, flags=re.DOTALL)
content = re.sub(r'<!-- Python Project 2 -->(.*?)<a href="https://github.com"', r'<!-- Python Project 2 -->\1<a href="https://github.com/PelleNybe/lerobot"', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
