# yt‑dlp Case‑Study • Software‑Quality Report

## 1  Problem Statement  
`yt‑dlp` is an extremely active open‑source video/audio‑downloader.  
Because rapid feature growth can erode maintainability, this study set out to **quantify code quality and pinpoint improvement areas**.

## 2  Analysis Pipeline & Tools  

| Step | Purpose | Tool(s) |
|------|---------|---------|
| Static complexity scan | Cyclomatic Complexity (CC) & Logical Lines of Code (LLOC) | **Radon** |
| Test‑suite execution & coverage | Line + branch coverage | **coverage** |
| Defect‑density mining | Bugs / K‑LLOC from GitHub issues | GitHub issues list |


A single driver script `Analyze_YT‑DLP.py` orchestrates everything and writes plain‑text outputs to `metrics/`.

## 3  Collected Metrics  

| Metric | Result | Interpretation |
|--------|--------|----------------|
| **Cyclomatic Complexity** | *4.51 (A)* across 8 391 blocks; **1.33 %** ≥ grade D | Codebase is generally simple; a small set of risky hotspots deserve refactor  |
| **Logical LOC (LLOC)** | ~70.368 K LLOC ( Radon raw output ) | Size continues to climb with each release |
| **Defect Density** | Moderate overall; high closure rate | Active maintenance keeps bug backlog low  |
| **Test Coverage** | **36 %** lines, 28 % branches (current run) | Gaps exist—esp. edge‑case extractors |

## 4  Key Findings  

* **Healthy baseline quality:** Average CC of *A* indicates strong structure, but **~1 % outliers** need attention.  
* **Complexity ↔ bugs:** High‑CC modules correlate with more reported issues .  
* **Coverage is the weak link:** < 40 % coverage leaves many execution paths untested.  
* **Documentation debt:** Rapid contributor growth outpaces onboarding docs.

## 5  Recommendations  

1. **Refactor the dozen high‑risk functions** (grade D–F).  
2. **Raise unit coverage to ≥ 60 %**—prioritise extractor edge‑cases.  
3. **Automate Radon & coverage gates in CI**, blocking PRs that regress quality.  
4. **Expand contributor docs** (setup, test‑writing guide) to sustain velocity. 

## 6  Re‑running the Study  

```bash
# 1. clone this repo
https://github.com/Tvaughn22/yt-dlp-case-study.git
# 2. download yt-dlp zip
# 3. edit path in Analyze_YT-DLP.py to match yt-dlp zip location
# 4. Install dependencies
python -m venv .venv && source .venv/bin/activate
pip install radon and coverage

# 5.  Execute the pipeline
python Analyze_YT-DLP.py

# 6.  View outputs
cat metrics/complexity.txt       # CC grades per file/function
coverage html && open htmlcov/index.html
