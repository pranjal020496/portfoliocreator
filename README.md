# Dr. Pranjal Nandi - Changes Applied Portfolio

This version implements the change list from `changes1.docx`.

## Main changes

- Removed the name/brand from the top-left navigation.
- Centered the navigation links.
- Added Achievements to the navigation.
- Added GitHub, LinkedIn and Email buttons to the top navigation.
- Removed the hero button group.
- Removed the interactive portfolio badge.
- Changed the hero layout to a larger photo on the left and description on the right.
- Added `Dr.` and kept `Dr. Pranjal Nandi` on one line.
- Reworded the intro to appeal to AI/ML, HPC and scientific audiences.
- Added degree KPI cards with logo-style university badges.
- Added a placeholder Achievements section for future photos.
- Removed the recruiter pack.
- Contact section now focuses only on GitHub, LinkedIn and Email.
- Project labels now appear directly in the project title, e.g. `Project 01 · Sugar Belly`.
- Research download buttons use `Download Project — ...` labels.

## Run locally

```bash
conda activate portfoliocreater
cd interactive_portfolio_v0_11_changes_applied
pip install -r requirements.txt
streamlit run app.py
```

## Replace achievement photos later

Add images to:

```text
assets/achievements/
```

Suggested names:

```text
lindau.jpg
agaur_fi.jpg
paris_tech_totalenergies.jpg
conferences.jpg
```


## v0.12 document changes

Applied the latest changes from `changes1.docx`:
- Materials Science is split into three individual research projects: Hafnia RRAM, Xenon Clusters and LSMO Defect Quantification.
- Project titles now use numbers only, for example `01 · Sugar Belly` instead of `Project 01`.
- HPC titles no longer say `HPC Project`.
- The separate research download list was removed; each research project now has its own `Download Project` button.
- Added Publications with DOI links under Materials Science.
- Removed the numbered `Contact Me` heading; kept only the `Let’s connect` contact card.
- Standardized blue accent colour across the app.
- Updated hero/expertise wording and removed the Contact card from the expertise area.
