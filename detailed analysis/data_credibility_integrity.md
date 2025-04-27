# Data Credibility
Collected data are credible and unbiased. As first-party data, collected directly from Cyclist database using own resources, the data are original and reflects the business through the observations. The chosen sample (last 12 month) is also current, large enough to show trends, and is representative of the entire population of rides. We won't perform in-depth statistical analysis since we should start from the beginning calculating the total amount of rides available setting a confidence level and a margin of error. The reliability of our conclusion will be based on the hypothesis that the sample is representative of the population. 
Original/internal data is owned directly by the company (own internal license), that can also provide any data processing activity previously used. The privacy of the dataset involves not using personal identifiable information so we won't be able to connect past purchase to credit card numbers to determine if casual riders lives in the Cyclist service area, or if they purchase multiple single pass. This information can be found in the fictional 'Data Life Cycle' documentation that the Data Science team should have been prepared before collecting observations.

Note: from prior inspection with Excel of random month data, we notice multiple errors and inconsistency in the dataset:

• start/end station name and id contains NULL values
• start/end station_id have inconsistent naming
• start/end latitude and longitude contain NULL values

# Data Integrity
Original (downloaded) data haven't been replicated into multiple location, transferred, or manipulated. Also, Cyclist data engineers (suppose they exist into the analytical team or they hire external third party engineers as needed) are confident about any human error, viruses or system failure that could have been compromised data integrity. In addition, I suppose the identifier 'ride_id' is unique for the single months dataset but not across all the collected datasets. Although I don't consider the identifier as necessary during the analysis steps, I will investigate and try to validate this hypothesis. Data are accurate, complete, consistent, and trustworthy through its life cycle. So we can be sure about data integrity.
