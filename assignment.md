# Question one 
## How many taxi trips were there on January 15?

SELECT 
	CAST(tpep_pickup_datetime AS DATE) AS "days",
	COUNT(1)
FROM 
	yellow_taxi_data
GROUP BY 1
HAVING CAST(tpep_pickup_datetime AS DATE)= '2021-01-15';

## ANSWER: 53024




# Question two 
## Find the largest tip for each day. On which day it was the largest tip in January?
--Use the pick up time for your calculations.
--(note: it's not a typo, it's "tip", not "trip")

SELECT 
	CAST(tpep_pickup_datetime AS DATE) AS "days",
	--tip_amount,
	MAX(tip_amount) AS tip
FROM 
	yellow_taxi_data
GROUP BY 1,tip_amount
HAVING CAST(tpep_pickup_datetime AS DATE) BETWEEN '2021-01-01' AND '2021-01-31'
ORDER BY tip_amount DESC; 

# ANSWER: Highest tip= 1140.44 and Date: 2021-01-20

# Question three 
## What was the most popular destination for passengers picked up in central park on January 14?
--Use the pick up time for your calculations.
--Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown"


SELECT 
	CAST(tpep_pickup_datetime AS DATE) AS "days",
	zpickup."Zone" as pickup_zone,
	zdropoff."Zone" as dropoff_zone,
	count(zdropoff."Zone") as count_of_dropoff
FROM 
	yellow_taxi_data t  join taxi_zones zpickup
	on t."PULocationID" =zpickup."LocationID" 
	join taxi_zones zdropoff 
	on t."DOLocationID"  = zdropoff."LocationID" 
group by 1,2,3
having 
	zpickup."Zone" = 'Central Park' and CAST(tpep_pickup_datetime AS DATE) = '2021-01-14'
order by count(zdropoff."Zone") desc ;

# Answer: Highest Count is 97 and Dropoff_zone : Upper East Side South

# Question four
## What's the pickup-dropoff pair with the largest average price for a ride (calculated based on total_amount)?
--Enter two zone names separated by a slash
--For example:
--"Jamaica Bay / Clinton East"
--If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East"

SELECT 
	concat( zpickup."Zone",'/', zdropoff."Zone") as pickup_dropoff_pair,
	avg(t.total_amount) as average_amount
FROM 
	yellow_taxi_data t  join taxi_zones zpickup
	on t."PULocationID" =zpickup."LocationID" 
	join taxi_zones zdropoff 
	on t."DOLocationID"  = zdropoff."LocationID" 
group by 1
order by avg(t.total_amount) desc ;

# Answer: Largest average amount is 2292.4 and the pickup_dropoff pair is Alphabet City/Unknown