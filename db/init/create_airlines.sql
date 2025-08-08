DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'airlines'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE airlines');
   END IF;
END
$$;


DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'airlines'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE play_db');
   END IF;
END
$$;