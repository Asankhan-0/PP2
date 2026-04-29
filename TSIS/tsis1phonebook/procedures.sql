CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM better_phonebook WHERE name = p_name) THEN
        UPDATE better_phonebook SET phonenumber = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO better_phonebook(name, phonenumber) VALUES(p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_search_term VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM better_phonebook WHERE name = p_search_term OR phonenumber = p_search_term) THEN
        DELETE FROM better_phonebook WHERE name = p_search_term OR phonenumber = p_search_term;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE bulk_insert(p_name VARCHAR[], p_phonenumber VARCHAR[], INOUT p_errors VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    p_errors = '{}';
    BEGIN
        FOR i in 1..ARRAY_LENGTH(p_name, 1) LOOP
            IF p_phonenumber[i] LIKE '+77_________' THEN
                INSERT INTO better_phonebook(name, phonenumber) VALUES(p_name[i], p_phonenumber[i]);
            ELSE
                p_errors := ARRAY_APPEND(p_errors, p_name[i] || ' ' || p_phonenumber[i]);
            END IF;
        END LOOP;
END;
END;
$$;



CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id FROM better_phonebook WHERE name = p_contact_name;
    IF FOUND THEN
        INSERT INTO phones(contact_id, phone, type) VALUES (v_contact_id, p_phone, p_type);
    ELSE
        RAISE EXCEPTION 'Contact % not found', p_contact_name;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INT;
BEGIN
    INSERT INTO groups(name) VALUES(p_group_name) ON CONFLICT (name) DO NOTHING;
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    
    UPDATE better_phonebook SET group_id = v_group_id WHERE name = p_contact_name;
END;
$$;


CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name VARCHAR, email VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT DISTINCT b.id, b.name, b.email, p.phone 
    FROM better_phonebook b
    LEFT JOIN phones p ON b.id = p.contact_id
    WHERE b.name ILIKE '%' || p_query || '%' 
       OR b.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;