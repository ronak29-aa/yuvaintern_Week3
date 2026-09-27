from pathlib import Path
import os, runpy
root=Path(__file__).resolve().parents[1]; os.chdir(root)
runpy.run_path("src/analysis.py")
runpy.run_path("src/visualize_results.py")
print("Week 3 statistical analysis pipeline completed.")
