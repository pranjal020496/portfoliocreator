from pathlib import Path
import base64
import mimetypes
import textwrap
import streamlit as st

st.set_page_config(
    page_title="Dr. Pranjal Nandi | Data • AI • HPC • Materials",
    page_icon="◎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"
CHAPTER_DIR = ASSET_DIR / "thesis_chapters"
SCREEN_DIR = ASSET_DIR / "project_screenshots"
ACH_DIR = ASSET_DIR / "achievements"

GITHUB_URL = "https://github.com/pranjal020496?tab=repositories"
LINKEDIN_URL = "https://www.linkedin.com/in/pranjal222"
EMAIL_URL = "mailto:pranjal222@gmail.com"

SUGARBELLY_REPO = "https://github.com/pranjal020496/SugarBelly"
ASTROSPECTRA_REPO = "https://github.com/pranjal020496/Astrospectra-ml"
DOC_ASSISTANT_REPO = "https://github.com/pranjal020496/AI-Document-Summarising-Assistant"
ASTROCHEM_REPO = "https://github.com/pranjal020496/Astrochem-mini"

ASTRO_OVERVIEW = "https://raw.githubusercontent.com/pranjal020496/Astrospectra-ml/main/docs/screenshots/overview.png"
ASTRO_MODEL = "https://raw.githubusercontent.com/pranjal020496/Astrospectra-ml/main/docs/screenshots/model_comparison.png"
ASTRO_ANOMALY = "https://raw.githubusercontent.com/pranjal020496/Astrospectra-ml/main/docs/screenshots/anomaly_detection.png"



# PROJECT_SHOWCASE_UPDATE_START
RISKAUDIT_REPO = "https://github.com/pranjal020496/riskaudit-sme-credit-validation"
GRIDSHOCK_REPO = "https://github.com/pranjal020496/gridshock-energy-credit-stress-testing"
SIGNALCOVER_REPO = "https://github.com/pranjal020496/signalcover-telecom-outage-insurance"
RETAILPULSE_REPO = "https://github.com/pranjal020496/Retailpulse_sql"

DATA_PROJECTS = [
    {
        "name": "RiskAudit — SME Credit Model Validation",
        "repo": RISKAUDIT_REPO,
        "question": "Can a bank trust its SME probability-of-default model?",
        "solution": (
            "Independently validates a logistic regression credit-risk model against a "
            "decision-tree challenger, testing calibration, stability, sector performance "
            "and stress sensitivity before reaching an approval decision."
        ),
    },
    {
        "name": "GridShock — Energy-to-Credit Stress Testing",
        "repo": GRIDSHOCK_REPO,
        "question": (
            "How would a prolonged energy-price shock affect SME cash flow and a bank's credit losses?"
        ),
        "solution": (
            "Forecasts electricity prices, translates energy, interest-rate and demand shocks "
            "into borrower cash flow and default risk, and estimates portfolio losses through "
            "correlated Monte Carlo simulation."
        ),
    },
    {
        "name": "SignalCover — Telecom Outage Insurance Modelling",
        "repo": SIGNALCOVER_REPO,
        "question": (
            "Can broadband performance data detect genuine interruptions and support fair, automatic payouts?"
        ),
        "solution": (
            "Compares outage-detection methods and connects the selected trigger to customer "
            "segmentation, insurance pricing, basis-risk measurement and simulated portfolio losses."
        ),
    },
    {
        "name": "Sugar Belly — Public-Health Forecasting",
        "repo": SUGARBELLY_REPO,
        "question": (
            "How might obesity levels change by 2030 under different sugar-availability scenarios?"
        ),
        "solution": (
            "Combines WHO and FAOSTAT data, standardises country-year records, benchmarks predictive "
            "models and presents historical trends and future scenarios in an interactive dashboard."
        ),
    },
    {
        "name": "AstroSpectra ML Workbench",
        "repo": ASTROSPECTRA_REPO,
        "question": (
            "Can astronomical spectra be classified reliably while also identifying unusual observations?"
        ),
        "solution": (
            "Processes SDSS FITS spectra onto a common wavelength grid, compares classical models "
            "with a neural network and adds anomaly detection for researcher review."
        ),
    },
    {
        "name": "RetailPulse — SQL Commerce Analytics",
        "repo": RETAILPULSE_REPO,
        "question": (
            "How can raw e-commerce transactions be converted into reliable business metrics?"
        ),
        "solution": (
            "Builds a PostgreSQL analytical layer with relational modelling, automated quality checks, "
            "reusable views, indexes, CTEs and window functions for customer, product and revenue analysis."
        ),
    },

]

PROJECT_REEL_IMAGES = [
    ("local", "riskaudit-executive.png", "RiskAudit — Executive validation"),
    ("local", "gridshock-scenario-losses.png", "GridShock — Scenario losses"),
    ("local", "signalcover-detection.png", "SignalCover — Outage detection"),
    ("local", "sugarbelly_dashboard_overview.png", "Sugar Belly — Executive overview"),
    ("remote", ASTRO_MODEL, "AstroSpectra — Model comparison"),
    ("local", "riskaudit-calibration.png", "RiskAudit — Calibration"),
    ("local", "gridshock-energy-fan.png", "GridShock — Energy simulation"),
    ("local", "signalcover-basis-risk.png", "SignalCover — Basis risk"),
    (
        "local",
        "sugarbelly_ml_sugar_sensitivity_forecast.png",
        "Sugar Belly — 2030 scenarios",
    ),
    ("remote", ASTRO_ANOMALY, "AstroSpectra — Anomaly detection"),
    ("local", "riskaudit-scenarios.png", "RiskAudit — Stress scenarios"),
    ("local", "gridshock-sector-losses.png", "GridShock — Sector concentration"),
    ("local", "signalcover-loss-distribution.png", "SignalCover — Loss distribution"),
    ("local", "signalcover-sector-risk.png", "SignalCover — Sector risk"),
]
# PROJECT_SHOWCASE_UPDATE_DATA_END

def html(markup: str) -> None:
    st.html(textwrap.dedent(markup).strip())


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8") if path.exists() else ""


def data_img(path: Path, alt: str, css_class: str) -> str:
    if not path.exists():
        return f'<div class="image-placeholder">Add image: {path.name}</div>'
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    return f'<img class="{css_class}" src="data:{mime};base64,{b64(path)}" alt="{alt}">'


def profile_image() -> str:
    for filename in ["profile_photo.png", "profile_photo.jpg", "profile_photo.jpeg"]:
        path = ASSET_DIR / filename
        if path.exists():
            return data_img(path, "Dr. Pranjal Nandi", "hero-photo")
    return '<div class="hero-photo placeholder">PN</div>'


def local_img(filename: str, alt: str) -> str:
    path = SCREEN_DIR / filename
    if not path.exists():
        return f'<div class="screenshot-placeholder">Add screenshot: {filename}</div>'
    return data_img(path, alt, "screenshot-img")


def remote_img(url: str, alt: str) -> str:
    return f'<img class="screenshot-img" src="{url}" alt="{alt}" loading="lazy">'


def screenshot_carousel(slides: list[tuple[str, str, str]]) -> str:
    if not slides:
        return '<div class="screenshot-placeholder">Add screenshots later</div>'

    slide_html = ""
    for image_html, title, caption in slides:
        slide_html += f'''
        <div class="project-screenshot-slide">
          {image_html}
          <div class="screenshot-caption">
            <b>{title}</b>
            <span>{caption}</span>
          </div>
        </div>
        '''

    return f'''
    <div class="project-screenshot-carousel" aria-label="Project screenshot slideshow">
      <div class="project-screenshot-track">
        {slide_html}
      </div>
    </div>
    '''




def project_summary_cards(projects: list[dict[str, str]]) -> str:
    cards = []
    for number, project in enumerate(projects, start=1):
        cards.append(
            f"""
            <article class="project-summary-card">
                <div class="project-summary-head">
                    <div class="project-summary-title">
                        <span>{number:02d}</span>
                        <h3>{project["name"]}</h3>
                    </div>
                    <a
                        class="project-github-link"
                        href="{project["repo"]}"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        GitHub ↗
                    </a>
                </div>
                <div class="project-detail">
                    <div class="project-detail-label">Business question</div>
                    <p class="project-business-question">{project["question"]}</p>
                </div>
                <div class="project-detail">
                    <div class="project-detail-label">How it solves it</div>
                    <p class="project-solution">{project["solution"]}</p>
                </div>
            </article>
            """
        )
    return "\n".join(cards)


def project_screenshot_reel(images: list[tuple[str, str, str]]) -> str:
    cards = []
    for image_type, value, title in images:
        image_html = local_img(value, title) if image_type == "local" else remote_img(value, title)
        cards.append(
            f"""
            <figure class="project-reel-card">
                {image_html}
                <figcaption class="project-reel-label">{title}</figcaption>
            </figure>
            """
        )

    card_html = "\n".join(cards)
    return f"""
    <div class="project-reel-shell" aria-label="Selected project screenshots">
        <div class="project-reel-track">
            <div class="project-reel-group">{card_html}</div>
            <div class="project-reel-group" aria-hidden="true">{card_html}</div>
        </div>
    </div>
    """
# PROJECT_SHOWCASE_UPDATE_HELPERS_END

def achievement_photo(filename: str, label: str) -> str:
    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        path = ACH_DIR / f"{filename}{ext}"
        if path.exists():
            return data_img(path, label, "achievement-img")
    return f'<div class="achievement-placeholder"><span>{label}</span><small>Add photo later</small></div>'


def achievement_carousel(folder_name: str, label: str) -> str:
    folder = ACH_DIR / folder_name

    image_files = []
    if folder.exists():
        for pattern in ["*.jpg", "*.jpeg", "*.png", "*.webp"]:
            image_files.extend(sorted(folder.glob(pattern)))

    if not image_files:
        return f'''
        <div class="achievement-placeholder">
          <span>{label}</span>
          <small>Add photos inside assets/achievements/{folder_name}</small>
        </div>
        '''

    # Duplicate images so the right-to-left motion loops smoothly.
    loop_images = image_files + image_files

    slides = ""
    for img_path in loop_images:
        slides += f'''
        <div class="achievement-slide">
          {data_img(img_path, label, "achievement-marquee-img")}
        </div>
        '''

    return f'''
    <div class="achievement-marquee" aria-label="{label}">
      <div class="achievement-track">
        {slides}
      </div>
    </div>
    '''


def download_file(label: str, path: Path, filename: str) -> None:
    if path.exists():
        st.download_button(
            label=label,
            data=path.read_bytes(),
            file_name=filename,
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.info(f"Missing {path.name}")


def pdf_download_link(filename: str, label: str = "Download Project") -> str:
    path = CHAPTER_DIR / filename
    if not path.exists():
        return f'<span class="download-inline missing">Missing: {filename}</span>'
    return f'<a class="primary download-inline" download="{path.name}" href="data:application/pdf;base64,{b64(path)}">{label}</a>'

chapter_data = [
    ("03_hafnia_rram_structure_stoichiometry_dielectric.pdf", "Download Project — Hafnia RRAM", "Structure, stoichiometry and dielectric function."),
    ("04_xenon_clusters_pressure_charge_eels.pdf", "Download Project — Xenon Clusters", "Pressure and charge effects on EELS spectra."),
    ("05_lsmo_antisite_defects_haadf_quantification.pdf", "Download Project — LSMO Defects", "HAADF-STEM defect quantification."),
]

html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
  --page: #F5F6F8;
  --paper: #FFFFFF;
  --ink: #111827;
  --muted: #4B5563;
  --soft: #F1F5F9;
  --line: #E5E7EB;
  --line-strong: #CBD5E1;
  --navy: #0B1220;
  --blue: #1E3A8A;
  --blue-dark: #1E3A8A;
  --cyan: #1E3A8A;
  --shadow: 0 24px 70px rgba(15, 23, 42, .08);
  --max: 3000px;
}

html { scroll-behavior: smooth; scroll-padding-top: 92px; }
html, body, [class*="css"] { font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif; }

.stApp {
  background:
    radial-gradient(circle at 50% -8%, rgba(29, 78, 216, .10), transparent 34rem),
    radial-gradient(circle at 0% 30%, rgba(14, 116, 144, .06), transparent 24rem),
    linear-gradient(180deg, #F8FAFC 0%, #F5F6F8 50%, #F3F4F6 100%);
  color: var(--ink);
}

.block-container { max-width: 100% !important; padding: 0 !important; }
#MainMenu, header, footer, div[data-testid="stToolbar"] { visibility: hidden; height: 0; }

.page-shell {
  max-width: var(--max);
  margin: 0 auto;
  padding: 0 clamp(2rem, 5vw, 4.6rem); text-align: center;
}
.site-nav {
  position: sticky;
  top: 0;
  z-index: 50;
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, .90);
  backdrop-filter: blur(16px);
}

.nav-inner {
  max-width: var(--max);
  margin: 0 auto;
  padding: .82rem clamp(2rem, 5vw, 4.6rem);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .55rem;
  flex-wrap: wrap;
}

.nav-inner a {
  color: var(--muted) !important;
  text-decoration: none !important;
  font-weight: 850;
  font-size: .88rem;
  padding: .56rem .82rem;
  border-radius: 999px;
  border: 1px solid transparent;
}

.nav-inner a:hover { color: var(--blue-dark) !important; background: var(--soft); border-color: var(--line); }
.nav-inner a.external { color: var(--blue-dark) !important; border-color: #BFDBFE; background: #EFF6FF; }

.hero {
  min-height: auto;
  display: grid;
  grid-template-columns: minmax(260px, 390px) minmax(0, 1150px);

  column-gap: clamp(2rem, 5vw, 5rem);
  row-gap: 1rem;

  align-items: center;
  justify-content: center;
  padding: clamp(1rem, 3vw, 2rem) 0 1rem;
  margin: 0 auto;
}
.hero-copy { text-align: left; }
     
.hero-photo {
  width: 100%;
  max-width: 390px;
  aspect-ratio: 4 / 5;
  object-fit: cover;
  object-position: center top;
  border-radius: 34px;
  border: 1px solid var(--line-strong);
  box-shadow: var(--shadow);
  background: var(--soft);
}
.hero-photo.placeholder { display: grid; place-items: center; font-size: 4rem; font-weight: 900; color: var(--blue-dark); }

.hero-copy { text-align: left; }


.hero-title {
  color: var(--navy);
  font-size: clamp(3.3rem, 6.5vw, 7.4rem);
  line-height: .88;
  letter-spacing: 0em;
  margin: 0 0 1.15rem;
  white-space: nowrap;
}

.role {
  width: min(80vw, 1040px);
  color: var(--blue-dark);
  font-size: clamp(1.2rem, 2.0vw, 2.2rem);
  line-height: 1.08;
  letter-spacing: -.04em;
  font-weight: 600;
  margin: 0 0 1.1rem;
}
     
.role-kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.95rem;
  width: min(100%, 1220px);
  margin: 0 0 1.3rem;
}

.role-kpi {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 1rem 1.1rem;
  box-shadow: 0 12px 32px rgba(15,23,42,.05);
  min-height: 92px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.role-kpi span {
  color: var(--blue-dark);
  font-size: 0.78rem;
  font-weight: 900;
  letter-spacing: 0.12em;
  margin-bottom: 0.35rem;
}

.role-kpi b {
  color: var(--blue-dark);
  font-size: clamp(1rem, 1.25vw, 1.35rem);
  line-height: 1.15;
  font-weight: 800;
}


.role span { color: var(--blue-dark); }

.intro-text {
  color: var(--muted);
  font-size: clamp(1.06rem, 1.2vw, 1.22rem);
  line-height: 1.75;
  max-width: 1220px;
  margin: 1.2rem 0 0;
  text-align: left;
}

.degree-strip { display: grid; grid-template-columns: repeat(3, 1fr); gap: .95rem; margin: 1.5rem 0 0; }
.degree-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 22px;
  padding: 1rem;
  box-shadow: 0 12px 32px rgba(15,23,42,.05);
  display: grid;
  grid-template-columns: 52px 1fr;
  gap: .85rem;
  align-items: center;
}
.uni-logo {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  background: linear-gradient(135deg, var(--navy), var(--blue-dark));
  color: white;
  display: grid;
  place-items: center;
  font-weight: 950;
  letter-spacing: -.04em;
}
.degree-card b { display: block; color: var(--navy); line-height: 1.15; }
.degree-card span { display: block; color: var(--muted); font-size: .88rem; margin-top: .22rem; line-height: 1.25; }

.expertise-panel {margin-top: auto; padding: clamp(3rem, 4vw, 6rem) 0 clamp(2.5rem, 5vw, 4.5rem); }
.expertise-title { text-align: center; max-width: 1200px; margin: 0 auto 1.5rem; }

.expertise-title h2 { color: var(--navy); font-size: clamp(2rem, 4vw, 4.2rem); letter-spacing: -.04em; line-height: .95; margin: 0 0 .65rem; }
.expertise-title p { color: var(--muted); margin: 0 auto; font-size: 1.18rem; line-height: 1.6; max-width: 780px; }

.choice-grid { display: flex; justify-content: center; gap: .9rem; flex-wrap: wrap; } .choice { width: 360px; }
.choice {
  min-height: 202px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid var(--line);
  border-radius: 24px;
  background: var(--paper);
  color: var(--ink) !important;
  text-decoration: none !important;
  padding: 1.1rem;
  text-align: left;
  box-shadow: var(--shadow);
  transition: transform .24s ease, border-color .24s ease, background .24s ease;
}
.choice:hover { transform: translateY(-6px); border-color: #93C5FD; background: #FBFDFF; }
.choice-number { color: var(--blue-dark); font-size: .82rem; font-weight: 950; letter-spacing: .12em; text-transform: uppercase; }
.choice h3 { color: var(--blue-dark); font-size: clamp(1.12rem, 1.45vw, 1.42rem); line-height: 1.04; letter-spacing: -.05em; margin: .65rem 0 .45rem; text-align: center;}
.choice p { color: var(--muted); font-size: .98rem; line-height: 1.45; margin: 0; text-align: center; }
.open-link { color: var(--blue-dark); font-weight: 900; margin-top: .9rem; }

.proof-strip { display: grid; grid-template-columns: repeat(4, 1fr); gap: .95rem; padding: 0 0 clamp(2.6rem, 5vw, 4.5rem); }
.metric { border: 1px solid var(--line); border-radius: 22px; background: var(--paper); padding: 1.15rem; box-shadow: var(--shadow); text-align: center; }
.metric b { display: block; color: var(--blue-dark); font-size: clamp(1.75rem, 2.3vw, 2.35rem); letter-spacing: -.06em; line-height: 1; }
.metric span { display: block; color: var(--muted); font-weight: 650; margin-top: .35rem; }

.branch { padding: clamp(7rem, 11vw, 10rem) 0 clamp(3.5rem, 7vw, 6.4rem); border-top: 1px solid var(--line); }
.branch-head { text-align: center; max-width: none; margin: 0 auto 5rem; }
.branch-index { width: 58px; height: 58px; border-radius: 18px; background: linear-gradient(135deg, var(--navy), var(--blue-dark)); color: white; display: grid; place-items: center; font-weight: 950; box-shadow: 0 18px 36px rgba(30,58,138,.18); margin: 0 auto 1rem; }
.branch-head h2 { color: var(--navy); font-size: clamp(2.9rem, 5vw, 5.1rem); line-height: .9; letter-spacing: -.03em; margin: 0 0 .85rem; }
.branch-head p { color: var(--muted); font-size: 1.18rem; line-height: 1.62; margin: 0 auto; max-width: 760px; }
.branch-content {
  max-width: 1700px;
  margin: 0 auto;
  display: grid;
  gap: 5rem;
}

.project-case { border: 1px solid var(--line); border-radius: 34px; background: var(--paper); box-shadow: var(--shadow); padding: clamp(1rem, 2vw, 1.8rem); display: grid; gap: 1.15rem; }
.project-topline { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; border-bottom: 1px solid var(--line); padding-bottom: 1rem; }
.project-case h3 { color: var(--blue-dark); font-size: clamp(2.1rem, 4vw, 4.4rem); line-height: .9; letter-spacing: -.03em; margin: .35rem 0 .7rem; }
.project-case p { color: var(--muted); font-size: 1.13rem; line-height: 1.65; max-width: none; }

.project-links { display: flex; gap: .7rem; flex-wrap: wrap; justify-content: center; }
.project-links a,
.contact-links a {
  text-decoration: none !important;
  color: var(--navy) !important;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: .86rem 1.12rem;
  font-weight: 850;
  font-size: .98rem;
  box-shadow: 0 12px 32px rgba(15,23,42,.06);
}
.project-links a.primary,
.contact-links a.primary { background: linear-gradient(135deg, var(--navy), var(--blue-dark)); color: white !important; border-color: transparent; }

.flow { display: grid; grid-template-columns: repeat(6, 1fr); gap: 1rem; }
.flow.five { grid-template-columns: repeat(5, 1fr); }
.flow.four { grid-template-columns: repeat(4, 1fr); }

.workflow-title {
  text-align: center;
  margin: 1rem 0 .9rem;
}

.workflow-title h4 {
  color: var(--blue-dark);
  font-size: clamp(1.28rem, 1.7vw, 1.78rem);
  line-height: 1.02;
  letter-spacing: -.03em;
  margin: 0;
  text-align: center;
}

.flow + .card-grid {
  margin-top: 1.5rem;
}     

.step { border: 1px solid var(--line); border-radius: 18px; background: #F8FAFC; padding: 1rem; }
.step b { display: block; color: var(--blue-dark); font-size: .82rem; text-transform: uppercase; letter-spacing: .09em; margin-bottom: 0.5rem; text-align: center; }
.step span { color: var(--muted); font-weight: 650; line-height: 1.35; text-align: center; display: block; }

.card-grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 1rem; }
.card-grid.three { grid-template-columns: repeat(3, minmax(0,1fr)); }
.card { border: 1px solid var(--line); border-radius: 24px; background: #FBFDFF; box-shadow: 0 12px 36px rgba(15,23,42,.05); padding: clamp(1.2rem, 1.65vw, 1.55rem); }
.card h4, .card h3 { color: var(--blue-dark); font-size: clamp(1.28rem, 1.7vw, 1.78rem); line-height: 1.02; letter-spacing: -.03em; margin: 0 0 .8rem; text-align: center; }
.card p, .card li { color: var(--muted); font-size: clamp(1rem, 1.05vw, 1.1rem); line-height: 1.6; text-align: center; }
.card ul { margin-bottom: 0; padding-left: 1.2rem; }

.tag-row { display: flex; gap: .42rem; flex-wrap: wrap; margin-top: .95rem; margin-bottom: 1.2rem;}
.tag { color: var(--blue-dark); background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 999px; padding: .36rem .6rem; font-size: .78rem; font-weight: 850; }

.screenshot-title { text-align: center; margin: 1rem 0 .2rem; }
.screenshot-title h4 { color: var(--navy); font-size: clamp(1.5rem, 2.5vw, 2.4rem); letter-spacing: -.06em; margin: 0 0 .35rem; }
.screenshot-title p { margin: 0 auto; color: var(--muted); max-width: 720px; }
.gallery { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 1rem; }
.screenshot-card { border: 1px solid var(--line); border-radius: 22px; overflow: hidden; background: var(--paper); box-shadow: 0 14px 44px rgba(15,23,42,.06); }
.screenshot-img { width: 100%; display: block; background: #F8FAFC; }
.screenshot-caption { padding: 1rem 1.1rem 1.15rem; }
.screenshot-caption b { display: block; font-size: 1.05rem; margin-bottom: .35rem; color: var(--navy); }
.screenshot-caption span { color: var(--muted); line-height: 1.45; }
.screenshot-placeholder, .image-placeholder { min-height: 240px; display: grid; place-items: center; background: #F8FAFC; color: var(--muted); }
.center-button { display: flex; justify-content: center; margin-top: .5rem; }

.project-screenshot-carousel {
  width: min(100%, 980px);
  margin: 0 auto;
  border: 1px solid var(--line);
  border-radius: 24px;
  background: var(--paper);
  box-shadow: 0 14px 44px rgba(15,23,42,.06);
  overflow: hidden;
}

.project-screenshot-track {
  display: flex;
  width: 100%;
  animation: project-screenshot-slide 9s ease-in-out infinite;
}



.project-screenshot-slide {
  min-width: 100%;
  flex: 0 0 100%;
  background: var(--paper);
}

.project-screenshot-slide .screenshot-img {
  width: 100%;
  max-height: 580px;
  object-fit: contain;
  display: block;
  background: #F8FAFC;
}

.project-screenshot-slide .screenshot-caption {
  text-align: center;
}

@keyframes project-screenshot-slide {
  0% { transform: translateX(0%); }
  30% { transform: translateX(0%); }

  34% { transform: translateX(-100%); }
  63% { transform: translateX(-100%); }

  67% { transform: translateX(-200%); }
  96% { transform: translateX(-200%); }

  100% { transform: translateX(0%); }
}

.achievement-grid { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 1rem; }
.achievement-card { border: 1px solid var(--line); border-radius: 24px; background: var(--paper); box-shadow: var(--shadow); overflow: hidden; }

.achievement-marquee {
  width: 100%;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  background: #F8FAFC;
  position: relative;
}

.achievement-track {
  height: 100%;
  display: flex;
  width: 100%;
  animation: achievement-slide-show 15s ease-in-out infinite;
}
.achievement-card:hover .achievement-track {
  animation-play-state: paused;
}
     

.achievement-slide {
  min-width: 100%;
  height: 100%;
  flex: 0 0 100%;
}

.achievement-marquee-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

@keyframes achievement-slide-show {
  0%   { transform: translateX(0%); }
  14%  { transform: translateX(0%); }

  18%  { transform: translateX(-100%); }
  32%  { transform: translateX(-100%); }

  36%  { transform: translateX(-200%); }
  50%  { transform: translateX(-200%); }

  54%  { transform: translateX(-300%); }
  68%  { transform: translateX(-300%); }

  72%  { transform: translateX(-400%); }
  86%  { transform: translateX(-400%); }

  100% { transform: translateX(0%); }
}

.achievement-img, .achievement-placeholder { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; background: #F8FAFC; }
.achievement-placeholder { display: grid; place-items: center; text-align: center; color: var(--muted); }
.achievement-placeholder span { font-weight: 900; color: var(--blue-dark); }
.achievement-placeholder small { display: block; color: var(--muted); margin-top: .25rem; }
.achievement-caption { padding: 1rem; }
.achievement-caption b {
  color: var(--blue-dark);
  display: block;
  margin-bottom: .35rem;
  font-size: clamp(1.4rem, 1.6vw, 1.8rem);
  line-height: 1.15;
  font-weight: 850;
}
.achievement-caption span { color: var(--muted); line-height: 1.45; }


.hpc-map-panel {
  border: 1px solid var(--line);
  border-radius: 34px;
  background:
    radial-gradient(circle at top left, rgba(59, 130, 246, 0.10), transparent 32%),
    var(--paper);
  box-shadow: var(--shadow);
  padding: clamp(1.2rem, 2.6vw, 2.4rem);
  display: grid;
  gap: 1.6rem;
}

.hpc-map-header {
  max-width: 2000px;
}

.hpc-map-header h3 {
  margin: 0;
  color: var(--blue-dark);
  font-size: clamp(1.2rem, 2.6vw, 2.5rem);
  letter-spacing: -0.02em;
  line-height: 1.05;
  text-align: justify;
}

.hpc-map-header p {
  margin: .65rem 0 0;
  color: var(--muted);
  font-size: 1.02rem;
  line-height: 1.65;
}

.hpc-proof-row {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: .9rem;
}

.hpc-proof {
  border: 1px solid rgba(30, 58, 138, 0.18);
  border-radius: 22px;
  background: #F8FAFC;
  padding: 1rem;
}

.hpc-proof b {
  display: block;
  color: var(--blue-dark);
  font-size: clamp(1.45rem, 2.4vw, 2.15rem);
  line-height: 1;
  letter-spacing: -0.05em;
  text-align: center;
}

.hpc-proof span {
  display: block;
  margin-top: .35rem;
  color: var(--muted);
  font-weight: 750;
  font-size: 1.2rem;
  text-align: center;   
}

.hpc-capability-map {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
  align-items: stretch;
}

.hpc-capability-column {
  display: grid;
  gap: 1rem;
}


.hpc-skill-card {
  border: 1px solid var(--line);
  border-radius: 24px;
  background: white;
  padding: 1.05rem;
  min-height: 155px;
}

.hpc-skill-card .num {
  display: inline-grid;
  place-items: center;
  width: 2rem;
  height: 2rem;
  border-radius: 999px;
  background: #DBEAFE;
  color: var(--blue-dark);
  font-weight: 950;
  margin-bottom: .7rem;
}

.hpc-skill-card h4 {
  margin: 0 0 .55rem;
  color: var(--blue-dark);
  font-size: 1.5rem;
  letter-spacing: -0.025em;
  text-align: center;
}

.hpc-skill-card p {
  margin: 0;
  color: var(--muted);
  line-height: 1.55;
  font-weight: 200;
  font-size: 1.2rem;
  text-align: center;
}


@media (max-width: 980px) {
  .hpc-capability-map,
  .hpc-proof-row {
    grid-template-columns: 1fr;
  }
}

.contact-card { text-align: center; border: 1px solid var(--line); border-radius: 34px; background: var(--paper); box-shadow: var(--shadow); padding: clamp(1.5rem, 3vw, 2.6rem); }
.contact-card h3 { color: var(--navy); font-size: clamp(2.2rem, 4vw, 4.4rem); line-height: .9; letter-spacing: -.03em; margin: 0 0 .7rem; }
.contact-card p { color: var(--muted); max-width: 1500px; margin: 0 auto 1.15rem; font-size: 1.12rem; line-height: 1.6; }
.contact-links { display: flex; justify-content: center; gap: .8rem; flex-wrap: wrap; }

.download-inline { display:inline-flex; justify-content:center; align-items:center; }
.download-inline.missing { color: var(--muted); border: 1px solid var(--line); border-radius: 999px; padding: .8rem 1rem; }

div[data-testid="stDownloadButton"] button, div[data-testid="stLinkButton"] a { min-height: 4.2rem; border-radius: 18px !important; border: 1px solid var(--line) !important; background: var(--paper) !important; color: var(--navy) !important; font-weight: 850 !important; box-shadow: 0 10px 28px rgba(15,23,42,.05); white-space: normal; }
div[data-testid="stDownloadButton"] button:hover, div[data-testid="stLinkButton"] a:hover { border-color: #93C5FD !important; background: #F8FAFC !important; color: var(--blue-dark) !important; }

.choice, .metric, .card, .project-case, .hpc-map-panel, .hpc-proof, .hpc-skill-card, .screenshot-card, .step, .achievement-card { animation: reveal-card both; animation-timeline: view(); animation-range: entry 4% cover 24%; }
@keyframes reveal-card { from { opacity: .25; transform: translateY(28px) scale(.985); } to { opacity: 1; transform: translateY(0) scale(1); } }

.footer { border-top: 1px solid var(--line); color: var(--muted); text-align: center; padding: 3rem 0 4rem; }

@media (max-width: 1180px) {
  .hero { grid-template-columns: 1fr; text-align: center; }
  .hero-copy { text-align: center; }
  .hero-photo { margin: 0 auto; max-width: 330px; }
  .degree-strip { grid-template-columns: 1fr; }
  .choice-grid { grid-template-columns: repeat(2, 1fr); }
  .role-kpi-grid { grid-template-columns: repeat(2, 1fr); }
  .flow, .flow.five, .flow.four { grid-template-columns: repeat(3, 1fr); }
  .gallery, .card-grid.three, .achievement-grid { grid-template-columns: repeat(2, 1fr); }
  .proof-strip { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 760px) {
  .nav-inner { justify-content: flex-start; }
  .choice-grid, .card-grid, .card-grid.three, .gallery, .flow, .flow.five, .flow.four, .proof-strip, .achievement-grid { grid-template-columns: 1fr; }
  .hero-title { white-space: normal; }
  .role { width: 100%; }
}

/* PROJECT_SHOWCASE_UPDATE_CSS_START */
.project-summary-grid {
    width: min(100%, 1500px);
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem;
}
.project-summary-card {
    background: var(--paper);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: clamp(1.25rem, 2vw, 1.8rem);
    box-shadow: 0 18px 48px rgba(15, 23, 42, 0.06);
    text-align: left;
}
.project-summary-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    padding-bottom: 1rem;
    margin-bottom: 1.1rem;
    border-bottom: 1px solid var(--line);
}
.project-summary-title { display: flex; align-items: flex-start; gap: 0.7rem; }
.project-summary-title > span {
    color: #94a3b8;
    font-size: 0.9rem;
    font-weight: 900;
    padding-top: 0.2rem;
}
.project-summary-head h3 {
    margin: 0;
    color: var(--blue-dark);
    font-size: clamp(1.35rem, 2vw, 2rem);
    line-height: 1.15;
    letter-spacing: -0.025em;
}
.project-github-link {
    flex: 0 0 auto;
    text-decoration: none !important;
    color: white !important;
    background: linear-gradient(135deg, var(--navy), var(--blue-dark));
    border-radius: 999px;
    padding: 0.7rem 1rem;
    font-size: 0.9rem;
    font-weight: 800;
}
.project-detail + .project-detail { margin-top: 1rem; }
.project-detail-label {
    margin-bottom: 0.35rem;
    color: #64748b;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.project-business-question {
    margin: 0 !important;
    color: var(--navy) !important;
    font-size: 1.08rem !important;
    font-weight: 800;
    line-height: 1.5 !important;
}
.project-solution {
    margin: 0 !important;
    color: var(--muted) !important;
    font-size: 1rem !important;
    line-height: 1.65 !important;
}
.project-showcase-heading {  grid-column: 1 / -1; width: 100%; margin: 4.5rem 0 1.4rem; text-align: center; }
.project-showcase-heading h3 {
    margin: 0 0 0.45rem;
    color: var(--navy);
    font-size: clamp(1.8rem, 3vw, 3rem);
}
.project-showcase-heading p { margin: 0; color: var(--muted); }
.project-reel-shell {
    grid-column: 1 / -1;
    justify-self: stretch;
    

    width: 100vw;
    max-width: 100%;
    margin: 0 auto;
    overflow: hidden;
    padding: 1rem 0 1.8rem;
}
.project-reel-track {
    display: flex;
    width: max-content;
    animation: project-reel-scroll 68s linear infinite;
    will-change: transform;
}
.project-reel-group { display: flex; gap: 1.15rem; padding-right: 1.15rem; }
.project-reel-card {
    position: relative;
    flex: 0 0 clamp(320px, 40vw, 680px);
    aspect-ratio: 16 / 9;
    margin: 0;
    overflow: hidden;
    background: white;
    border: 1px solid var(--line);
    border-radius: 22px;
    box-shadow: 0 18px 48px rgba(15, 23, 42, 0.1);
}
.project-reel-card .screenshot-img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: contain;
    background: #f8fafc;
}
.project-reel-label {
    position: absolute;
    left: 0.85rem;
    bottom: 0.85rem;
    max-width: calc(100% - 1.7rem);
    padding: 0.55rem 0.8rem;
    color: white;
    background: rgba(11, 18, 32, 0.86);
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 800;
    backdrop-filter: blur(8px);
}

@keyframes project-reel-scroll {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}
@media (max-width: 850px) {
    .project-summary-grid { grid-template-columns: 1fr; }
    .project-summary-head { flex-direction: column; }
    .project-reel-card { flex-basis: 82vw; }
}
@media (prefers-reduced-motion: reduce) {
    .project-reel-track { animation: none; }
    .project-reel-shell { overflow-x: auto; }
}
/* PROJECT_SHOWCASE_UPDATE_CSS_END */

</style>
""")

html(f"""
<nav class="site-nav">
  <div class="nav-inner">
    <a href="#top">Home</a>
    <a href="#projects">Projects</a>
    <a href="#hpc">HPC</a>
    <a href="#materials">Materials</a>
    <a href="#leadership">Leadership</a>
    <a href="#achievements">Achievements</a>
    <a href="#contact">Contact</a>
    <a class="external" href="{GITHUB_URL}" target="_blank">GitHub</a>
    <a class="external" href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
    <a class="external" href="{EMAIL_URL}">Email</a>
  </div>
</nav>

<div class="page-shell">
  <section class="hero" id="top">
    <div class="hero-image">
      {profile_image()}
    </div>
    <div class="hero-copy">
      
      <h1 class="hero-title">Dr. Pranjal Nandi</h1>
      <div class="role-kpi-grid">
        <div class="role-kpi">
          <b>Data Analyst</b>
        </div>

        <div class="role-kpi">
          <b>Machine Learning / AI Engineer</b>
        </div>

        <div class="role-kpi">
          <b>High Performance Computing</b>
        </div>

        <div class="role-kpi">
          <b>Materials Science Data Simulation</b>
        </div>
      </div>
      <p class="intro-text">
        A multidisciplinary profile with 4+ years of data analysis at the intersection of artificial intelligence, machine learning, high-performance computing and materials research. 
      </p>
    </div>
    <div class="project-showcase-heading">
          
        </div>
        {project_screenshot_reel(PROJECT_REEL_IMAGES)}
  </section>

  

  
  <section class="expertise-panel">
    <div class="expertise-title">
      <h2>I specialise in the following areas</h2>
    </div>

    <div class="choice-grid">
      <a class="choice" href="#projects"><div><h3>Data, ML & AI Projects</h3><p>Business questions, concise analytical solutions and selected project previews.</p></div><div class="open-link">Explore →</div></a>
      <a class="choice" href="#hpc"><div><h3>High Performance Computing</h3><p>Batch jobs, Linux/SLURM, simulation workflows and reproducibility.</p></div><div class="open-link">Explore →</div></a>
      <a class="choice" href="#materials"><div><h3>Materials Science Data Simulation</h3><p>Research projects, chapter downloads and scientific methods.</p></div><div class="open-link">Explore →</div></a>
      
    </div>
  </section>
  
  
    <div class="expertise-title">
      <h2>And have a little bit of</h2>
    </div>

    <div class="choice-grid">
      <a class="choice" href="#publications"><div><h3>Publications</h3><p>Peer-reviewed research papers, DOI links and selected scientific outputs.</p></div><div class="open-link">Explore →</div></a>
      <a class="choice" href="#achievements"><div><h3>Achievements</h3><p>Awards, fellowships, scholarships, conferences and selected research recognition.</p></div><div class="open-link">Explore →</div></a>
      <a class="choice" href="#leadership"><div><h3>Entrepreneurship</h3><p>Sales, logistics, crisis management and real-world execution.</p></div><div class="open-link">Explore →</div></a>
    </div>
  </section>

""")

# Projects
html(f"""
<section class="branch" id="projects">
    <div class="branch-head">
        <h2>Data, ML & Quantitative Projects</h2>
        <p>
            Selected projects framed around the question they address and the
            analytical approach used to solve it.
        </p>
    </div>
    <div class="branch-content">
        <div class="project-summary-grid">
            {project_summary_cards(DATA_PROJECTS)}
        </div>
        
    </div>
</section>
""")

# HPC
html("""
<section class="branch" id="hpc">
  <div class="branch-head">
    <h2>High Performance Computing</h2>
  </div>

  <div class="branch-content">
    <article class="hpc-map-panel">

      

      <div class="hpc-proof-row">
        <div class="hpc-proof">
          <b>1,000+</b>
          <span>simulation variants tested</span>
        </div>
        <div class="hpc-proof">
          <b>2</b>
          <span>European supercomputing centres</span>
        </div>
        <div class="hpc-proof">
          <b>5</b>
          <span>major PhD case studies</span>
        </div>
        <div class="hpc-proof">
          <b>3+</b>
          <span>years scientific computing workflows</span>
        </div>
      </div>

      <div class="hpc-capability-map">

        <div class="hpc-capability-column">
          <div class="hpc-skill-card">
            
            <h4>Linux & Remote HPC Usage</h4>
            <p>Linux command line, Bash, SSH</p>
          </div>

          <div class="hpc-skill-card">
            
            <h4>SLURM Workload Management</h4>
            <p>Batch scripts, sbatch, srun, squeue, partitions, wall-time and memory requests.</p>
          </div>

          <div class="hpc-skill-card">
            
            <h4>Parallel Computing Configuration</h4>
            <p>MPI, Open MP</p>
          </div>
        </div>

        <div class="hpc-capability-column">
          <div class="hpc-skill-card">
            
            <h4>Software Environments</h4>
            <p>Environment modules, compilers, MPI libraries, Software compilations</p>
          </div>

          <div class="hpc-skill-card">
            
            <h4>Large-Scale Simulation Campaigns</h4>
            <p>Parameter sweeps, convergence studies, charge states, pressures, structures, compositions and DFT/EELS workflows.</p>
          </div>

          <div class="hpc-skill-card">
            
            <h4>Performance & Reliability</h4>
            <p>Runtime analysis, resource allocation, scaling awareness, memory optimisation, log analysis and failed-job recovery.</p>
          </div>
        </div>

      </div>

    </article>
  </div>
</section>
""")
# Materials


html(f"""
<section class="branch" id="materials">
  <div class="branch-head"><h2>Materials Science Research</h2></div>
  <div class="branch-content">
    <article class="project-case">
      <div class="project-topline"><h3>1. Hafnia RRAM</h3></div>
      <p>Research on how oxygen exposure and structure affect dielectric behaviour in hafnia-based resistive memory materials.</p>
      <div class="tag-row"><span class="tag">RRAM</span><span class="tag">HfO₂</span><span class="tag">Oxygen vacancies</span><span class="tag">Dielectric function</span><span class="tag">DFT-EELS</span></div>
      <div class="flow five"><div class="step"><b>01 System</b><span>Hafnia-based RRAM oxide layers.</span></div><div class="step"><b>2. Imaging</b><span>STEM/EELS structural and chemical evidence.</span></div><div class="step"><b>3. Simulation</b><span>DFT-based electronic and dielectric response.</span></div><div class="step"><b>4. Compare</b><span>Relate structure, oxygen content and spectra.</span></div><div class="step"><b>5. Interpret</b><span>Explain structure-property links in memory oxides.</span></div></div>
<div class="center-button"><div class="project-links"><a class="primary download-inline" href="https://drive.google.com/uc?export=download&id=1R0aOHeMFs1ztwxTHSXn9SlDK76tacX2-" target="_blank">Download Project</a></div></div>    </article>

    <article class="project-case">
      <div class="project-topline"><h3>2. Xenon Clusters</h3></div>
      <p>Research on pressure- and charge-tunable simulated EELS signatures of graphene-confined xenon clusters.</p>
      <div class="tag-row"><span class="tag">Xe clusters</span><span class="tag">Graphene confinement</span><span class="tag">Pressure</span><span class="tag">Charge</span><span class="tag">EELS simulation</span></div>
      <div class="flow five"><div class="step"><b>01 Cluster</b><span>Model Xe clusters inside graphene confinement.</span></div><div class="step"><b>2. Parameters</b><span>Vary pressure and charge states.</span></div><div class="step"><b>3. Calculate</b><span>Generate simulated EELS spectra.</span></div><div class="step"><b>04 Validate</b><span>Compare with experimental reference spectra.</span></div><div class="step"><b>05 Identify</b><span>Find spectral signatures and discrepancies.</span></div></div>
      <div class="center-button"><div class="project-links"><a class="primary download-inline" href="https://drive.google.com/uc?export=download&id=1n-DUjQwLMBxMf4O5V6Zud-C7CYJdgAOT" target="_blank">Download Project</a></div></div>
    </article>

    <article class="project-case">
      <div class="project-topline"><h3>3. LSMO Defect Quantification</h3></div>
      <p>Research on converting qualitative HAADF-STEM microscopy contrast into quantitative antisite-defect metrics in LSMO thin films.</p>
      <div class="tag-row"><span class="tag">LSMO</span><span class="tag">HAADF-STEM</span><span class="tag">Antisite defects</span><span class="tag">ATOMAP</span><span class="tag">Image simulation</span></div>
      <div class="flow five"><div class="step"><b>01 Structure</b><span>LSMO thin-film reference models.</span></div><div class="step"><b>2. Simulate</b><span>Generate HAADF-STEM image references.</span></div><div class="step"><b>3. Detect</b><span>Extract atomic-column intensities.</span></div><div class="step"><b>04 Metric</b><span>Use relative intensity ratios.</span></div><div class="step"><b>05 Quantify</b><span>Estimate defect signatures and concentration trends.</span></div></div>
      <div class="center-button"><div class="project-links"><a class="primary download-inline" href="https://drive.google.com/uc?export=download&id=1G3NgQGACNMJvwRN5KrlKDMVKPoxeFeJo" target="_blank">Download Project</a></div></div>
    </article>
  </div>
</section>

<section class="branch" id="publications">
  <div class="branch-head"><h2>Publications</h2></div>
  <div class="branch-content">
    <div class="card-grid three">
      <div class="card"><h4>Superorders and terahertz acoustic modes in multiferroic BiFeO₃/LaFeO₃ superlattices</h4><p>Applied Physics Reviews, 2024.</p><div class="project-links"><a class="primary" href="https://doi.org/10.1063/5.0203076" target="_blank">Link</a></div></div>
      <div class="card"><h4>Understanding coating thickness and uniformity of blade-coated SnO₂ ETL for scalable perovskite solar cells</h4><p>Solar RRL, 2023.</p><div class="project-links"><a class="primary" href="https://doi.org/10.1002/solr.202300273" target="_blank">Link</a></div></div>
      <div class="card"><h4>The impact of Mn nonstoichiometry on oxygen mass transport in La₀.₈Sr₀.₂MnO₃±δ thin films</h4><p>Journal of Physics: Energy, 2022.</p><div class="project-links"><a class="primary" href="https://doi.org/10.1088/2515-7655/ac98df" target="_blank">Link</a></div></div>
    </div>
  </div>
</section>
""")




# Research download buttons removed per change request.

# Leadership, Achievements, Contact
html(f"""
<div class="page-shell">

<section class="branch" id="achievements">
  <div class="branch-head">
    <h2>Achievements</h2>
    <p>Awards, fellowships and scholarships were the official story. This is the honest visual audit: where the money went, mostly to the conferences, travel, coffee, poster tubes, airport snacks and occasionally looking confident while being lost on campus.</p>
  </div>

  <div class="achievement-grid">
    <div class="achievement-card">
      {achievement_carousel('lindau', 'Lindau Nobel Laureate Meeting')}
      <div class="achievement-caption">
        <b>Young Scientist 2024</b>
        <span>73rd Lindau Nobel Laureate Meetings</span>
      </div>
    </div>

    <div class="achievement-card">
      {achievement_carousel('agaur_fi', 'AGAUR-FI Fellowship')}
      <div class="achievement-caption">
        <b>AGAUR-FI PhD Fellowship 2021-2024</b>
        <span>Catalan Government doctoral fellowship.</span>
      </div>
    </div>

    <div class="achievement-card">
      {achievement_carousel('paris_tech_totalenergies', 'TotalEnergies ParisTech Scholarship')}
      <div class="achievement-caption">
        <b>Master's Scholarship 2019-2020</b>
        <span>TotalEnergies and Fondation ParisTech scholarship.</span>
      </div>
    </div>

    <div class="achievement-card">
      {achievement_carousel('conferences', 'Research Conferences')}
      <div class="achievement-caption">
        <b>Sponsored Conferences 2021-2025</b>
        <span>Conference presentations and scientific outreach.</span>
      </div>
    </div>
  </div>
</section>

<section class="branch" id="leadership">
  <div class="branch-head">
    <h2>Entrepreneurship</h2>
  </div>

  <div class="branch-content">
    <div class="card-grid">
      <div class="card">
        <h4>Wedding event management</h4>
        <p>Managed 5+ weddings with more than 1000 total guests.</p>
        <div class="tag-row">
          <span class="tag">Clients</span>
          <span class="tag">Vendors</span>
          <span class="tag">Logistics</span>
        </div>
      </div>

      <div class="card">
        <h4>COVID grocery supply chain</h4>
        <p>Coordinated Indian grocery supply for around 200 hostel residents using forms, vendor negotiation and volunteers.</p>
        <div class="tag-row">
          <span class="tag">Crisis ops</span>
          <span class="tag">Trust</span>
          <span class="tag">Community</span>
        </div>
      </div>

      <div class="card">
        <h4>Hostel quick commerce</h4>
        <p>Sourced essentials, understood demand timing and generated monthly revenue.</p>
        <div class="tag-row">
          <span class="tag">Sales</span>
          <span class="tag">Pricing</span>
          <span class="tag">Customer behavior</span>
        </div>
      </div>

      <div class="card">
        <h4>Rental / hospitality management</h4>
        <p>Managed listings, Google Ads, reviews, guest expectations and seasonal pricing.</p>
        <div class="tag-row">
          <span class="tag">Marketing</span>
          <span class="tag">Reviews</span>
          <span class="tag">Service</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="branch" id="contact">
  <div class="contact-card">
    <h3>Let’s connect</h3>
    <p>Questions, ideas, or opportunities? Reach out on LinkedIn or email. Mind reading is not yet supported.</p>
    <div class="contact-links">
      <a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>
      <a href="{EMAIL_URL}">Email</a>
    </div>
  </div>
</section>

<footer class="footer">Dr. Pranjal Nandi — Data, AI/ML, HPC scientific computing and materials science.</footer>

</div>
""")
