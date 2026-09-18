# Using Generative AI Tools — Boon or Bane

Course repository for **REIT6811 Applied Class 6 (Activity 2)**.  
GitHub: [jt-09](https://github.com/jt-09) · repo: [`Generative_AI_Research_47861774`](https://github.com/jt-09/Generative_AI_Research_47861774)

Dummy project files for a class exercise on organising research data and using GitHub. Identifiable participant files (signed consent, raw transcripts, photos) would go in **UQ RDM**, not in this repo.

---

## Project structure

```text
Generative_AI_Research_47861774/
│
├── README.md                          ← you are here
├── Project_logbook.txt                ← collaboration log (Activity 2, step 6)
├── .gitignore
│
├── 01_literature/
│   ├── gai_literature_notes_20260918_v1.md
│   └── gai_literature_source-list_20260918_v1.md
│
├── 02_quantitative/
│   ├── raw/
│   │   ├── gai_survey_questions_20260918_v1.md
│   │   └── gai_survey_raw-responses_20260918_v1.csv
│   ├── processed/
│   │   └── gai_survey_cleaned-responses_20260918_v1.csv
│   ├── analysis/
│   │   └── gai_survey_analysis_20260918_v1.py
│   └── reports/
│       └── gai_survey_analysis-report_20260918_v1.md
│
├── 03_qualitative/
│   ├── protocols/
│   │   └── gai_interview_protocol_20260918_v1.md
│   ├── consent/
│   │   └── gai_consent_form-template_20260918_v1.md
│   ├── transcripts/
│   │   ├── README.md
│   │   └── gai_interview_transcript_P01-anonymised_20260918_v1.md
│   ├── analysis/
│   │   └── gai_interview_insights_20260918_v1.md
│   └── visualisations/
│       └── gai_interview_theme-counts_20260918_v1.md
│
├── 04_drafts_and_reports/
│   ├── gai_proposal_draft_20260918_v1.md
│   └── gai_conference-paper_draft_20260918_v1.md
│
└── 05_additional_materials/
    ├── gai_information-sheet_20260918_v1.md
    └── media/
        └── README.md
```

---

## How to navigate the files

Start at the numbered folders. They follow the research workflow: reading → survey work → interviews → writing up → extra materials.

| If you need… | Go to… | Notes |
|---|---|---|
| Papers / reading notes | `01_literature/` | PDFs can stay in Zotero; this folder holds notes and the source list |
| Survey questions or the original CSV | `02_quantitative/raw/` | Do not edit raw files. Copy into `processed/` if you need to clean them |
| Cleaned survey table | `02_quantitative/processed/` | Named `…cleaned-responses…` so it is obvious it is not the original |
| Python / analysis scripts | `02_quantitative/analysis/` | Run against the **processed** CSV, not the raw one |
| Survey write-up | `02_quantitative/reports/` | Summary of the numbers, not a second copy of the data |
| Interview script | `03_qualitative/protocols/` | How the interview is run |
| Consent template | `03_qualitative/consent/` | Blank template only. Signed forms would be in UQ RDM |
| Dummy transcript | `03_qualitative/transcripts/` | Fake / anonymised. Real identifiable transcripts would not be committed here |
| Interview themes | `03_qualitative/analysis/` and `visualisations/` | Insights text and placeholder chart notes |
| Proposal or paper drafts | `04_drafts_and_reports/` | Bump the date or `_v2` instead of saving `final.docx` |
| Info sheet / media placeholder | `05_additional_materials/` | Photos that could identify someone do not belong in `media/` |
| Group collaboration notes | `Project_logbook.txt` | Used for the fork / branch / pull-request exercise |

**Rule of thumb:** `raw/` is the original. `processed/` is cleaned. `analysis/` is code. `reports/` is what you would show a supervisor.

---

## File naming

Use:

```text
project_datatype_description_YYYYMMDD_version
```

Example: `gai_survey_cleaned-responses_20260918_v1.csv`

- `gai` = this project  
- `survey` / `interview` / `literature` = data type  
- a short description of the file  
- date the version was made  
- `v1`, `v2`, … if you replace it the same day  

Do not use names like `final2.docx` or `analysis_NEW_reallyfinal.py`.

---

## How to contribute

This repo uses branches and pull requests so two people do not silently overwrite each other on `main`.

1. Fork the repo, or ask to be added as a collaborator.
2. Clone your fork (or the repo) and create a branch with a useful name, for example `add-cleaned-survey` or `update-logbook-round1`.
3. Put new files in the matching folder and follow the naming convention above.
4. Commit with a message that says what changed, for example: `Added cleaned survey data and initial analysis scripts`.
5. Push the branch and open a **pull request into `main`**.
6. Wait for the reviewer to check it and merge. Do not push straight onto `main` if we are using PRs.

If two people edit the **same line** of a file (this will happen on purpose in `Project_logbook.txt`), GitHub will show a merge conflict. The reviewer keeps one version, or writes a combined line, then commits the fix and merges.

### Round 1 vs round 2 (class collaboration)

- **Round 1:** each developer edits **different lines** of `Project_logbook.txt` → should merge cleanly.  
- **Round 2:** both developers edit the **same line** → reviewer resolves the conflict, then merges.

---

## Sensitive data

Do not commit signed consent forms, identifiable transcripts, or photos of people. Those would be stored in UQ RDM with access limited to named investigators. What is in this repo is dummy text so the folder layout is visible for the class.

---

## AI use

Some of the file headings, comments, and commit messages in this repository were generated with AI. The folder structure, GitHub setup, and how the project is organised were done by me.
