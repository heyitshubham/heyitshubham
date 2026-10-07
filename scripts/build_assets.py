"""Generates the animated SVGs in ../assets.

Every animation is SMIL with the *final* frame as the base state, so a viewer
that ignores animation (some mobile clients, image proxies) still shows the
finished picture instead of a blank card.

Run:  python3 scripts/build_assets.py
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

MONO = "'JetBrains Mono','SF Mono','Fira Code',Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

BG, PANEL, BORDER = "#0d1117", "#161b22", "#30363d"
TEXT, MUTED = "#e6edf3", "#8b949e"
GREEN, BLUE, AMBER, PURPLE, PINK = "#3fb950", "#58a6ff", "#d29922", "#bc8cff", "#ff7b72"


def appear(at):
    """Hidden until `at` seconds, then visible for good. Base state is visible."""
    return (f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;0.999;1" '
            f'dur="{at}s" fill="freeze"/>')


def fade_in(at, length=0.5):
    end = at + length
    return (f'<animate attributeName="opacity" values="0;0;1" keyTimes="0;{at/end:.4f};1" '
            f'dur="{end}s" fill="freeze"/>')


def write(name, body):
    (OUT / name).write_text(body.strip() + "\n", encoding="utf-8")
    print("wrote", OUT / name)


# ---------------------------------------------------------------- hero ----
def hero():
    W, H = 960, 380
    CW = 9.05          # monospace advance at 15px
    X0, Y0, STEP = 34, 84, 29
    lines, defs = [], []
    t = 0.3

    def prompt_line(i, cmd, start):
        nonlocal defs
        y = Y0 + i * STEP
        x_cmd = X0 + 3.6 * CW
        type_end = start + 0.1 + len(cmd) * 0.045
        width = len(cmd) * CW + 6
        cid = f"type{i}"
        defs.append(
            f'<clipPath id="{cid}"><rect x="{x_cmd}" y="{y-16}" height="22" width="{width:.0f}">'
            f'<animate attributeName="width" values="0;0;{width:.0f}" '
            f'keyTimes="0;{(start+0.1)/type_end:.4f};1" dur="{type_end:.2f}s" fill="freeze"/>'
            f'</rect></clipPath>')
        lines.append(
            f'<g>{appear(start)}'
            f'<text x="{X0}" y="{y}" class="m" fill="{GREEN}">➜</text>'
            f'<text x="{X0 + 2*CW}" y="{y}" class="m" fill="{BLUE}">~</text>'
            f'<text x="{x_cmd}" y="{y}" class="m" fill="{TEXT}" clip-path="url(#{cid})">{escape(cmd)}</text>'
            f'</g>')
        return type_end

    t = prompt_line(0, "whoami", 0.4) + 0.3
    lines.append(
        f'<g>{appear(t)}<text x="{X0}" y="{Y0 + STEP}" class="m">'
        f'<tspan fill="{TEXT}" font-weight="700">Shubham Chauhan</tspan>'
        f'<tspan fill="{MUTED}">  //  senior software engineer · full stack</tspan></text></g>')

    t = prompt_line(2, "cat ~/.stack", t + 0.4) + 0.3
    stack = [("java 21", AMBER), ("spring boot", GREEN), ("angular", PINK), ("postgres", BLUE),
             ("kafka", TEXT), ("redis", PINK), ("aws", AMBER)]
    spans, first = [], True
    for word, col in stack:
        if not first:
            spans.append(f'<tspan fill="{BORDER}"> · </tspan>')
        spans.append(f'<tspan fill="{col}">{word}</tspan>')
        first = False
    lines.append(f'<g>{appear(t)}<text x="{X0}" y="{Y0 + 3*STEP}" class="m">{"".join(spans)}</text></g>')

    t = prompt_line(4, "git log --oneline --author=shubham | head -4", t + 0.4) + 0.3
    commits = [
        ("a1f9c02", "split a legacy monolith into 9 spring boot microservices"),
        ("7c3e811", "upgrade angular v9 → v20, 30+ modules to standalone"),
        ("4d02b6e", "fix order search: full table scan → index lookup"),
        ("e93a1d7", "talk @ devfest noida: \"AI writes your code. who checks it?\""),
    ]
    for k, (sha, msg) in enumerate(commits):
        y = Y0 + (5 + k) * STEP
        lines.append(
            f'<g>{appear(round(t + k*0.22, 2))}<text x="{X0}" y="{y}" class="m">'
            f'<tspan fill="{AMBER}">{sha}</tspan><tspan fill="{TEXT}">  {escape(msg)}</tspan></text></g>')
    t = t + 4 * 0.22 + 0.3

    y = Y0 + 9 * STEP
    lines.append(
        f'<g>{appear(round(t, 2))}'
        f'<text x="{X0}" y="{y}" class="m" fill="{GREEN}">➜</text>'
        f'<text x="{X0 + 2*CW}" y="{y}" class="m" fill="{BLUE}">~</text>'
        f'<rect x="{X0 + 3.6*CW + 1}" y="{y-14}" width="9" height="18" fill="{GREEN}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.05s" repeatCount="indefinite"/>'
        f'</rect></g>')

    write("hero.svg", f'''
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Terminal: Shubham Chauhan, senior software engineer, full stack. Java 21, Spring Boot, Angular, Postgres, Kafka, Redis, AWS.">
  <style>.m{{font-family:{MONO};font-size:15px}}.s{{font-family:{SANS}}}</style>
  <defs>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BLUE}"/><stop offset=".5" stop-color="{PURPLE}"/><stop offset="1" stop-color="{GREEN}"/>
    </linearGradient>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#ffffff" opacity=".018"/></pattern>
    {''.join(defs)}
  </defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{BG}" stroke="url(#edge)" stroke-width="1.5"/>
  <rect x="1" y="1" width="{W-2}" height="40" rx="14" fill="{PANEL}"/>
  <rect x="1" y="28" width="{W-2}" height="13" fill="{PANEL}"/>
  <line x1="1" y1="41" x2="{W-1}" y2="41" stroke="{BORDER}"/>
  <circle cx="26" cy="21" r="6.5" fill="#ff5f57"/><circle cx="48" cy="21" r="6.5" fill="#febc2e"/><circle cx="70" cy="21" r="6.5" fill="#28c840"/>
  <text x="{W/2}" y="26" text-anchor="middle" class="m" font-size="13" fill="{MUTED}" style="font-size:13px">shubham@delhi-ncr — zsh — 96×24</text>
  {''.join(lines)}
  <rect x="2" y="42" width="{W-4}" height="{H-44}" rx="12" fill="url(#scan)" pointer-events="none"/>
</svg>''')


# ------------------------------------------------------- architecture ----
def architecture():
    W, H = 960, 380
    gx, gw = 360, 560
    col_w, gap = 176, 16
    rows_y = [138, 190, 242]
    names = ["orders", "users", "payments"]
    services = []
    for i in range(9):
        r, c = divmod(i, 3)
        x, y = gx + c * (col_w + gap), rows_y[r]
        named = i < len(names)
        label = names[i] if named else f"service-{i+1:02d}"
        col = [GREEN, BLUE, AMBER][i] if named else MUTED
        services.append(
            f'<g>{fade_in(round(2.2 + i*0.14, 2), 0.35)}'
            f'<rect x="{x}" y="{y}" width="{col_w}" height="40" rx="8" fill="{PANEL}" stroke="{col if named else BORDER}"/>'
            f'<circle cx="{x+18}" cy="{y+20}" r="4" fill="{col}">'
            f'<animate attributeName="opacity" values="1;.35;1" dur="{1.6 + (i % 4)*0.3:.1f}s" repeatCount="indefinite"/></circle>'
            f'<text x="{x+32}" y="{y+25}" class="m" fill="{TEXT if named else MUTED}">{label}</text></g>')

    stubs = "".join(
        f'<line x1="{gx + c*(col_w+gap) + col_w/2}" y1="282" x2="{gx + c*(col_w+gap) + col_w/2}" y2="306" stroke="{BORDER}" stroke-dasharray="3 3"/>'
        f'<line x1="{gx + c*(col_w+gap) + col_w/2}" y1="114" x2="{gx + c*(col_w+gap) + col_w/2}" y2="138" stroke="{BORDER}" stroke-dasharray="3 3"/>'
        for c in range(3))

    dots = "".join(
        f'<circle r="4" fill="{col}"><animateMotion dur="{d}s" begin="{b}s" repeatCount="indefinite" path="M{gx+10},321 H{gx+gw-10}"/></circle>'
        for col, d, b in [(GREEN, 3.2, 0), (AMBER, 4.1, 1.1), (BLUE, 3.6, 2.0), (PINK, 4.6, 0.6)])
    rdots = "".join(
        f'<circle r="3" fill="{col}" opacity=".8"><animateMotion dur="{d}s" begin="{b}s" repeatCount="indefinite" path="M{gx+gw-10},321 H{gx+10}"/></circle>'
        for col, d, b in [(PURPLE, 3.9, 0.4), (BLUE, 5.0, 1.7)])

    write("architecture.svg", f'''
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="A legacy monolith split into nine Spring Boot microservices, behind an API gateway with circuit breakers, talking over Kafka and Amazon SQS.">
  <style>.m{{font-family:{MONO};font-size:14px}}.s{{font-family:{SANS}}}</style>
  <defs>
    <linearGradient id="mono" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2d333b"/><stop offset="1" stop-color="#1c2128"/></linearGradient>
    <linearGradient id="bus" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GREEN}" stop-opacity=".18"/><stop offset=".5" stop-color="{BLUE}" stop-opacity=".18"/><stop offset="1" stop-color="{PURPLE}" stop-opacity=".18"/></linearGradient>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/></marker>
  </defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{BG}" stroke="{BORDER}"/>
  <text x="34" y="44" class="m" fill="{MUTED}">// strangler fig, one release at a time</text>
  <text x="{W-34}" y="44" text-anchor="end" class="m" fill="{MUTED}">day job · high-volume e-commerce platform</text>

  <!-- monolith: cracks, then fades as the services take over -->
  <g>
    <animate attributeName="opacity" values="1;1;.45" keyTimes="0;.6;1" dur="2.6s" fill="freeze"/>
    <rect x="60" y="96" width="190" height="226" rx="10" fill="url(#mono)" stroke="#444c56"/>
    <text x="155" y="128" text-anchor="middle" class="m" fill="{TEXT}" font-weight="700">MONOLITH</text>
    <text x="155" y="148" text-anchor="middle" class="m" fill="{MUTED}" style="font-size:12px">legacy · one deploy</text>
    <g stroke="#444c56" stroke-width="1">
      <path d="M80 170 H230 M80 196 H230 M80 222 H230 M80 248 H230 M80 274 H230 M80 300 H230" />
      <path d="M118 170 V300 M156 196 V274 M196 170 V300" stroke-dasharray="2 4"/>
    </g>
    <path d="M140 96 L160 150 L138 200 L170 250 L150 322" fill="none" stroke="{PINK}" stroke-width="2.5"
          stroke-dasharray="260" stroke-dashoffset="0">
      <animate attributeName="stroke-dashoffset" values="260;260;0" keyTimes="0;.45;1" dur="1.6s" fill="freeze"/>
    </path>
  </g>

  <path d="M266 209 H340" stroke="{BLUE}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)">
    <animate attributeName="stroke-dashoffset" from="22" to="0" dur=".8s" repeatCount="indefinite"/>
  </path>
  <text x="303" y="196" text-anchor="middle" class="m" fill="{BLUE}" style="font-size:12px">split</text>

  <g>{fade_in(1.6)}
    <rect x="{gx}" y="74" width="{gw}" height="40" rx="8" fill="{PANEL}" stroke="{PURPLE}"/>
    <text x="{gx+18}" y="99" class="m" fill="{PURPLE}" font-weight="700">API GATEWAY</text>
    <text x="{gx+gw-18}" y="99" text-anchor="end" class="m" fill="{MUTED}" style="font-size:12px">service discovery · resilience4j ⚡</text>
  </g>
  {stubs}
  {''.join(services)}
  <g>{fade_in(3.5)}
    <rect x="{gx}" y="306" width="{gw}" height="30" rx="15" fill="url(#bus)" stroke="{BORDER}"/>
    {dots}{rdots}
    <text x="{gx + gw/2}" y="358" text-anchor="middle" class="m" fill="{MUTED}" style="font-size:12px">events over KAFKA + AMAZON SQS · JUnit + Mockito guarding every step</text>
  </g>
</svg>''')


# ---------------------------------------------------------------- talk ----
def talk():
    W, H = 960, 260
    findings = [
        (PINK, "slow-query", "search() → EXPLAIN: Seq Scan"),
        (AMBER, "ignored-error", "catch (e) {} hides the failure"),
        (BLUE, "missing-test", "no test for the failed refund"),
        (PURPLE, "time-zone", "LocalDate.now() with no ZoneId"),
    ]
    rows = "".join(
        f'<g>{fade_in(round(0.9 + i*0.45, 2), 0.3)}'
        f'<rect x="548" y="{104 + i*32}" width="{len(tag)*7.6 + 16:.0f}" height="22" rx="11" fill="{col}" fill-opacity=".15" stroke="{col}" stroke-opacity=".6"/>'
        f'<text x="{556}" y="{119 + i*32}" class="m" fill="{col}" style="font-size:12px">{tag}</text>'
        f'<text x="{548 + len(tag)*7.6 + 26:.0f}" y="{119 + i*32}" class="m" fill="{TEXT}" style="font-size:12px">{escape(msg)}</text></g>'
        for i, (col, tag, msg) in enumerate(findings))
    write("talk.svg", f'''
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Talk at DevFest Noida 2026: AI writes your code. Who checks it?">
  <style>.m{{font-family:{MONO}}}.s{{font-family:{SANS}}}</style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#161a33"/></linearGradient>
    <linearGradient id="hl" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#4285f4"/><stop offset=".33" stop-color="#ea4335"/><stop offset=".66" stop-color="#fbbc04"/><stop offset="1" stop-color="#34a853"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#bg)" stroke="{BORDER}"/>
  <rect x="1" y="1" width="{W-2}" height="4" rx="2" fill="url(#hl)"/>
  <text x="40" y="58" class="m" fill="{MUTED}" style="font-size:13px;letter-spacing:2px">SPEAKER · DEVFEST NOIDA 2026</text>
  <text x="40" y="112" class="s" fill="{TEXT}" style="font-size:38px;font-weight:800">AI writes your code.</text>
  <text x="40" y="160" class="s" fill="url(#hl)" style="font-size:38px;font-weight:800">Who checks it?</text>
  <text x="40" y="200" class="s" fill="{MUTED}" style="font-size:15px">An Agent Skill that reviews Spring Boot PRs the way</text>
  <text x="40" y="222" class="s" fill="{MUTED}" style="font-size:15px">a senior engineer would, with secrets kept out of the AI's context.</text>

  <rect x="530" y="40" width="396" height="190" rx="10" fill="{BG}" stroke="{BORDER}"/>
  <text x="548" y="70" class="m" fill="{MUTED}" style="font-size:12px">/pr-review  ·  OrderService.java</text>
  <line x1="530" y1="84" x2="926" y2="84" stroke="{BORDER}"/>
  {rows}
</svg>''')


# --------------------------------------------------------------- cards ----
def card(name, accent, kicker, title, desc, chips, crt=False):
    W, H = 460, 210
    chip_svg, x = [], 28
    for c in chips:
        w = len(c) * 7.4 + 22
        chip_svg.append(
            f'<rect x="{x}" y="160" width="{w:.0f}" height="26" rx="13" fill="{accent}" fill-opacity=".12" stroke="{accent}" stroke-opacity=".45"/>'
            f'<text x="{x + w/2:.0f}" y="177" text-anchor="middle" class="m" fill="{accent}" style="font-size:12px">{escape(c)}</text>')
        x += w + 8
    crt_layer = ""
    if crt:
        crt_layer = (f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#scan)"/>'
                     f'<rect x="1" y="-30" width="{W-2}" height="30" fill="{accent}" opacity=".06">'
                     f'<animate attributeName="y" values="-30;{H}" dur="3.5s" repeatCount="indefinite"/></rect>')
    title_style = f"font-size:26px;font-weight:800" + (";letter-spacing:2px" if crt else "")
    title_font = "m" if crt else "s"
    write(name, f'''
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}: {escape(' '.join(desc))}">
  <style>.m{{font-family:{MONO}}}.s{{font-family:{SANS}}}</style>
  <defs>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{accent}" stop-opacity=".16"/><stop offset=".55" stop-color="{accent}" stop-opacity="0"/></linearGradient>
    <pattern id="scan" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="1" fill="#000" opacity=".35"/></pattern>
    <clipPath id="clip"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14"/></clipPath>
  </defs>
  <g clip-path="url(#clip)">
    <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{BG}"/>
    <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#glow)"/>
    <rect x="1" y="1" width="5" height="{H-2}" fill="{accent}"/>
    {crt_layer}
  </g>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="{BORDER}"/>
  <text x="28" y="40" class="m" fill="{accent}" style="font-size:11px;letter-spacing:1.5px">{escape(kicker)}</text>
  <text x="28" y="78" class="{title_font}" fill="{TEXT}" style="{title_style}">{escape(title)}</text>
  <text x="28" y="110" class="s" fill="{MUTED}" style="font-size:14px">{escape(desc[0])}</text>
  <text x="28" y="132" class="s" fill="{MUTED}" style="font-size:14px">{escape(desc[1])}</text>
  {''.join(chip_svg)}
  <text x="{W-26}" y="40" text-anchor="end" class="m" fill="{MUTED}" style="font-size:16px">↗</text>
</svg>''')


hero()
architecture()
talk()
card("card-leadloop.svg", GREEN, "HACKATHON · SERPAPI INDIA 2026", "LeadLoop",
     ("An AI agent that finds buyers, researches them and",
      "pitches a free sample. A human approves every email."),
     ["Python", "LangGraph", "FastAPI", "SerpApi"])
card("card-dukaan-saathi.svg", "#00baf2", "HACKATHON · PAYTM · MERCHANT GROWTH AI", "Dukaan Saathi",
     ("An AI business partner for kirana stores: WhatsApp",
      "orders, khata credit, and a copilot that can say no."),
     ["Java", "Next.js", "AI agents", "Hinglish"])
card("card-pr-review-skill.svg", PURPLE, "AGENT SKILL · FROM MY DEVFEST TALK", "pr-review-skill",
     ("Reviews Spring Boot PRs like a senior engineer:",
      "missing tests, ignored errors, slow queries, time zones."),
     ["Claude Code", "Agent Skills", "Spring Boot"])
card("card-type-tank.svg", "#39ff7a", "SIDE QUEST · ZERO DEPENDENCIES", "TYPE//TANK",
     ("A retro DOS typing-defense game: CRT glow, a 180°",
      "rotating cannon and sound synthesized in Web Audio."),
     ["Vanilla JS", "Canvas", "Web Audio"], crt=True)
