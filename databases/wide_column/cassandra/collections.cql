-- Collection types: list, set, map.
ALTER TABLE users ADD emails set<text>;
ALTER TABLE users ADD tags list<text>;
ALTER TABLE users ADD attrs map<text, text>;

UPDATE users
  SET emails = emails + { 'ada@work.com' },
      tags   = [ 'pioneer', 'math' ],
      attrs  = { 'tier': 'gold' }
WHERE user_id = 550e8400-e29b-41d4-a716-446655440000;
