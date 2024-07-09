import pandas as pd

# Data extracted from Table 2, handling multi-line rows in 'Model'
data = {
    'Model': ['ByteNet [18]', 'Deep-Att + PosUnk [39]', 'GNMT + RL [38]', 'ConvS2S [9]', 'MoE [32]',
              'Deep-Att + PosUnk Ensemble [39]\n', 'GNMT + RL Ensemble [38]', 'ConvS2S Ensemble [9]',
              'Transformer (base model)', 'Transformer (big)'],
    'EN-DE': ['23.75', '39.2', '24.6', '25.16', '26.03', '40.4', '26.30', '26.36', '27.3', '28.4'],
    'EN-FR': ['', '', '39.92', '40.46', '40.56', '', '41.16', '41.29', '38.1', '41.8'],
    'EN-DE Training Cost (FLOPs)': ['', '1.0 · 1020', '2.3 · 1019', '9.6 · 1018', '2.0 · 1019', '8.0 · 1020',
                                    '1.8 · 1020', '7.7 · 1019', '3.3 · 1018', '2.3 · 1019'],
    'EN-FR Training Cost (FLOPs)': ['', '', '1.4 · 1020', '1.5 · 1020', '1.2 · 1020', '', '1.1 · 1021', '1.2 · 1021',
                                    '', '']
}

# Combine 'EN-DE' and 'EN-FR' columns element-wise
data['BLEU Score'] = [f"{en_de} ; {en_fr}" for en_de, en_fr in zip(data['EN-DE'], data['EN-FR'])]

# Drop the original 'EN-DE' and 'EN-FR' columns
data.pop('EN-DE')
data.pop('EN-FR')

# Create the dataframe
df = pd.DataFrame(data)

# Write to CSV
df.to_csv('bleu_scores.csv', index=False)