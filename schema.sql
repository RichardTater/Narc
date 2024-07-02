CREATE TABLE IF NOT EXISTS `Offender` (
	`Offender_ID` integer primary key NOT NULL UNIQUE,
	`Plate_Number` TEXT NOT NULL,
	`Plate_State` TEXT NOT NULL,
	`Make` TEXT NOT NULL,
	`Model` TEXT NOT NULL,
	`Color` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Narc` (
	`Narc_ID` integer primary key NOT NULL UNIQUE,
	`Narc_Email` TEXT NOT NULL,
	`Narc_First_Name` TEXT NOT NULL,
	`Narc_Last_Name` TEXT NOT NULL,
	`MVP_Password` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Offences` (
	`Offence_ID` integer primary key NOT NULL UNIQUE,
	`Narc_ID` INTEGER NOT NULL,
	`Offender_ID` INTEGER NOT NULL,
	`Date_Of_Offense` TEXT NOT NULL,
	`Time_Of_Offence` TEXT NOT NULL,
	`State_Of_Offence` TEXT NOT NULL,
	`City_Of_Offence` TEXT NOT NULL,
	`Offence_Note` TEXT NOT NULL,
FOREIGN KEY(`Narc_ID`) REFERENCES `Narc`(`Narc_ID`),
FOREIGN KEY(`Offender_ID`) REFERENCES `Offender`(`Offender_ID`)
);
