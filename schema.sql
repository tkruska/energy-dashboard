CREATE SCHEMA IF NOT EXISTS energy;

CREATE TABLE IF NOT EXISTS energy.metrics (
    ts timestamp,
    metric_type varchar(255),
    measurement real,
    country varchar(2) CHECK (
        country IN (
            'de',
            'ch',
            'eu',
            'all',
            'al',
            'am',
            'at',
            'az',
            'ba',
            'be',
            'bg',
            'by',
            'cy',
            'cz',
            'dk',
            'ee',
            'es',
            'fi',
            'fr',
            'ge',
            'gr',
            'hr',
            'hu',
            'ie',
            'it',
            'lt',
            'lu',
            'lv',
            'md',
            'me',
            'mk',
            'mt',
            'nie',
            'nl',
            'no',
            'pl',
            'pt',
            'ro',
            'rs',
            'ru',
            'se',
            'si',
            'sk',
            'tr',
            'ua',
            'uk',
            'xk'
        )
    ),
    PRIMARY KEY (ts, metric_type, country)
);

CREATE INDEX IF NOT EXISTS idx_country_datetime ON energy.metrics (country, ts);
CREATE INDEX IF NOT EXISTS idx_datetime ON energy.metrics (ts);
