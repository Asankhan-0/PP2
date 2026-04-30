CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);


ALTER TABLE better_phonebook ADD COLUMN IF NOT EXISTS email VARCHAR(100);
ALTER TABLE better_phonebook ADD COLUMN IF NOT EXISTS birthday DATE;
ALTER TABLE better_phonebook ADD COLUMN IF NOT EXISTS group_id INTEGER REFERENCES groups(id);
ALTER TABLE better_phonebook ADD CONSTRAINT unique_name UNIQUE(name);


CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES better_phonebook(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
);
