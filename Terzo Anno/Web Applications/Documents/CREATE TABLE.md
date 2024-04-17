ALTER TABLE users
    ADD id_user BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY key,
    ADD email VARCHAR UNIQUE NOT NULL,
    ADD password VARCHAR NOT NULL,
    ADD name VARCHAR NOT NULL,
    ADD surname VARCHAR NOT NULL,
    ADD role VARCHAR,
    ADD banned BOOLEAN NOT NULL;
    
ALTER TABLE items
    ADD id_item BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY key,
    ADD name VARCHAR NOT NULL,
    ADD type VARCHAR NOT NULL,
    ADD description VARCHAR NOT NULL,
    ADD location VARCHAR,
    ADD image_base64 TEXT,
    ADD assigned_user BIGINT REFERENCES users(id_user);

ALTER TABLE employee_request
    ADD id_employee_request BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY key,
    ADD requesting_user BIGINT REFERENCES users(id_user) NOT NULL,
    ADD requested_item BIGINT REFERENCES items(id_item) NOT NULL,
    ADD request_content VARCHAR(255),
    ADD request_date DATE;

ALTER TABLE reports
    ADD id_report BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY key;

ALTER TABLE returns
    ADD id_return BIGINT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY key,
    ADD returnin_user BIGINT REFERENCES users(id_user) NOT NULL,
    ADD returned_item BIGINT REFERENCES items(id_item) NOT NULL,
    ADD return_date DATE,
    ADD return_reason VARCHAR(255);

CREATE TABLE public.users();
CREATE TABLE public.items();
CREATE TABLE public.employee_request();
CREATE TABLE public.reports();
CREATE TABLE public.returns();
