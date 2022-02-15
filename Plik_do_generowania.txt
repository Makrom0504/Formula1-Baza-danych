WITH preselect AS (
    SELECT DISTINCT
        d.driverid,
        CONCAT(d.forename, ' ', d.surname) AS kierowca,
        r.constructorid,
        c.constructor_ref,
        d.surname
    FROM
        public.drivers AS d
        LEFT JOIN public.results AS r ON (d.driverid = r.driverid)
        LEFT JOIN public.constructors AS c ON (c.constructor_id = r.constructorid)
    WHERE r.constructorid = <NUMBER>
)
SELECT
    kierowca,
    constructor_ref
FROM
    preselect
ORDER BY
    surname;

