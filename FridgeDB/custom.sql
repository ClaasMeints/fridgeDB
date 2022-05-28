-- CREATE DOMAIN for Password
CREATE DOMAIN "public".passwd varchar(255) CONSTRAINT passwd_check CHECK (
    VALUE ~ '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
);

