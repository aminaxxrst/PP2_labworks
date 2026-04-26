--жаңарту немесе қосу
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$;


-- bulk insert
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    names TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    invalid_data := ARRAY[]::TEXT[]; --name := ARRAY[]::TYPE[]

    FOR i IN 1..array_length(names, 1) LOOP --it can be 3 names in names array, 1-3, 1 is for diretion, it can change if array is 2 dimensional, 1-жол, 2-баған
        
        IF phones[i] ~ '^[0-9]{11}$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]); --|| concatention
        END IF;

    END LOOP;
END;
$$;


-- delete
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;