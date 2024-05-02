1. Extract Brain ROIs:
    1.1. Load brain images for all subjects.
    1.2. Segment the whole brain hemisphere into left and right ROIs.
    1.3. Extract 100 Grey matter ROIs from each hemisphere.
    1.4. Extract 100 Adjacent white matter ROIs (2mm from grey matter) for each hemisphere.

2. Extract Radiomics Features:
    2.1. For each subject:
        2.1.1. For each Grey matter ROI:
            2.1.1.1. Extract radiomics features (Total energy and IDM).
            2.1.1.2. Store the extracted features.
        2.1.2. For each White matter ROI:
            2.1.2.1. Extract radiomics features (Total energy and IDM).
            2.1.2.2. Store the extracted features.

3. Sort Subjects:
    3.1. Sort subjects based on cognitive normal status (amyloid negative, amyloid positive).

4. Statistical Analysis:
    4.1. For each radiomics feature:
        4.1.1. Perform linear model analysis to measure:
            4.1.1.1. SD
            4.1.1.2. Mean
            4.1.1.3. P-values
            4.1.1.4. T-value
        4.1.2. Store the statistical results.

5. Reporting:
    5.1. Tabulate the statistical results for all radiomics features.
    5.2. Report the results.
