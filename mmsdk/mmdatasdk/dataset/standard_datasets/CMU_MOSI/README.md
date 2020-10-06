CMU-Multimodal Opinion Sentiment Intensity (MOSI) dataset. 

1. The dataset contains 93 videos across 89 distinct speakers. 
2. There is only one person speaking within each video. 
3. The topic of all videos is movie reviews. 
4. The dataset is approximately gender balanced.
5. The sentiment score is between -3,3 (extremely neg, extremely pos)
6. The sentiment binarization in all of the previous papers follows negative/non-negative binary classification with criteria of sentiment score <0 being negative and otherwise being non-negative. Newer approaches (after 2019) leave values equal to zero outside (therefore <0 being negative and >0 being strictly positive). There is around 2-3% difference between these two measures, latter being higher in accuracy.
7. For further details of the dataset, please refer to: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7742221
8. For 7-class sentiment, we use the round function to map to discretized range [-3,3]

# Scoreboard
Feel free to push your novel work!

| Models       | MAE   | Corr  | Acc-2 | Acc-2 | F-Score | F-Score | Acc-7 |
|--------------|-------|-------|-------|-------|---------|---------|-------|
| BC-LSTM      | 1.079 | 0.581 | 73.9  | -/    | 73.9    | -/      | 28.7  |
| MV-LSTM      | 1.019 | 0.601 | 73.9  | -/    | 74      | -/      | 33.2  |
| TFN          | 0.97  | 0.633 | 73.9  | -/    | 73.4    | -/      | 32.1  |
| MARN         | 0.968 | 0.625 | 77.1  | -/    | 77      | -/      | 34.7  |
| MFN          | 0.965 | 0.632 | 77.4  | -/    | 77.3    | -/      | 34.1  |
| LMF          | 0.912 | 0.668 | 76.4  | -/    | 75.7    | -/      | 32.8  |
| CH-Fusion    | -     | -     | 80    | -/    | -       | -/      | -     |
| MFM          | 0.951 | 0.662 | 78.1  | -/    | 78.1    | -/      | 36.2  |
| RAVEN        | 0.915 | 0.691 | 78    | -/    | 76.6    | -/      | 33.2  |
| RMFN         | 0.922 | 0.681 | 78.4  | -/    | 78      | -/      | 38.3  |
| MCTN         | 0.909 | 0.676 | 79.3  | -/    | 79.1    | -/      | 35.6  |
| CIA          | 0.914 | 0.689 | 79.8  | -/    | -/      | 79.5    | 38.9  |
| HFFN         | -     | -     | -/    | 80.2  | -/      | 80.3    | -     |
| LMFN         | -     | -     | -/    | 80.9  | -/      | 80.9    | -     |
| DFF-ATMF (B) | -     | -     | -/    | 80.9  | -/      | 81.2    | -     |
| ARGF         | -     | -     | -/    | 81.4  | -/      | 81.5    | -     |
| MulT         | 0.871 | 0.698 | -/    | 83    | -/      | 82.8    | 40    |
| TFN (B)      | 0.901 | 0.698 | -/    | 80.8  | -/      | 80.7    | 34.9  |
| LMF (B)      | 0.917 | 0.695 | -/    | 82.5  | -/      | 82.4    | 33.2  |
| MFM (B)      | 0.877 | 0.706 | -/    | 81.7  | -/      | 81.6    | 35.4  |
| ICCN (B)     | 0.86  | 0.71  | -/    | 83    | -/      | 83      | 39    |
| MISA (B)     | 0.783 | 0.761 | 81.8  | 83.4  | 81.7    | 83.6    | 42.3  |
| FMT          |       |       | 81.5  | 83.5  | 81.4    |         |       |
