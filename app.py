import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Vidya | Product Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# CONFIG — replace these values
# -----------------------------
NAME = "Vidya"
ROLE = "Senior Product Manager"
TAGLINE = "Factory Software · Supply Chain · Manufacturing · AI"

LINKEDIN_URL = "https://www.linkedin.com/in/vidya-krishnamoorthy-288845b8/"
GITHUB_URL = "https://github.com/vidyakrishnamoorthy"
RESUME_URL = "https://docs.google.com/document/d/165_V5BScRxjAczOhIvw19v0CLIUzv9xtYryHsCeCxB8/edit?usp=sharing"
SCHOLAR_URL = "https://scholar.google.com/citations?hl=en&user=PVloDrkAAAAJ"

PUBLICATIONS = [
    {
        "year": "2026",
        "title": "Adaptive Driving Style for SAE Level-2 Driving Automation: Minimizing Preference Mismatch",
        "venue": "American Control Conference (ACC)",
        "authors": "K. Akash, Z. Zheng, T. Misu, V. Krishnamoorthy, M. Dong, Y. Lee, G. Huang",
        "url": "https://arxiv.org/abs/2607.21819",
        "tag": "Adaptive Automation",
    },
    {
        "year": "2024",
        "title": "Driving Aggressively or Conservatively? Investigating the Effects of Automated Vehicle Interaction Type and Road Event on Drivers’ Trust and Preferred Driving Style",
        "venue": "Human Factors",
        "authors": "Y. Lee, M. Dong, V. Krishnamoorthy, K. Akash, T. Misu, Z. Zheng, G. Huang",
        "url": "https://doi.org/10.1177/00187208231181199",
        "tag": "Human Factors",
    },
    {
        "year": "2022",
        "title": "Investigating Users' Preferences in Adaptive Driving Styles for Level 2 Driving Automation",
        "venue": "AutomotiveUI '22",
        "authors": "Z. Sajedinia, K. Akash, Z. Zheng, T. Misu, M. Dong, V. Krishnamoorthy, et al.",
        "url": "https://doi.org/10.1145/3543174.3546088",
        "tag": "User Preference",
    },
    {
        "year": "2022",
        "title": "Identification of Adaptive Driving Style Preference through Implicit Inputs in SAE L2 Vehicles",
        "venue": "International Conference on Multimodal Interaction (ICMI)",
        "authors": "Z. Zheng, K. Akash, T. Misu, V. Krishnamoorthy, M. Dong, Y. Lee, G. Huang",
        "url": "https://doi.org/10.1145/3536221.3556637",
        "tag": "Multimodal AI",
    },
    {
        "year": "2022",
        "title": "The Impacts of Adaptive Driving Styles on Trust in Level 2 Automated Vehicles",
        "venue": "Human Factors and Ergonomics Society Annual Meeting",
        "authors": "Y. Y. Lee, M. Dong, V. Krishnamoorthy, K. Akash, Z. Zheng, T. Misu, G. Huang",
        "url": "https://doi.org/10.1177/1071181322661327",
        "tag": "Trust in Automation",
    },
]

PROJECTS = {
    "Factory Launch": {
        "icon": "🏭",
        "subtitle": "Building software for complex manufacturing operations",
        "status": "MISSION COMPLETE",
        "problem": (
            "A new manufacturing operation needed an end-to-end material flow that could "
            "coordinate internal logistics software with external manufacturing systems."
        ),
        "constraints": [
            "Multiple systems and teams with different ownership boundaries",
            "The rollout had to support ongoing physical operations",
            "The solution depended on reliable integrations between enterprise systems",
            "The solution needed to be reusable across future operational workflows",
        ],
        "decisions": [
            "Mapped the end-to-end user and operational journey before defining product behavior",
            "Clarified ownership across systems, workflows, and user teams",
            "Defined product requirements and integration behavior across connected systems",
            "Designed exception and recovery experiences alongside the primary workflow",
        ],
        "impact": [
            "Created a scalable foundation for operational material workflows",
            "Improved visibility and alignment across product, engineering, and operations",
            "Reduced ambiguity around ownership, system behavior, and exception handling",
        ],
        "lesson": (
            "Factory software is never just software. The product has to model the physical "
            "world, system boundaries, operator behavior, and failure recovery at the same time."
        ),
    },
    "Inventory Systems": {
        "icon": "📦",
        "subtitle": "Making operational state visible and actionable",
        "status": "MISSION COMPLETE",
        "problem": (
            "Operational teams needed better visibility into material, containers, and inventory "
            "moving across production and service workflows."
        ),
        "constraints": [
            "Operational state existed across several systems",
            "Physical and digital state could diverge",
            "Different user groups needed different levels of visibility",
            "Manual workarounds could mask underlying process or system problems",
        ],
        "decisions": [
            "Defined clear lifecycle states for tracked operational entities",
            "Designed workflows around exceptions, not only the happy path",
            "Used system signals to automate repeatable operational actions",
            "Standardized workflows so they could be reused across teams",
        ],
        "impact": [
            "Improved end-to-end operational visibility",
            "Reduced reliance on manual checks",
            "Created more consistent, scalable workflows across teams",
        ],
        "lesson": (
            "Visibility only matters if someone can act on it. Good inventory products connect "
            "state, ownership, exceptions, and next actions."
        ),
    },
    "Automation": {
        "icon": "⚡",
        "subtitle": "Removing repetitive operational work",
        "status": "MISSION COMPLETE",
        "problem": (
            "Several order, validation, shipment, and traceability workflows depended on manual "
            "intervention that slowed operations and introduced inconsistency."
        ),
        "constraints": [
            "Automation errors could affect downstream users and operations",
            "Rules varied depending on workflow state and context",
            "Edge cases were common and costly to resolve",
            "Users still needed visibility, control, and recovery paths",
        ],
        "decisions": [
            "Converted repeatable manual decisions into explicit product rules",
            "Added validations and safeguards before automatic actions",
            "Designed observable failure paths rather than silent automation",
            "Kept human judgment for ambiguous or higher-risk exceptions",
        ],
        "impact": [
            "Reduced manual intervention",
            "Improved workflow consistency",
            "Made exception handling easier to understand and scale",
        ],
        "lesson": (
            "The goal is not to automate everything. It is to automate the predictable work and "
            "make the unpredictable work easier for humans to resolve."
        ),
    },
    "Decision Copilot": {
        "icon": "🤖",
        "subtitle": "An AI side project for structured decision-making",
        "status": "SIDE QUEST",
        "problem": (
            "Complex decisions often become a collection of opinions, loose notes, and tradeoffs "
            "that are difficult to compare consistently."
        ),
        "constraints": [
            "AI recommendations need to remain explainable",
            "Inputs can be incomplete or subjective",
            "The tool should assist judgment rather than replace it",
            "The experience needed to stay lightweight enough to actually use",
        ],
        "decisions": [
            "Structured decisions around options, criteria, evidence, and tradeoffs",
            "Used AI to organize reasoning rather than simply output an answer",
            "Kept the decision trail visible to the user",
            "Designed the project as a practical PM tool instead of an AI demo",
        ],
        "impact": [
            "Built a working exploration of AI-assisted product decision-making",
            "Created a reusable framework for comparing complex choices",
            "Expanded hands-on experience building with AI",
        ],
        "lesson": (
            "AI is most useful when it improves the quality of a person's reasoning, not when it "
            "pretends uncertainty does not exist."
        ),
    },
}

SKILLS = {
    "Product": ["Product Strategy", "Roadmapping", "Discovery", "Prioritization", "UAT", "Launch"],
    "Systems": ["Systems Thinking", "APIs", "Event-Driven Systems", "SQL", "Observability", "Integrations"],
    "Operations": ["Manufacturing", "Supply Chain", "Inventory", "Material Flow", "Automation"],
    "Working Style": ["Cross-functional Leadership", "Root Cause Analysis", "User Research", "0→1"],
}


# -----------------------------
# SESSION STATE
# -----------------------------
if "completed_missions" not in st.session_state:
    st.session_state.completed_missions = set()

if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

if "decision_answered" not in st.session_state:
    st.session_state.decision_answered = False

if "scroll_to_top_next" not in st.session_state:
    st.session_state.scroll_to_top_next = False

if "scroll_to_missions" not in st.session_state:
    st.session_state.scroll_to_missions = False


def open_project(project_name):
    st.session_state.selected_project = project_name
    st.session_state.completed_missions.add(project_name)
    st.session_state.scroll_to_top_next = True


def go_home():
    st.session_state.selected_project = None
    st.session_state.scroll_to_top_next = True


# -----------------------------
# CSS
# -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #090d12;
        --panel: #0f151d;
        --panel-2: #121a24;
        --border: #243140;
        --text: #f5f7fa;
        --muted: #8e9baa;
        --accent: #79f2c0;
        --accent-2: #5fd1ff;
        --warning: #ffd166;
    }

    html, body, [class*="css"] {
        font-family: "Inter", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 85% 5%, rgba(95, 209, 255, .08), transparent 26rem),
            radial-gradient(circle at 10% 40%, rgba(121, 242, 192, .05), transparent 30rem),
            var(--bg);
        color: var(--text);
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.2rem;
        padding-bottom: 5rem;
    }

    h1, h2, h3 {
        letter-spacing: -0.035em;
    }

    a {
        text-decoration: none !important;
    }

    .mono {
        font-family: "DM Mono", monospace;
    }

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid var(--border);
        padding-bottom: 1rem;
        margin-bottom: 4.5rem;
        font-family: "DM Mono", monospace;
        font-size: .83rem;
        letter-spacing: .08em;
    }

    .brand {
        color: var(--text);
        font-weight: 500;
    }

    .online {
        color: var(--accent);
    }

    .eyebrow {
        font-family: "DM Mono", monospace;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: .13em;
        font-size: .78rem;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: clamp(3.4rem, 8vw, 7.2rem);
        font-weight: 800;
        letter-spacing: -.065em;
        line-height: .93;
        margin: 0 0 1.4rem;
    }

    .hero-copy {
        color: #c8d0d9;
        font-size: 1.32rem;
        max-width: 750px;
        line-height: 1.55;
        margin-bottom: .7rem;
    }

    .hero-role {
        color: var(--muted);
        font-family: "DM Mono", monospace;
        font-size: .92rem;
        margin-bottom: 2.2rem;
    }

    .section-label {
        font-family: "DM Mono", monospace;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: .12em;
        font-size: .78rem;
        margin: 5rem 0 1.25rem;
    }

    .stat-card {
        border-top: 1px solid var(--border);
        padding: 1.15rem 0 0;
        min-height: 100px;
    }

    .stat-value {
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -.04em;
    }

    .stat-label {
        color: var(--muted);
        font-size: .85rem;
        margin-top: .3rem;
    }

    .mission-card {
        border: 1px solid var(--border);
        background: linear-gradient(145deg, rgba(18,26,36,.95), rgba(11,16,23,.95));
        border-radius: 10px;
        padding: 1.35rem 1.35rem 1.2rem;
        min-height: 190px;
        margin-bottom: .6rem;
        transition: transform .15s ease, border-color .15s ease;
    }

    .mission-card:hover {
        transform: translateY(-2px);
        border-color: #40536a;
    }

    .mission-icon {
        font-size: 1.6rem;
        margin-bottom: 1.8rem;
    }

    .mission-name {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: .45rem;
    }

    .mission-subtitle {
        color: var(--muted);
        font-size: .88rem;
        line-height: 1.5;
        min-height: 44px;
    }

    .mission-status {
        font-family: "DM Mono", monospace;
        color: var(--accent);
        font-size: .68rem;
        letter-spacing: .1em;
        margin-top: 1rem;
    }

    .chip {
        display: inline-block;
        border: 1px solid var(--border);
        background: var(--panel);
        border-radius: 999px;
        padding: .43rem .72rem;
        margin: .22rem .18rem .22rem 0;
        color: #cbd5df;
        font-size: .78rem;
    }

    .terminal {
        background: #070a0e;
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 1.4rem;
        font-family: "DM Mono", monospace;
        font-size: .82rem;
        line-height: 1.85;
        color: #aebac7;
    }

    .terminal .green {
        color: var(--accent);
    }

    .terminal .blue {
        color: var(--accent-2);
    }

    .case-hero {
        border-bottom: 1px solid var(--border);
        padding-bottom: 2rem;
        margin-bottom: 2.5rem;
    }

    .case-title {
        font-size: clamp(2.8rem, 6vw, 5.5rem);
        font-weight: 800;
        letter-spacing: -.055em;
        line-height: .98;
        margin: .5rem 0 1rem;
    }

    .case-subtitle {
        color: var(--muted);
        font-size: 1.15rem;
    }

    .case-block {
        border-top: 1px solid var(--border);
        padding-top: 1rem;
        margin-top: 2.7rem;
    }

    .case-block h3 {
        font-family: "DM Mono", monospace;
        font-size: .78rem;
        text-transform: uppercase;
        letter-spacing: .12em;
        color: var(--accent);
    }

    .case-block p, .case-block li {
        color: #c9d2dc;
        line-height: 1.7;
    }

    .scholar-shell {
        border: 1px solid var(--border);
        background: linear-gradient(145deg, rgba(18,26,36,.95), rgba(10,15,21,.98));
        border-radius: 12px;
        padding: 1.4rem;
        margin-bottom: 1rem;
    }

    .scholar-head {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        align-items: flex-start;
        padding-bottom: 1.2rem;
        border-bottom: 1px solid var(--border);
    }

    .scholar-name {
        font-size: 1.35rem;
        font-weight: 700;
        letter-spacing: -.03em;
    }

    .scholar-meta {
        color: var(--muted);
        font-size: .85rem;
        margin-top: .25rem;
    }

    .pub-card {
        border-bottom: 1px solid var(--border);
        padding: 1.15rem 0;
    }

    .pub-card:last-child {
        border-bottom: none;
    }

    .pub-year {
        font-family: "DM Mono", monospace;
        color: var(--accent);
        font-size: .73rem;
        letter-spacing: .08em;
    }

    .pub-title {
        font-size: 1rem;
        font-weight: 650;
        line-height: 1.45;
        margin: .25rem 0;
    }

    .pub-authors {
        color: var(--muted);
        font-size: .79rem;
        line-height: 1.45;
    }

    .pub-tag {
        display: inline-block;
        font-family: "DM Mono", monospace;
        border: 1px solid #315147;
        color: var(--accent);
        border-radius: 999px;
        padding: .2rem .5rem;
        margin-top: .55rem;
        font-size: .65rem;
        letter-spacing: .05em;
    }

    .footer-wrap {
        border-top: 1px solid var(--border);
        margin-top: 6rem;
        padding-top: 1.5rem;
        color: var(--muted);
        font-family: "DM Mono", monospace;
        font-size: .75rem;
    }

    div[data-testid="stButton"] > button {
        border-radius: 7px;
        min-height: 2.7rem;
        font-weight: 600;
        border: 1px solid #304051;
    }

    div[data-testid="stLinkButton"] > a {
        border-radius: 7px;
        min-height: 2.7rem;
        font-weight: 600;
        border: 1px solid #304051;
    }

    .small-note {
        color: var(--muted);
        font-size: .78rem;
        font-family: "DM Mono", monospace;
    }

    @media (max-width: 700px) {
        .topbar {
            margin-bottom: 3rem;
        }
        .hero-title {
            font-size: 3.6rem;
        }
        .hero-copy {
            font-size: 1.08rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def scroll_to_top():
    components.html(
        """
        <script>
        const root = window.parent.document.querySelector('section.main');
        if (root) {
            root.scrollTo({top: 0, left: 0, behavior: 'instant'});
        } else {
            window.parent.scrollTo({top: 0, left: 0, behavior: 'instant'});
        }
        </script>
        """,
        height=0,
    )


def scroll_to_anchor(anchor_id):
    components.html(
        f"""
        <script>
        const el = window.parent.document.getElementById("{anchor_id}");
        if (el) {{
            el.scrollIntoView({{behavior: "smooth", block: "start"}});
        }}
        </script>
        """,
        height=0,
    )


# -----------------------------
# SHARED UI
# -----------------------------
def render_topbar():
    completed = len(st.session_state.completed_missions)
    st.markdown(
        f"""
        <div class="topbar">
            <div class="brand">VIDYA_OS / PORTFOLIO</div>
            <div class="online">● ONLINE &nbsp; · &nbsp; {completed}/4 MISSIONS EXPLORED</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        """
        <div class="footer-wrap">
            VIDYA_OS v1.0 &nbsp; · &nbsp; BUILT WITH STREAMLIT &nbsp; · &nbsp;
            REQUIREMENTS SUBJECT TO CHANGE WITHOUT WARNING
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_project(project_name):
    project = PROJECTS[project_name]

    if st.session_state.get("scroll_to_top_next"):
        scroll_to_top()
        st.session_state.scroll_to_top_next = False

    render_topbar()

    if st.button("← Return to mission control", key="back_top"):
        go_home()
        st.rerun()

    st.markdown(
        f"""
        <div class="case-hero">
            <div class="eyebrow">{project["status"]} / CASE STUDY</div>
            <div class="case-title">{project["icon"]} {project_name}</div>
            <div class="case-subtitle">{project["subtitle"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="case-block">
            <h3>01 / The problem</h3>
            <p>{project["problem"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="case-block"><h3>02 / Constraints</h3></div>', unsafe_allow_html=True)
    for item in project["constraints"]:
        st.markdown(f"- {item}")

    st.markdown('<div class="case-block"><h3>03 / Product decisions</h3></div>', unsafe_allow_html=True)
    for item in project["decisions"]:
        st.markdown(f"- {item}")

    st.markdown('<div class="case-block"><h3>04 / Impact</h3></div>', unsafe_allow_html=True)
    for item in project["impact"]:
        st.markdown(f"- {item}")

    st.markdown(
        f"""
        <div class="case-block">
            <h3>05 / What I learned</h3>
            <p>{project["lesson"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### System view")
    if project_name == "Factory Launch":
        st.markdown(
            """
            <div class="terminal">
            <span class="green">REAL-WORLD FLOW</span><br>
            Physical process → Operational state → User action → Outcome<br><br>
            <span class="blue">SOFTWARE FLOW</span><br>
            Enterprise systems → Integration layer → Product workflow → Operational execution<br><br>
            <span class="green">PRODUCT LAYER</span><br>
            ownership · orchestration · exception handling · observability
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="terminal">
            SIGNAL → PRODUCT LOGIC → SYSTEM ACTION → OPERATOR VISIBILITY<br><br>
            <span class="green">DESIGN PRINCIPLE:</span>
            make state explicit, ownership obvious, and failures recoverable.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")
    if st.button("✓ Mission reviewed — back to home", type="primary"):
        go_home()
        st.rerun()

    render_footer()


# -----------------------------
# HOME
# -----------------------------
def render_home():
    if st.session_state.get("scroll_to_top_next"):
        scroll_to_top()
        st.session_state.scroll_to_top_next = False

    render_topbar()

    st.markdown('<div class="eyebrow">PRODUCT MANAGER / SYSTEMS BUILDER</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-title">Hi, I’m {NAME}.</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="hero-copy">
            I build software that makes complicated physical operations actually work.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="hero-role">{ROLE} &nbsp; · &nbsp; {TAGLINE}</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns([1.25, 1.15, 1, 1])
    with c1:
        st.link_button("View GitHub ↗", GITHUB_URL, use_container_width=True)
    with c2:
        st.link_button("LinkedIn ↗", LINKEDIN_URL, use_container_width=True)
    with c3:
        st.link_button("Resume ↗", RESUME_URL, use_container_width=True)
    with c4:
        if st.button("Explore ↓", use_container_width=True):
            st.session_state.scroll_to_missions = True

    st.markdown('<div class="section-label">Career telemetry</div>', unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4)
    stats = [
        ("04+", "Years building product at scale"),
        ("MULTI", "Factory + operational environments"),
        ("0→1", "New systems and workflows"),
        ("∞", 'Problems caused by "one edge case"'),
    ]
    for column, (value, label) in zip([s1, s2, s3, s4], stats):
        with column:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-value">{value}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div id="missions"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Choose your mission</div>', unsafe_allow_html=True)

    if st.session_state.get("scroll_to_missions"):
        scroll_to_anchor("missions")
        st.session_state.scroll_to_missions = False

    project_names = list(PROJECTS.keys())
    row1 = st.columns(2)
    row2 = st.columns(2)

    for column, project_name in zip(row1 + row2, project_names):
        project = PROJECTS[project_name]
        completed = project_name in st.session_state.completed_missions
        with column:
            st.markdown(
                f"""
                <div class="mission-card">
                    <div class="mission-icon">{project["icon"]}</div>
                    <div class="mission-name">{project_name}</div>
                    <div class="mission-subtitle">{project["subtitle"]}</div>
                    <div class="mission-status">
                        {"✓ EXPLORED" if completed else "○ READY TO EXPLORE"}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(
                "Open case study →",
                key=f"open_{project_name}",
                use_container_width=True,
            ):
                open_project(project_name)
                st.rerun()

    st.markdown('<div class="section-label">Skill tree</div>', unsafe_allow_html=True)

    skill_cols = st.columns(4)
    for column, (category, skills) in zip(skill_cols, SKILLS.items()):
        with column:
            st.markdown(f"**{category}**")
            chips = "".join([f'<span class="chip">{skill}</span>' for skill in skills])
            st.markdown(chips, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Research archive / publications</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="scholar-shell">
            <div class="scholar-head">
                <div>
                    <div class="scholar-name">Vidya Krishnamoorthy</div>
                    <div class="scholar-meta">
                        Human-centered automation · adaptive driving systems · trust · user preference
                    </div>
                </div>
                <div class="mono" style="color:var(--accent);font-size:.72rem;letter-spacing:.08em;">
                    SCHOLAR_VIEW
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    for pub in PUBLICATIONS:
        st.markdown(
            f"""
            <div class="pub-card">
                <div class="pub-year">{pub["year"]} · {pub["venue"]}</div>
                <div class="pub-title">{pub["title"]}</div>
                <div class="pub-authors">{pub["authors"]}</div>
                <div class="pub-tag">{pub["tag"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Open publication ↗", pub["url"])

    st.markdown("</div>", unsafe_allow_html=True)

    scholar_col, research_note_col = st.columns([1, 2.1])
    with scholar_col:
        st.link_button("View Google Scholar ↗", SCHOLAR_URL, use_container_width=True)
    with research_note_col:
        st.markdown(
            '<div class="small-note">SELECTED WORK · HUMAN-CENTERED AUTOMATION / TRUST / ADAPTIVE SYSTEMS</div>',
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-label">Decision lab / how I think</div>', unsafe_allow_html=True)

    st.markdown(
        """
        Your factory reports recurring inventory discrepancies. Operations wants a manual
        reconciliation workflow immediately. Engineering believes an integration is dropping events.
        **What should the PM do first?**
        """
    )

    choice = st.radio(
        "Choose an approach",
        [
            "Build the manual workaround so users can move faster",
            "Ask engineering to fix the suspected integration",
            "Map where physical and digital state diverge before choosing the solution",
            "Add more dashboards to monitor the discrepancy",
        ],
        index=None,
        label_visibility="collapsed",
    )

    if st.button("Run decision", type="primary", disabled=choice is None):
        st.session_state.decision_answered = True

    if st.session_state.decision_answered and choice:
        if choice.startswith("Map where"):
            st.success("SYSTEM MATCH ✓")
        else:
            st.warning("VALID TACTIC — BUT NOT MY FIRST MOVE")

        st.markdown(
            """
            **My approach:** map the lifecycle first. I would trace the physical movement,
            expected system events, systems of record, timing, and known failure states. That tells
            us whether we have a product gap, integration defect, process problem, or some mix of all
            three.

            The manual workflow or engineering fix may still be the right answer. The point is to
            avoid committing to a solution before we know **where reality diverges from the model**.
            """
        )

    st.markdown('<div class="section-label">Current status</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="terminal">
        $ whoami<br>
        <span class="green">Senior Product Manager</span><br><br>

        $ current_focus<br>
        complex systems · operational software · automation · AI-assisted products<br><br>

        $ next_mission<br>
        <span class="blue">Looking for product problems where software meets the real world.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")
    contact1, contact2 = st.columns([1, 2])
    with contact1:
        st.link_button("Connect on LinkedIn ↗", LINKEDIN_URL, use_container_width=True)
    with contact2:
        st.caption(
            "Replace the placeholder LinkedIn and resume URLs at the top of app.py before publishing."
        )

    render_footer()


# -----------------------------
# ROUTER
# -----------------------------
if st.session_state.selected_project:
    render_project(st.session_state.selected_project)
else:
    render_home()