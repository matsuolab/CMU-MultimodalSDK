CMU-Multimodal Opinion Sentiment Intensity (MOSI) dataset. 

1. The dataset contains 93 videos across 89 distinct spearkers. 
2. There is only one person speaking within each video. 
3. The topic of all videos is movie reviews. 
4. The dataset is approximately gender balanced.
5. The sentiment score is between -3,3 (extremely neg, extremely pos)
6. The sentiment binarization in all of the previous papers follows negative/non-negative binary classification with criteria of sentiment score <0 being negative and otherwise being non-negative. Newer approaches (after 2019) leave values equal to zero outside (therefore <0 being negative and >0 being strictly positive). There is around 2-3% difference between these two measures, latter being higher in accuracy.
7. For further details of the dataset, please refer to: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7742221
8. For 7-class sentiment, we use the round function to map to discretized range [-3,3]
