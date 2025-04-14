import subprocess
from pathlib import Path

# Define the path to the yt-dlp repo (user must download it manually)
yt_dlp_path = Path.home() / "Downloads" / "yt-dlp"
metrics_path = Path("metrics")
metrics_path.mkdir(exist_ok=True)

def run_radon(metric: str, args: list, output_file: str):
    command = ["radon", metric] + args + [str(yt_dlp_path)]
    with open(metrics_path / output_file, "w") as f:
        subprocess.run(command, stdout=f)

# Run different analyses
run_radon("cc", ["-s", "-a"], "complexity.txt")
run_radon("mi", [], "maintainability.txt")
run_radon("raw", [], "raw_metrics.txt")