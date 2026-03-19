# R_ID Reproducibility Pipeline

One-click reproduction of Integration-Dissipation Ratio (R_ID) results for OpenNeuro dataset ds005620.

## Quick Start

```bash
git clone https://github.com/danokeeffe1/rid-reproducibility.git
cd rid-reproducibility
docker compose up --build
```

First run takes ~3–5 hours (includes dataset download). Outputs appear in `outputs/`.

## Expected Outputs

| File | Rows | Description |
|------|------|-------------|
| full_window_results.csv | 25,350 | Per-window S_prod and C_L |
| rid_state_means.csv | 3 | State-level R_ID aggregates |
| inclusion_manifest.csv | 147 | Included recordings |
| validation_report.json | — | Pass/fail verification |

## Expected Results

| State | R_ID |
|-------|------|
| Wake | 0.000090 |
| Light | 0.000118 |
| Deep | 0.000050 |

## Companion Site

Interactive audit page: [state-echo.lovable.app](https://state-echo.lovable.app)

## License

MIT
