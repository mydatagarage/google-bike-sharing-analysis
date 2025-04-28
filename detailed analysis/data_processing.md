# Data Processing
This phase involves several key activities aimed at transforming raw data into valuable information. Firstly, we begin by organizing and cleaning the data to ensure its accuracy and consistency. This involves checking for missing values, removing duplicates, and addressing any data anomalies or inconsistencies that may impact the quality of our analysis. Next, we apply various data manipulation techniques such as filtering, sorting, and aggregating to extract relevant subsets of data that align with our research questions and objectives. By focusing on specific variables or time periods, we can uncover patterns and trends that are essential for our analysis.
Once the data is prepared, we proceed to conduct exploratory data analysis to gain a deeper understanding of the dataset. Through visualization techniques, statistical summaries, and data profiling, we explore the characteristics and relationships within the data, identifying potential insights and hypotheses to be further investigated. Throughout the process, we document our methodologies, decisions, and any assumptions made, ensuring transparency and reproducibility. Additionally, we continuously evaluate and refine our analysis techniques, adapting as necessary to address emerging insights and refine our research questions.

## Data type used for SQL table
• ride_id - character varying (string)
• bike_type - character varying (string)
• start_time - timestamp without time zone (datetime)
• end_time - timestamp without time zone (datetime)
• start_station_name - character varying (string)
• start_station_id - character varying (string)
• end_station_name - character varying (string)

## Pre-cleaning considerations
• Stations’ names does not provide crucial insights on different behavior of casual riders and annual
members. The analysis is not heavily dependent on geographic information –> drop the names’ and
coordinates’ features
• Coordinates are necessary to meet the analysis goal –> round all coordinates to 2 decimal precision
• We can do partial geographic analysis –> perform operations on coordinates only for classic bikes
• We can enrich our data –> try to obtain more accurate coordinates, altought from our hypothesis
coordinates collection is limited in precision for electric bike not docked
• Keep coordinates’ features reaching a common level of precision for every record –> round the 6 decimal
precision to the lower 2 decimal precision: most practical solution
• Keep as many data as possible, evaluating with more advance techniques the difference in precision –>
perform a sensitive analysis to understand how the uncertainty in the coordinates with only 2 decimal
places affects the overall results: most advanced solution
The geographic information provided by the coordinates can offer valuable insights into usage patterns,
popular routes, and areas with high demand. We decided to keep these stations’ names data and round
latitude and longitude from the six-decimal-place coordinates to two decimal places before performing any
calculation. This will ensure consistency in precision, although we will loose potential valuable data. We also
accept a maximum potential error for transformations and operations on latitude and longitude coordinates
of the dataset. When calculating useful features like distance between geographic coordinates, we will try to
minimize cumulative rounding errors performing calculation with higher precision before rounding the final
result to two decimal places. This caution should reduce the impact of rounding at each calculation step.
