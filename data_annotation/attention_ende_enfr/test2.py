import pandas as pd

# Data extracted from the PDF
data = {
    "Model": ["ByteNet [18]", "Deep-Att + PosUnk [39]", "GNMT + RL [38]", "ConvS2S [9]",
              "MoE [32]", "Deep-Att + PosUnk Ensemble [39]", "GNMT + RL Ensemble [38]",
              "ConvS2S Ensemble [9]", "Transformer (base model)", "Transformer (big)"],
    "EN-DE": [None, 23.75, 24.6, 25.16, 26.03, None, 26.30, 26.36, 27.3, 28.4],
    "EN-FR": [None, 39.2, 39.92, 40.46, 40.56, 40.4, 41.16, 41.29, 38.1, 41.8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Combine the BLEU scores into a single column
df["BLEU Scores"] = df["EN-DE"].astype(str) + " ; " + df["EN-FR"].astype(str)

# Drop the individual columns
df = df.drop(columns=["EN-DE", "EN-FR"])

# Save to a new CSV file
output_path = "combined_bleu_scores.csv"
df.to_csv(output_path, index=False)

print(output_path)