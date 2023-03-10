SELECT *
FROM pg_stat_activity
WHERE datname = 'Food_Restaurant';


SELECT
	pg_terminate_backend (pg_stat_activity.pid)
FROM
	pg_stat_activity
WHERE
	pg_stat_activity.datname = 'Food_Restaurant';
    

DROP DATABASE 'Food_Restaurant';

DROP DATABASE Food_Restaurant;