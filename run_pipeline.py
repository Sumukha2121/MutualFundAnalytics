"""
Master execution script for the Bluestock Mutual Fund Analytics project.

Runs the core data ingestion, cleaning, validation, database preparation,
and analytics-support scripts in the required project sequence.
"""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def run_script(script_path: Path) -> None:
    """Execute a Python script and stop the pipeline if it fails."""
    print(f"\nRunning: {script_path.name}")
    subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        check=True,
    )


def main() -> None:
    """Run the project pipeline in the required execution order."""

    pipeline = [
        PROJECT_ROOT / "data_ingestion.py",
        SCRIPTS_DIR / "clean_investor_transactions.py",
        SCRIPTS_DIR / "clean_nav_history.py",
        SCRIPTS_DIR / "clean_scheme_performance.py",
        SCRIPTS_DIR / "validate_amfi.py",
        SCRIPTS_DIR / "create_date_dimension.py",
        SCRIPTS_DIR / "create_database.py",
        SCRIPTS_DIR / "load_to_sqlite.py",
        SCRIPTS_DIR / "data_quality_report.py",
    ]

    for script in pipeline:
        if not script.exists():
            raise FileNotFoundError(f"Required script not found: {script}")

        run_script(script)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()