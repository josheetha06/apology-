import math

def generate_lace_heart():
    width = 600
    height = 540
    
    svg_parts = []
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <filter id="lace-shadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#4a3f35" flood-opacity="0.12" />
    </filter>
    <radialGradient id="lace-paper-grad" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="85%" stop-color="#faf7f2" />
      <stop offset="100%" stop-color="#f0ebe1" />
    </radialGradient>
  </defs>
  <g filter="url(#lace-shadow)">
''')

    def heart_point(t, scale=1.0, cx=300, cy=245):
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        return (cx + x * scale, cy + y * scale)

    n_scallops = 44
    scallop_path_d = []
    dt = (2 * math.pi) / n_scallops
    
    for i in range(n_scallops):
        t1 = -math.pi + i * dt
        t2 = -math.pi + (i + 1) * dt
        t_mid = (t1 + t2) / 2
        
        p1 = heart_point(t1, scale=15.0, cy=245)
        p2 = heart_point(t2, scale=15.0, cy=245)
        pm = heart_point(t_mid, scale=16.8, cy=245)
        
        if i == 0:
            scallop_path_d.append(f"M {p1[0]:.2f} {p1[1]:.2f}")
        scallop_path_d.append(f"Q {pm[0]:.2f} {pm[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}")
        
    scallop_path_str = " ".join(scallop_path_d) + " Z"
    svg_parts.append(f'    <path d="{scallop_path_str}" fill="url(#lace-paper-grad)" stroke="#eae4d8" stroke-width="1.5" />\n')

    # Eyelets and decorative perforations
    eyelets = []
    for i in range(n_scallops):
        t = -math.pi + (i + 0.5) * dt
        pt = heart_point(t, scale=14.5, cy=245)
        eyelets.append(f'    <circle cx="{pt[0]:.2f}" cy="{pt[1]:.2f}" r="3.2" fill="#d2c8b8" fill-opacity="0.35" stroke="#ffffff" stroke-width="0.8" />')
        
        pt_inner = heart_point(t, scale=13.0, cy=245)
        eyelets.append(f'    <circle cx="{pt_inner[0]:.2f}" cy="{pt_inner[1]:.2f}" r="1.8" fill="#c4b9a7" fill-opacity="0.3" stroke="#ffffff" stroke-width="0.5" />')
    
    svg_parts.append("\n".join(eyelets) + "\n")

    # Filigree arches
    n_arches = 36
    dt_arch = (2 * math.pi) / n_arches
    arch_paths = []
    for i in range(n_arches):
        t1 = -math.pi + i * dt_arch
        t2 = -math.pi + (i + 1) * dt_arch
        t_mid = (t1 + t2) / 2
        p1 = heart_point(t1, scale=12.2, cy=245)
        p2 = heart_point(t2, scale=12.2, cy=245)
        pm = heart_point(t_mid, scale=10.8, cy=245)
        
        arch_paths.append(f'    <path d="M {p1[0]:.2f} {p1[1]:.2f} Q {pm[0]:.2f} {pm[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}" fill="none" stroke="#e0d7c7" stroke-width="1.8" />')
        pt_drop = heart_point(t_mid, scale=11.6, cy=245)
        arch_paths.append(f'    <ellipse cx="{pt_drop[0]:.2f}" cy="{pt_drop[1]:.2f}" rx="2.5" ry="4.5" fill="#cfc4b2" fill-opacity="0.4" transform="rotate({math.degrees(t_mid) + 90} {pt_drop[0]:.2f} {pt_drop[1]:.2f})" />')
    
    svg_parts.append("\n".join(arch_paths) + "\n")

    # Inner heart solid panel
    inner_heart_pts = []
    for step in range(120):
        t = -math.pi + step * (2 * math.pi / 120)
        pt = heart_point(t, scale=9.8, cy=245)
        if step == 0:
            inner_heart_pts.append(f"M {pt[0]:.2f} {pt[1]:.2f}")
        else:
            inner_heart_pts.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
    inner_heart_path = " ".join(inner_heart_pts) + " Z"
    svg_parts.append(f'    <path d="{inner_heart_path}" fill="#fffdfa" stroke="#e6decb" stroke-width="1" stroke-dasharray="3,2" />\n')

    # Central delicate ring
    center_heart_pts = []
    for step in range(80):
        t = -math.pi + step * (2 * math.pi / 80)
        pt = heart_point(t, scale=6.5, cy=245)
        if step == 0:
            center_heart_pts.append(f"M {pt[0]:.2f} {pt[1]:.2f}")
        else:
            center_heart_pts.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
    center_heart_path = " ".join(center_heart_pts) + " Z"
    svg_parts.append(f'    <path d="{center_heart_path}" fill="none" stroke="#ede5d8" stroke-width="1.2" />\n')
    
    # Inner mesh lines
    mesh_lines = []
    for ox in range(210, 400, 16):
        mesh_lines.append(f'    <line x1="{ox}" y1="160" x2="{ox + 80}" y2="340" stroke="#f2ecdf" stroke-width="0.8" opacity="0.7"/>')
        mesh_lines.append(f'    <line x1="{ox + 80}" y1="160" x2="{ox}" y2="340" stroke="#f2ecdf" stroke-width="0.8" opacity="0.7"/>')
    svg_parts.append("\n".join(mesh_lines) + "\n")

    svg_parts.append('''  </g>
</svg>''')
    
    with open("assets/lace-heart.svg", "w", encoding="utf-8") as f:
        f.write("".join(svg_parts))
    print("Generated assets/lace-heart.svg")

def generate_orchid():
    # Elegant Phalaenopsis orchid blossom matching the reference photo
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 300" width="100%" height="100%">
  <defs>
    <filter id="orchid-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="6" stdDeviation="7" flood-color="#2a1f1d" flood-opacity="0.25" />
    </filter>
    
    <!-- Petal Gradients -->
    <radialGradient id="petal-main-grad" cx="45%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="45%" stop-color="#fdf4f6" />
      <stop offset="75%" stop-color="#f5d7e1" />
      <stop offset="100%" stop-color="#e8b8cb" />
    </radialGradient>

    <radialGradient id="petal-back-grad" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="60%" stop-color="#fae7ed" />
      <stop offset="100%" stop-color="#dfaabf" />
    </radialGradient>

    <radialGradient id="lip-center-grad" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fff275" />
      <stop offset="35%" stop-color="#ea738d" />
      <stop offset="80%" stop-color="#9e1946" />
      <stop offset="100%" stop-color="#6b0d2b" />
    </radialGradient>

    <linearGradient id="stem-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8a9e70" />
      <stop offset="100%" stop-color="#556b3e" />
    </linearGradient>
  </defs>

  <g filter="url(#orchid-shadow)">
    <!-- Stem / Pedicel -->
    <path d="M 160 160 Q 145 220 120 270" stroke="url(#stem-grad)" stroke-width="5" stroke-linecap="round" fill="none" />
    
    <!-- Back Top Dorsal Sepal -->
    <path d="M 160 150 C 130 110 135 60 160 30 C 185 60 190 110 160 150 Z" 
          fill="url(#petal-back-grad)" stroke="#edd3de" stroke-width="0.8" />
    
    <!-- Back Lower Left Sepal -->
    <path d="M 155 155 C 115 155 70 195 90 230 C 120 240 150 190 155 155 Z" 
          fill="url(#petal-back-grad)" stroke="#edd3de" stroke-width="0.8" />

    <!-- Back Lower Right Sepal -->
    <path d="M 165 155 C 205 155 250 195 230 230 C 200 240 170 190 165 155 Z" 
          fill="url(#petal-back-grad)" stroke="#edd3de" stroke-width="0.8" />

    <!-- Left Large Lateral Petal -->
    <path d="M 160 150 C 110 115 40 120 40 155 C 40 195 110 185 160 150 Z" 
          fill="url(#petal-main-grad)" stroke="#e8c7d5" stroke-width="0.8" />
    <!-- Subtle Petal Veining Left -->
    <path d="M 155 150 Q 100 148 60 155" stroke="#d99cb5" stroke-width="0.75" opacity="0.4" fill="none" />
    <path d="M 150 146 Q 110 130 75 135" stroke="#d99cb5" stroke-width="0.6" opacity="0.35" fill="none" />
    <path d="M 150 155 Q 110 168 75 172" stroke="#d99cb5" stroke-width="0.6" opacity="0.35" fill="none" />

    <!-- Right Large Lateral Petal -->
    <path d="M 160 150 C 210 115 280 120 280 155 C 280 195 210 185 160 150 Z" 
          fill="url(#petal-main-grad)" stroke="#e8c7d5" stroke-width="0.8" />
    <!-- Subtle Petal Veining Right -->
    <path d="M 165 150 Q 220 148 260 155" stroke="#d99cb5" stroke-width="0.75" opacity="0.4" fill="none" />
    <path d="M 170 146 Q 210 130 245 135" stroke="#d99cb5" stroke-width="0.6" opacity="0.35" fill="none" />
    <path d="M 170 155 Q 210 168 245 172" stroke="#d99cb5" stroke-width="0.6" opacity="0.35" fill="none" />

    <!-- Labellum / Lip (Center floral tongue with rich speckled details) -->
    <!-- Lip side lobes -->
    <path d="M 150 150 C 135 140 130 160 140 170 C 148 175 155 160 150 150 Z" fill="#9e1946" opacity="0.85" />
    <path d="M 170 150 C 185 140 190 160 180 170 C 172 175 165 160 170 150 Z" fill="#9e1946" opacity="0.85" />
    
    <!-- Mid-lobe spreading downward -->
    <path d="M 152 165 C 135 185 138 210 160 215 C 182 210 185 185 168 165 Z" 
          fill="url(#lip-center-grad)" stroke="#780e32" stroke-width="0.8" />

    <!-- Little tendril tips at lip apex -->
    <path d="M 158 214 Q 152 224 148 220" stroke="#8a1139" stroke-width="1.2" fill="none" stroke-linecap="round" />
    <path d="M 162 214 Q 168 224 172 220" stroke="#8a1139" stroke-width="1.2" fill="none" stroke-linecap="round" />

    <!-- Speckles & Spots on Orchid Lip -->
    <circle cx="156" cy="180" r="1.2" fill="#540720" />
    <circle cx="164" cy="180" r="1.2" fill="#540720" />
    <circle cx="152" cy="190" r="1.4" fill="#540720" />
    <circle cx="160" cy="188" r="1.5" fill="#540720" />
    <circle cx="168" cy="190" r="1.3" fill="#540720" />
    <circle cx="157" cy="198" r="1.2" fill="#540720" />
    <circle cx="163" cy="198" r="1.2" fill="#540720" />

    <!-- Central Column (anther cap) -->
    <ellipse cx="160" cy="148" rx="7" ry="9" fill="#ffffff" stroke="#f3d4e0" stroke-width="1" />
    <circle cx="160" cy="151" r="2.8" fill="#fadb38" />
  </g>
</svg>'''
    with open("assets/orchid.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated assets/orchid.svg")

def generate_wax_seal():
    # Luxury vintage wax seal
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="100%" height="100%">
  <defs>
    <filter id="seal-shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#1e0b0b" flood-opacity="0.35" />
    </filter>
    <radialGradient id="wax-grad" cx="40%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#b83b3b" />
      <stop offset="50%" stop-color="#8b1c1c" />
      <stop offset="85%" stop-color="#631010" />
      <stop offset="100%" stop-color="#450808" />
    </radialGradient>
    <radialGradient id="gold-foil-grad" cx="40%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#fff1b8" />
      <stop offset="40%" stop-color="#dfb15b" />
      <stop offset="75%" stop-color="#ab7a28" />
      <stop offset="100%" stop-color="#69460d" />
    </radialGradient>
  </defs>

  <g filter="url(#seal-shadow)">
    <!-- Organic dripping/pressed wax border -->
    <path d="M 80 15 
             C 98 12, 115 18, 128 32 
             C 142 45, 149 65, 147 84 
             C 145 105, 137 122, 122 135 
             C 107 148, 86 150, 68 146 
             C 48 142, 30 133, 20 116 
             C 10 99, 12 78, 20 60 
             C 28 42, 45 25, 65 17 
             C 70 15, 75 14, 80 15 Z" 
          fill="url(#wax-grad)" stroke="#420606" stroke-width="1.2" />

    <!-- Inner pressed groove -->
    <circle cx="80" cy="80" r="46" fill="#751515" stroke="#500909" stroke-width="2.5" />
    <circle cx="80" cy="80" r="43" fill="none" stroke="#9e2828" stroke-width="1" stroke-dasharray="4,2" />

    <!-- Embossed Heart Emblem in center -->
    <path d="M 80 94 
             C 77 90, 62 76, 62 67 
             C 62 59, 68 54, 75 54 
             C 79 54, 82 56, 84 59 
             C 86 56, 89 54, 93 54 
             C 100 54, 106 59, 106 67 
             C 106 76, 91 90, 88 94 
             C 86 96, 82 96, 80 94 Z" 
          fill="url(#gold-foil-grad)" stroke="#ffe494" stroke-width="0.8" />
          
    <!-- Glossy highlight crescent -->
    <path d="M 45 42 A 46 46 0 0 1 115 42 A 48 48 0 0 0 45 42 Z" fill="#ffffff" opacity="0.18" />
  </g>
</svg>'''
    with open("assets/wax-seal.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated assets/wax-seal.svg")

def generate_default_polaroid():
    # We will also create a vintage sunset/holding hands vector photo illustration for default polaroid
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 340" width="100%" height="100%">
  <defs>
    <linearGradient id="sky-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3d405b" />
      <stop offset="40%" stop-color="#8f5b6f" />
      <stop offset="70%" stop-color="#e07a5f" />
      <stop offset="100%" stop-color="#f4a261" />
    </linearGradient>
    <radialGradient id="sun-glow" cx="65%" cy="65%" r="40%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9" />
      <stop offset="30%" stop-color="#ffe8a3" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#f4a261" stop-opacity="0" />
    </radialGradient>
  </defs>
  
  <rect width="400" height="340" fill="url(#sky-grad)" />
  <circle cx="260" cy="210" r="90" fill="url(#sun-glow)" />
  
  <!-- Silhouette of peaceful ocean or horizon with gentle waves -->
  <path d="M 0 250 Q 100 245 200 248 T 400 246 L 400 340 L 0 340 Z" fill="#264653" opacity="0.8" />
  <path d="M 0 270 Q 120 262 240 266 T 400 265 L 400 340 L 0 340 Z" fill="#1b2e3b" />
  
  <!-- Warm sparkle particles / sunset bokeh -->
  <circle cx="270" cy="190" r="3" fill="#ffffff" opacity="0.8" />
  <circle cx="295" cy="180" r="2" fill="#fff7d6" opacity="0.7" />
  <circle cx="240" cy="225" r="2.5" fill="#ffffff" opacity="0.9" />
  <circle cx="160" cy="210" r="4" fill="#ffffff" opacity="0.25" />
  <circle cx="180" cy="160" r="2" fill="#ffffff" opacity="0.4" />
</svg>'''
    with open("assets/default-photo.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated assets/default-photo.svg")

generate_lace_heart()
generate_orchid()
generate_wax_seal()
generate_default_polaroid()
