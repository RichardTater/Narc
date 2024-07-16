CREATE TABLE IF NOT EXISTS `offender` (
	`id` integer primary key NOT NULL UNIQUE,
	`plate_number` TEXT NOT NULL,
	`plate_state` TEXT NOT NULL,
	`make` TEXT NOT NULL,
	`model` TEXT NOT NULL,
	`color` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `narc` (
	`id` integer primary key NOT NULL UNIQUE,
	`email` TEXT NOT NULL,
	`first_name` TEXT NOT NULL,
	`last_name` TEXT NOT NULL,
	`password` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `offence` (
	`id` integer primary key NOT NULL UNIQUE,
	`narc_id` INTEGER NOT NULL,
	`offender_id` INTEGER NOT NULL,
	`date` TEXT NOT NULL,
	`time` TEXT NOT NULL,
	`state` TEXT NOT NULL,
	`city` TEXT NOT NULL,
	`note` TEXT NOT NULL,
FOREIGN KEY(`narc_id`) REFERENCES `narc`(`id`),
FOREIGN KEY(`offender_id`) REFERENCES `offender`(`id`)
);
