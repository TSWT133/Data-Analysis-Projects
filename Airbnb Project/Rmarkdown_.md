---
title: "Step by step process"
author: "Thomas To"
date: "23/11/2023"
output:
  pdf_document: default
  html_document:
    df_print: paged
  word_document: default
---

## [ETL in SQL (Big Query)]{.underline}

[**Extraction and Importing:**]{.underline} Extracted data from [Airbnb](http://insideairbnb.com/get-the-data/), imported into BigQuery, and assessed data loading.

![*Data sourced from Airbnb*](Source%20data.PNG){width="569"}

![*Creating Data warehouse*](Created%20data%20set.PNG)

![*Importing multiple tables*](Import%20start.PNG)

![*Configuration for data import*](import%20table%20config.PNG)

![*Import of 2nd data table*](2nd%20table%20import.PNG)

**Handling Missing Values:** Identified missing values in "Last Review date," used JOIN functions to populate missing data.

**Column Transformation:** Split condensed information in the 'name' column into separate values.

**Combining Queries:** Condensed previous queries into a single, efficient query for data processing.

**Exporting Cleaned Data:** Exported the cleaned dataset into a new table within the database.

**Data Type Correction:** Identified issues with the data type in the Rating column and attempted to correct it, handling anomalies like mixing bedroom data into the ratings.

**Refinement of Rating Column:** Updated queries to refine the Rating column, handling 'New' values as null. Final Export: Exported the refined data into a new table.

## [Visualization with R]{.underline}

**Package Installation:** Installed necessary R packages for data manipulation and visualization.

**Data Manipulation:** Filtered outliers, summarized key insights about total reviews, average price, and availability based on room types and neighborhoods.

**Visual Exploration:** Created visualizations depicting relationships between variables such as room type and reviews, price vs. rating, geographical distribution of listings, etc.

**Geographical Mapping:** Utilized Google Maps API to plot the location of Airbnb listings on a map of London.