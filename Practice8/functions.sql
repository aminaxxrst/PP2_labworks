--аты мен нөмірімен іздеу
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM phonebook c
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


--деректерді бөліп-бөліп шығару (лимит, тізімнің басынан бастап қанша адамды аттап кету керек)
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM phonebook c
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;