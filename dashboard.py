from __future__ import annotations

import uuid
from typing import Any

import requests
import streamlit as st


API_DEFAULT = "http://127.0.0.1:8000"


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="SCA — Sovereign Career Architect",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>
    :root {
        --bg: #0b0d11;
        --panel: #12151b;
        --panel-2: #181c23;
        --border: #2a2f39;
        --text: #f3f4f6;
        --muted: #9aa3b2;
        --gold: #d6a84f;
        --red: #8f1d2c;
        --red-2: #b52a3d;
        --green: #45c486;
        --yellow: #e0b74f;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    [data-testid="stSidebar"] {
        background: #0f1217;
        border-right: 1px solid var(--border);
    }

    [data-testid="stSidebar"] * {
        color: var(--text);
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 2rem;
    }

    .brand-mark {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: linear-gradient(135deg, #d6a84f, #8f1d2c);
        font-size: 23px;
        box-shadow: 0 8px 25px rgba(214,168,79,.18);
    }

    .brand-name {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: .02em;
    }

    .brand-sub {
        color: var(--muted);
        font-size: .84rem;
        margin-top: 2px;
    }

    .hero {
        padding: 2rem 2.2rem;
        border-radius: 22px;
        background:
            radial-gradient(circle at 88% 12%, rgba(214,168,79,.10), transparent 22%),
            linear-gradient(135deg, #161a21 0%, #0f1217 100%);
        border: 1px solid var(--border);
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: 2.45rem;
        font-weight: 800;
        letter-spacing: -.03em;
        margin: 0;
    }

    .hero-subtitle {
        color: var(--muted);
        font-size: 1.03rem;
        margin-top: .6rem;
    }

    .hero-accent {
        color: var(--gold);
    }

    .section-title {
        font-size: 1.3rem;
        font-weight: 750;
        margin: 1.4rem 0 .85rem;
    }

    .metric-card {
        background: linear-gradient(145deg, #151920, #11141a);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1.1rem 1.2rem;
        min-height: 115px;
    }

    .metric-label {
        color: var(--muted);
        font-size: .82rem;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        margin-top: .35rem;
    }

    .metric-small {
        color: var(--muted);
        font-size: .82rem;
        margin-top: .25rem;
    }

    .intel-card {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 17px;
        padding: 1rem 1.1rem;
        margin-bottom: .8rem;
    }

    .intel-title {
        font-weight: 750;
        font-size: 1rem;
    }

    .intel-body {
        color: var(--muted);
        margin-top: .35rem;
        line-height: 1.5;
    }

    .tag {
        display: inline-block;
        padding: .42rem .72rem;
        border-radius: 999px;
        background: #211d15;
        border: 1px solid #54462a;
        color: #e5c06b;
        margin: .2rem .25rem .2rem 0;
        font-size: .82rem;
    }

    .priority-high {
        border-left: 4px solid var(--red-2);
    }

    .priority-medium {
        border-left: 4px solid var(--gold);
    }

    .priority-low {
        border-left: 4px solid #5e6878;
    }

    .roadmap-stage {
        color: var(--gold);
        font-size: .78rem;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    .roadmap-skill {
        font-size: 1.02rem;
        font-weight: 700;
        margin-top: .25rem;
    }

    .roadmap-priority {
        color: var(--muted);
        margin-top: .3rem;
    }

    .empty-card {
        background: var(--panel);
        border: 1px dashed var(--border);
        border-radius: 16px;
        padding: 1.2rem;
        color: var(--muted);
    }

    .footer {
        color: #687181;
        font-size: .78rem;
        border-top: 1px solid var(--border);
        padding-top: 1rem;
        margin-top: 2rem;
    }

    div[data-baseweb="tab-list"] {
        gap: 8px;
    }

    button[data-baseweb="tab"] {
        border-radius: 10px 10px 0 0;
    }

    div[data-testid="stMetric"] {
        background: var(--panel);
        border: 1px solid var(--border);
        padding: .7rem;
        border-radius: 14px;
    }

    .stButton > button {
        border-radius: 11px;
        border: 1px solid var(--border);
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #8f1d2c, #b52a3d);
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def api_request(
    method: str,
    path: str,
    base_url: str,
    **kwargs: Any,
) -> tuple[bool, Any]:
    try:
        response = requests.request(
            method=method,
            url=f"{base_url.rstrip('/')}{path}",
            timeout=20,
            **kwargs,
        )
    except requests.RequestException as exc:
        return False, {"error": str(exc)}

    try:
        payload = response.json()
    except ValueError:
        payload = response.text

    if response.ok:
        return True, payload

    return False, {
        "status_code": response.status_code,
        "detail": payload,
    }


def valid_uuid(value: str) -> str | None:
    try:
        return str(uuid.UUID(value.strip()))
    except (ValueError, AttributeError):
        return None


def error_text(payload: Any) -> str:
    if isinstance(payload, dict):
        if "detail" in payload:
            return str(payload["detail"])
        if "error" in payload:
            return str(payload["error"])
    return str(payload)


def collection_count(data: Any) -> int:
    return len(data) if isinstance(data, list) else 0


def render_tags(items: list[Any]) -> None:
    if not items:
        st.markdown(
            '<div class="empty-card">No data available.</div>',
            unsafe_allow_html=True,
        )
        return

    html = "".join(
        f'<span class="tag">{str(item)}</span>'
        for item in items
    )
    st.markdown(html, unsafe_allow_html=True)


def render_collection(
    data: Any,
    empty_message: str = "No records found.",
) -> None:
    if not data:
        st.markdown(
            f'<div class="empty-card">{empty_message}</div>',
            unsafe_allow_html=True,
        )
        return

    if isinstance(data, list):
        for item in data:
            if not isinstance(item, dict):
                st.write(item)
                continue

            title = (
                item.get("name")
                or item.get("title")
                or item.get("job_title")
                or item.get("institution")
                or "Record"
            )

            details = []
            for key in (
                "company_name",
                "issuer",
                "degree_level",
                "field_of_study",
                "employment_type",
                "status",
                "progress",
                "description",
            ):
                value = item.get(key)
                if value not in (None, ""):
                    details.append(f"**{key.replace('_', ' ').title()}:** {value}")

            body = "<br>".join(details)

            st.markdown(
                f"""
                <div class="intel-card">
                    <div class="intel-title">{title}</div>
                    <div class="intel-body">{body or "Record available."}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    elif isinstance(data, dict):
        st.json(data)
    else:
        st.write(data)


# ============================================================
# SESSION
# ============================================================

if "professional_id" not in st.session_state:
    st.session_state.professional_id = ""

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "required_skills" not in st.session_state:
    st.session_state.required_skills = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-mark">🧭</div>
            <div>
                <div class="brand-name">SCA</div>
                <div class="brand-sub">Sovereign Career Architect</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Connection")

    api_url = st.text_input(
        "API URL",
        value=API_DEFAULT,
        label_visibility="visible",
    )

    if st.button("Check API", use_container_width=True):
        ok, data = api_request("GET", "/health", api_url)
        if ok:
            st.success("SCA API online")
        else:
            st.error(error_text(data))

    st.divider()

    st.markdown("### Professional")

    uuid_input = st.text_input(
        "Professional UUID",
        value=st.session_state.professional_id,
        placeholder="Enter UUID",
    )

    if uuid_input.strip():
        normalized = valid_uuid(uuid_input)

        if normalized:
            st.session_state.professional_id = normalized
        else:
            st.warning("Invalid UUID format.")

    if st.session_state.professional_id:
        st.caption(
            f"Active profile: `{st.session_state.professional_id}`"
        )

    st.divider()

    st.caption("SCA V1")
    st.caption("Professional Intelligence Platform")


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">
            Sovereign Career <span class="hero-accent">Architect</span>
        </div>
        <div class="hero-subtitle">
            Transform professional evidence into measurable career intelligence,
            strategic recommendations, and an actionable roadmap.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# CREATE PROFILE
# ============================================================

if not st.session_state.professional_id:

    st.markdown('<div class="section-title">Create Your Career Profile</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="empty-card">Create a Professional profile to activate SCA intelligence.</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    with st.form("create_profile"):

        left, right = st.columns(2)

        with left:
            full_name = st.text_input(
                "Full name",
                placeholder="Anil Khanal",
            )

        with right:
            primary_goal = st.text_input(
                "Primary professional goal",
                placeholder="Become a strong AI/full-stack engineer",
            )

        submitted = st.form_submit_button(
            "Create Professional Profile",
            type="primary",
            use_container_width=True,
        )

        if submitted:

            if not full_name.strip() or not primary_goal.strip():
                st.error("Both fields are required.")
            else:

                ok, data = api_request(
                    "POST",
                    "/professionals",
                    api_url,
                    json={
                        "full_name": full_name.strip(),
                        "primary_goal": primary_goal.strip(),
                    },
                )

                if ok:

                    st.session_state.professional_id = data["id"]

                    st.success("Professional profile created.")

                    st.rerun()

                else:
                    st.error(error_text(data))

    st.stop()


# ============================================================
# LOAD PROFESSIONAL
# ============================================================

professional_id = st.session_state.professional_id

ok, profile = api_request(
    "GET",
    f"/professionals/{professional_id}",
    api_url,
)

if not ok:
    st.error(
        f"Unable to load Professional profile: {error_text(profile)}"
    )
    st.stop()


# ============================================================
# PROFILE HEADER
# ============================================================

st.markdown(
    '<div class="section-title">Professional Intelligence Profile</div>',
    unsafe_allow_html=True,
)

profile_cols = st.columns(3)

with profile_cols[0]:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Professional</div>
            <div class="metric-value">{profile.get("full_name", "—")}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with profile_cols[1]:
    goal = profile.get("primary_goal", "—")
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Primary Goal</div>
            <div class="metric-value" style="font-size:1.2rem;">
                {goal}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with profile_cols[2]:
    created = profile.get("created_at", "—")
    if created and created != "—":
        created = created[:10]

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">Profile Created</div>
            <div class="metric-value">{created}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# LOAD COLLECTIONS
# ============================================================

endpoints = {
    "Skills": f"/professionals/{professional_id}/skills",
    "Education": f"/education/{professional_id}",
    "Experience": f"/experiences/{professional_id}",
    "Projects": f"/projects/{professional_id}",
    "Goals": f"/goals/{professional_id}",
    "Achievements": f"/achievements/{professional_id}",
    "Certificates": f"/certificates/{professional_id}",
    "Timeline": f"/professionals/{professional_id}/timeline",
}

collections: dict[str, Any] = {}

for name, endpoint in endpoints.items():
    success, data = api_request("GET", endpoint, api_url)
    collections[name] = data if success else []


# ============================================================
# INTELLIGENCE ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">Career Intelligence</div>',
    unsafe_allow_html=True,
)

required_skills_text = st.text_input(
    "Target-role skills",
    value=", ".join(st.session_state.required_skills),
    placeholder="Python, FastAPI, SQL, Docker, AWS, Machine Learning, LLMs",
)

if st.button(
    "Run Career Analysis",
    type="primary",
    use_container_width=True,
):

    required_skills = [
        value.strip()
        for value in required_skills_text.split(",")
        if value.strip()
    ]

    st.session_state.required_skills = required_skills

    ok, analysis = api_request(
        "POST",
        f"/career-intelligence/{professional_id}/analysis",
        api_url,
        json={
            "required_skills": required_skills,
        },
    )

    if ok:
        st.session_state.analysis = analysis
        st.success("Career intelligence updated.")
    else:
        st.error(error_text(analysis))


analysis = st.session_state.analysis

if analysis:

    score = analysis.get("career_score", 0)
    completion = analysis.get("profile_completion", 0)
    readiness = analysis.get("career_readiness", 0)
    gaps = analysis.get("skill_gaps", [])

    metric_cols = st.columns(4)

    metrics = [
        ("Career Score", score, "Overall career alignment"),
        ("Profile Completion", completion, "Evidence coverage"),
        ("Career Readiness", readiness, "Readiness signal"),
        ("Skill Gaps", len(gaps), "Missing target capabilities"),
    ]

    for column, (label, value, note) in zip(metric_cols, metrics):
        with column:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-small">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        '<div class="section-title">Skill Gap Analysis</div>',
        unsafe_allow_html=True,
    )

    if gaps:
        render_tags(gaps)
    else:
        st.success("No skill gaps reported.")


# ============================================================
# INTELLIGENCE TABS
# ============================================================

tabs = st.tabs(
    [
        "Overview",
        "Insights",
        "Recommendations",
        "Roadmap",
        "Market",
        "Evidence",
    ]
)


# ------------------------------------------------------------
# OVERVIEW
# ------------------------------------------------------------

with tabs[0]:

    st.markdown(
        '<div class="section-title">Career Overview</div>',
        unsafe_allow_html=True,
    )

    if not analysis:
        st.markdown(
            '<div class="empty-card">Run Career Analysis to activate the intelligence overview.</div>',
            unsafe_allow_html=True,
        )
    else:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Current Position")

            st.write(
                f"**Career Score:** {analysis.get('career_score', '—')}"
            )
            st.write(
                f"**Profile Completion:** {analysis.get('profile_completion', '—')}"
            )
            st.write(
                f"**Career Readiness:** {analysis.get('career_readiness', '—')}"
            )

        with col2:
            st.markdown("#### Immediate Gaps")

            gaps = analysis.get("skill_gaps", [])

            if gaps:
                for gap in gaps:
                    st.warning(gap)
            else:
                st.success("No immediate skill gaps reported.")


# ------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------

with tabs[1]:

    st.markdown(
        '<div class="section-title">Career Insights</div>',
        unsafe_allow_html=True,
    )

    ok, insights = api_request(
        "GET",
        f"/career-intelligence/{professional_id}/insights",
        api_url,
    )

    if not ok:
        st.error(error_text(insights))
    elif not insights:
        st.markdown(
            '<div class="empty-card">No insights available yet.</div>',
            unsafe_allow_html=True,
        )
    else:

        for insight in insights:

            st.markdown(
                f"""
                <div class="intel-card">
                    <div class="intel-title">
                        {insight.get("title", "Insight")}
                    </div>
                    <div class="intel-body">
                        {insight.get("description", "")}
                        <br><br>
                        <strong>Category:</strong>
                        {insight.get("category", "")}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------------------------------------------------
# RECOMMENDATIONS
# ------------------------------------------------------------

with tabs[2]:

    st.markdown(
        '<div class="section-title">Strategic Recommendations</div>',
        unsafe_allow_html=True,
    )

    ok, recommendations = api_request(
        "GET",
        f"/career-intelligence/{professional_id}/recommendations",
        api_url,
    )

    if not ok:
        st.error(error_text(recommendations))
    elif not recommendations:
        st.markdown(
            '<div class="empty-card">No recommendations available yet.</div>',
            unsafe_allow_html=True,
        )
    else:

        for recommendation in recommendations:

            priority = str(
                recommendation.get("priority", "NORMAL")
            ).upper()

            css_class = "priority-low"

            if priority == "HIGH":
                css_class = "priority-high"
            elif priority == "MEDIUM":
                css_class = "priority-medium"

            st.markdown(
                f"""
                <div class="intel-card {css_class}">
                    <div class="intel-title">
                        {priority} — {recommendation.get("action", "Recommendation")}
                    </div>
                    <div class="intel-body">
                        {recommendation.get("reason", "")}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------------------------------------------------
# ROADMAP
# ------------------------------------------------------------

with tabs[3]:

    st.markdown(
        '<div class="section-title">Career Roadmap</div>',
        unsafe_allow_html=True,
    )

    ok, roadmap = api_request(
        "GET",
        f"/career-intelligence/{professional_id}/roadmap",
        api_url,
    )

    if not ok:
        st.error(error_text(roadmap))
    elif not roadmap:
        st.markdown(
            '<div class="empty-card">No roadmap items available yet.</div>',
            unsafe_allow_html=True,
        )
    else:

        for index, item in enumerate(roadmap, start=1):

            st.markdown(
                f"""
                <div class="intel-card">
                    <div class="roadmap-stage">
                        Stage {index} · {item.get("stage", "Learning")}
                    </div>
                    <div class="roadmap-skill">
                        {item.get("skill", "Skill")}
                    </div>
                    <div class="roadmap-priority">
                        Priority: {item.get("priority", "—")}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------------------------------------------------
# MARKET
# ------------------------------------------------------------

with tabs[4]:

    st.markdown(
        '<div class="section-title">Market Intelligence</div>',
        unsafe_allow_html=True,
    )

    ok, market = api_request(
        "GET",
        f"/career-intelligence/{professional_id}/market-intelligence",
        api_url,
    )

    if not ok:

        st.error(error_text(market))

    else:

        matched = market.get("matched_skills", [])
        opportunities = market.get("opportunity_skills", [])
        high_priority = market.get(
            "high_priority_opportunities",
            [],
        )

        c1, c2 = st.columns(2)

        with c1:

            st.markdown("#### Market-Matched Skills")
            render_tags(matched)

            st.markdown("#### Opportunity Skills")
            render_tags(opportunities)

        with c2:

            st.markdown("#### High-Priority Opportunities")

            if high_priority:

                for opportunity in high_priority:

                    st.markdown(
                        f"""
                        <div class="intel-card priority-high">
                            <div class="intel-title">
                                {opportunity}
                            </div>
                            <div class="intel-body">
                                High-priority market signal.
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            else:
                st.markdown(
                    '<div class="empty-card">No high-priority opportunities reported.</div>',
                    unsafe_allow_html=True,
                )


# ------------------------------------------------------------
# EVIDENCE
# ------------------------------------------------------------

with tabs[5]:

    st.markdown(
        '<div class="section-title">Professional Evidence</div>',
        unsafe_allow_html=True,
    )

    summary_cols = st.columns(8)

    for column, name in zip(
        summary_cols,
        [
            "Skills",
            "Education",
            "Experience",
            "Projects",
            "Goals",
            "Achievements",
            "Certificates",
            "Timeline",
        ],
    ):
        with column:
            st.metric(
                name,
                collection_count(collections.get(name)),
            )

    evidence_tabs = st.tabs(
        [
            "Skills",
            "Education",
            "Experience",
            "Projects",
            "Goals",
            "Achievements",
            "Certificates",
            "Timeline",
        ]
    )

    for tab, name in zip(
        evidence_tabs,
        [
            "Skills",
            "Education",
            "Experience",
            "Projects",
            "Goals",
            "Achievements",
            "Certificates",
            "Timeline",
        ],
    ):
        with tab:
            render_collection(
                collections.get(name),
                f"No {name.lower()} records found.",
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        SCA V1 · Sovereign Career Architect · Professional Intelligence Platform
        · Developed by ANIREX AI
    </div>
    """,
    unsafe_allow_html=True,
)
