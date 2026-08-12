import pandas as pd

scorecard = pd.read_csv("reports/fund_scorecard.csv")

scorecard["risk_grade"] = pd.cut(
    scorecard["max_drawdown_pct"].abs(),
    bins=[-float("inf"), 15, 20, float("inf")],
    labels=["Low", "Moderate", "High"]
)

def recommend_funds(risk_appetite, top_n=3):
    risk_appetite = risk_appetite.strip().title()

    if risk_appetite not in ["Low", "Moderate", "High"]:
        raise ValueError("Risk appetite must be Low, Moderate, or High.")

    recommendations = (
        scorecard[scorecard["risk_grade"] == risk_appetite]
        .sort_values("fund_score", ascending=False)
        .head(top_n)
    )

    return recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "cagr_3yr",
            "max_drawdown_pct",
            "fund_score"
        ]
    ]


if __name__ == "__main__":
    for risk in ["Low", "Moderate", "High"]:
        print(f"\nTop 3 Fund Recommendations for {risk} Risk Appetite:")
        print(recommend_funds(risk).to_string(index=False))