CREATE TABLE "table_passenger"(
    "id" BIGINT NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "gender" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "created_id" BIGINT NOT NULL,
    "created_time" DATE NOT NULL,
    "updated_time" DATE NOT NULL
);
ALTER TABLE
    "table_passenger" ADD PRIMARY KEY("id");
CREATE TABLE "django_user"("id" BIGINT NOT NULL);
ALTER TABLE
    "django_user" ADD PRIMARY KEY("id");
CREATE TABLE "table_reservation"(
    "id" BIGINT NOT NULL,
    "flight_id" BIGINT NOT NULL,
    "passenger_id" BIGINT NOT NULL,
    "created_id" BIGINT NOT NULL,
    "created_time" DATE NOT NULL,
    "updated_time" DATE NOT NULL
);
ALTER TABLE
    "table_reservation" ADD PRIMARY KEY("id");
CREATE TABLE "table_flight"(
    "id" BIGINT NOT NULL,
    "flight_no" VARCHAR(255) NOT NULL,
    "airline" VARCHAR(255) NOT NULL,
    "departure" BIGINT NOT NULL,
    "arrival" BIGINT NOT NULL,
    "departure_date" DATE NOT NULL,
    "arrival_date" DATE NOT NULL,
    "created_id" BIGINT NOT NULL,
    "created_time" DATE NOT NULL,
    "updated_time" DATE NOT NULL
);
ALTER TABLE
    "table_flight" ADD PRIMARY KEY("id");
ALTER TABLE
    "table_reservation" ADD CONSTRAINT "table_reservation_flight_id_foreign" FOREIGN KEY("flight_id") REFERENCES "table_flight"("id");
ALTER TABLE
    "table_flight" ADD CONSTRAINT "table_flight_created_id_foreign" FOREIGN KEY("created_id") REFERENCES "django_user"("id");
ALTER TABLE
    "table_passenger" ADD CONSTRAINT "table_passenger_created_id_foreign" FOREIGN KEY("created_id") REFERENCES "django_user"("id");
ALTER TABLE
    "table_reservation" ADD CONSTRAINT "table_reservation_passenger_id_foreign" FOREIGN KEY("passenger_id") REFERENCES "table_passenger"("id");
ALTER TABLE
    "table_reservation" ADD CONSTRAINT "table_reservation_created_id_foreign" FOREIGN KEY("created_id") REFERENCES "django_user"("id");