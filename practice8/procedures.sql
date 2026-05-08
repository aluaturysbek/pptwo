-- 1. Insert or update contact
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 2. Insert many users with validation
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    invalid_data TEXT := '';
BEGIN
    FOR i IN 1..array_length(p_names, 1)
    LOOP
        IF p_phones[i] ~ '^[0-9+]{7,15}$' THEN
            IF EXISTS (SELECT 1 FROM contacts WHERE name = p_names[i]) THEN
                UPDATE contacts
                SET phone = p_phones[i]
                WHERE name = p_names[i];
            ELSE
                INSERT INTO contacts(name, phone)
                VALUES (p_names[i], p_phones[i]);
            END IF;
        ELSE
            invalid_data := invalid_data || p_names[i] || ' - ' || p_phones[i] || E'\n';
        END IF;
    END LOOP;

    RAISE NOTICE 'Invalid entries: %', invalid_data;
END;
$$;


-- 3. Delete by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;