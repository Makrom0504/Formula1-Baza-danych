WITH preselect AS (
    SELECT DISTINCT
        d.driverid,
        CONCAT(d.forename, ' ', d.surname) AS kierowca,
        d.surname,
        r.fastestLapTime AS Najszybsze_Okrążenie,
        r.race_id,
        ra.raceid,
        ra.circuitid,
        c.circuitid,
        c.circuitRef AS Nazwa_Toru,
        ra.year AS Rok
    FROM
        public.drivers AS d
        LEFT JOIN public.results AS r ON (d.driverid = r.driverid)
        LEFT JOIN public.races AS ra ON (r.race_id = ra.raceid)
        LEFT JOIN public.circuits AS c ON (ra.circuitid = c.circuitid)
      WHERE r.fastestLapTime IS NOT NULL AND ra.year= '<YEAR>'
)

SELECT
    kierowca,
    Najszybsze_Okrążenie,
    Nazwa_Toru,
    Rok
FROM
    preselect
ORDER BY
Nazwa_Toru, Rok;

