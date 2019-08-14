CREATE TABLE [Game] (
	[id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, 
	[home_team] int NOT NULL, 
	[away_team] int NOT NULL, 
	[start_date] date NOT NULL, 
	[start_time] datetime2 NOT NULL
);