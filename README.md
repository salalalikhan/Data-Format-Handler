## Overview
This task delves into the performance analysis of parallel processing in handling large datasets with varying storage types: Fixed, Delimited, and Offset. It explores the impact of increasing processes varying from (1, 2, 4, and 8) on both small (1000 records) and large (100k records) datasets, highlighting key trends and findings.

## Objectives
1. Evaluate the performance of different storage types.
2. Investigate how process count affects computational efficiency.
3. Analyze the influence of dataset size on processing times.
4. Assess hardware performance in handling parallelized workflows.

## Highlights of My Work
1. **Data-Driven Observations**:
   - Identified performance degradation for smaller datasets during increase of process counts due to overhead.
   - Demonstrated significant improvements for larger datasets with parallel processing.

2. **Insightful Analysis**:
   - Fixed storage exhibited the highest processing time due to increased computational overhead.
   - Offset storage consistently outperformed other types particularly for larger datasets.

3. **Innovative Thought Process**:
   - Leveraged real-world hardware constraints like (MacBook Pro: 2.7 GHz dual-core processor, 8GB RAM) to uncover unexpected bottlenecks.
   - Emphasized the relationship between dataset size, storage type, and computational efficiency.

## Key Results
### **Impact of Process Count on Fixed Storage**:
| Processes | 1000 Records (s) | 100k Records (s) |
|-----------|------------------|------------------|
| 1         | 0.75             | 9.41             |
| 8         | 1.31             | 3.29             |

### **Impact of Process Count on Delimited Storage**:
| Processes | 1000 Records (s) | 100k Records (s) |
|-----------|------------------|------------------|
| 1         | 0.61             | 5.53             |
| 8         | 1.45             | 2.36             |

### **Impact of Process Count on Offset Storage**:
| Processes | 1000 Records (s) | 100k Records (s) |
|-----------|------------------|------------------|
| 1         | 0.87             | 10.43            |
| 8         | 1.49             | 5.02             |

## Key Insights
- **Smaller Datasets**:
  - Minimal performance gains with increased process count.
  - Fixed storage incurred higher processing times due to computational overhead.

- **Larger Datasets**:
  - Parallel processing significantly reduced processing times.
  - Offset storage emerged as the most efficient method for handling large-scale data.

## Challenges Tackled
1. **Unexpected Results**:
   - Smaller datasets (1000 records) showed negligible performance improvements and highlighting the limitations of parallelism for small scale data.
   - Fixed storage consistently underperformed across all scenarios.

2. **Hardware Limitations**:
   - Addressed the constraints of testing on a dual-core processor with 8GB RAM, ensuring results were both realistic and scalable.

## Files Included
- `Analysis_Salal.pdf`: Comprehensive report documenting observations and findings.
- `store_analyze.py`: Python script for processing and analyzing datasets, structured to optimize readability and efficiency.

## Conclusion
This task provided an in-depth understanding of how storage types, dataset sizes, and parallel processes interact. The results underscore the importance of choosing appropriate storage mechanisms and optimizing hardware utilization for big data processings.
