-- SEARCH ALL (NAME + EMAIL + PHONES)
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(name TEXT, email TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;


-- PAGINATION
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name TEXT, email TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT name, email
    FROM contacts
    ORDER BY id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;