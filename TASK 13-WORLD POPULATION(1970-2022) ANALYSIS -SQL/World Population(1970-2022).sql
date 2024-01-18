USE world_population;

SELECT * FROM world_population;

SELECT Continent, COUNT(Country) AS Number_Of_Countries
FROM world_population
GROUP BY Continent
ORDER BY Number_Of_Countries DESC;

SELECT * FROM world_population ORDER BY `2022 Population` DESC LIMIT 1;

SELECT * FROM world_population WHERE Continent = 'Asia'
ORDER BY `Rank` ASC;

SELECT Continent, AVG (`2022 Population`) as Avg_population
FROM world_population
GROUP BY Continent
ORDER BY Avg_population DESC LIMIT 5;

SELECT `Rank`,Continent,Country,`2022 Population`,`World Population Percentage`,`Density (per kmÂ²)` FROM world_population
ORDER BY `Density (per kmÂ²)` DESC LIMIT 5;

SELECT `Rank`,Continent,Country,`2022 Population`,`World Population Percentage`,`Growth Rate` FROM world_population
WHERE `Growth Rate` > 1
ORDER BY `Growth Rate` DESC;

SELECT Continent, Country, SUM(`2022 Population`) AS Total_population 
FROM world_population
GROUP BY Continent, Country
ORDER BY Total_population DESC;


SELECT Continent, Country, SUM(`2022 Population`) AS Total_population, `Area (kmÂ²)`
FROM world_population
GROUP BY Continent, Country, `Area (kmÂ²)`
ORDER BY Total_population ASC
LIMIT 10;

SELECT Continent, Country, SUM(`2022 Population`) AS Total_population, `Growth Rate`,`Area (kmÂ²)`
FROM world_population 
WHERE `2022 Population` > 50000000 AND `Growth Rate` < 1
GROUP BY Continent, Country, `Area (kmÂ²)`,`Growth Rate`;

SELECT Continent, Country, SUM(`2022 Population`) AS Total_population, `Growth Rate`,`Area (kmÂ²)`
FROM world_population 
GROUP BY Continent, Country, `Area (kmÂ²)`,`Growth Rate`
ORDER BY `Growth Rate` DESC LIMIT 3;

SELECT Continent, Country, SUM(`2022 Population`) AS 2022_population, SUM(`2020 Population`) AS 2020_population,`Growth Rate`
FROM world_population
WHERE `2022 Population` < `2000 Population`
GROUP BY Continent, Country, `Area (kmÂ²)`,`Growth Rate`
ORDER BY 2022_population DESC LIMIT 10;

SELECT Continent, Country, SUM(`1970 Population`) AS `1970_population`, SUM(`2022 Population`) AS `2022_population`, `Growth Rate`
FROM world_population 
GROUP BY Continent, Country, `Growth Rate`
ORDER BY (`2022_population` - `1970_population`) ASC
LIMIT 1;

SELECT Continent, Country, SUM(`2022 Population`) AS `2022_population`, MAX(`World Population Percentage`) AS `World Population Percentage`, `Growth Rate`
FROM world_population 
GROUP BY Continent, Country, `Growth Rate`
ORDER BY `World Population Percentage` DESC
LIMIT 1;










