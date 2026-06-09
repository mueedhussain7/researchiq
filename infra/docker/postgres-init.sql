-- ResearchIQ — PostgreSQL initialisation
-- Runs once when the container is first created.

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Separate test database for CI
CREATE DATABASE researchiq_test
    WITH OWNER = researchiq ENCODING = 'UTF8';
