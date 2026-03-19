"""
Main entry point for the R_ID reproducibility pipeline.
Downloads ds005620 from OpenNeuro, preprocesses EEG, computes S_prod and C_L,
and outputs aggregate R_ID per state.

TODO: Replace stub logic with your actual analysis code.
"""
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

DATA_DIR = os.environ.get("DATA_DIR", "data")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "outputs")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log.info("Starting R_ID pipeline v1.0.0")
    log.info(f"Data dir: {DATA_DIR}, Output dir: {OUTPUT_DIR}")

    # Step 1: Download / cache dataset
    log.info("Step 1: Fetching ds005620 from OpenNeuro...")
    # TODO: openneuro.download(dataset="ds005620", target_dir=DATA_DIR)

    # Step 2: Build inclusion manifest
    log.info("Step 2: Building inclusion manifest...")
    # TODO: exclude acq-tms recordings

    # Step 3: Preprocess (bandpass 1-45 Hz, downsample to 256 Hz, z-score)
    log.info("Step 3: Preprocessing EEG...")

    # Step 4: Window and compute metrics
    log.info("Step 4: Computing S_prod and C_L per 4s window...")

    # Step 5: Aggregate R_ID per state
    log.info("Step 5: Aggregating R_ID = mean(S_prod) / mean(C_L) per state...")

    # Step 6: Write outputs
    log.info("Step 6: Writing outputs...")
    log.info("Pipeline complete.")

if __name__ == "__main__":
    main()
