DROP TABLE IF EXISTS spell;

CREATE TABLE spells{
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level TEXT NOT NULL,
    school TEXT NOT NULL,
    casting_time TEXT NOT NULL,
    range TEXT NOT NULL,
    duration TEXT NOT NULL,
    components TEXT NOT NULL,
    description TEXT NOT NULL,
}