# Initial Design
## Products
1. A table `car-results` in Redshift with Edmunds data on three cars: Honda Civic, Toyota Corolla, and Toyota 4Runner.
2. A periodic snapshot table `cars-weekly` that summarizes volumes by make and model 
3. An accumulating snapshot table called `cars-progress` that tracks how quickly a car enters and leaves the market.
4. A Tableau Public presentation of the findings
5. A website displaying the project
6. Unit testing across the entire pipeline.