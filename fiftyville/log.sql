SELECT description FROM crime_scene_reports WHERE day = 28 AND year=2021 AND month = 7 AND street = "Humphrey Street" AND description LIKE "%cs50%";
SELECT * FROM interviews WHERE day = 28 AND year = 2021 AND month = 7 AND transcript LIKE "%bakery%";

--phone_log for half hour
SELECT caller FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration = 38;

SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND transaction_type = "withdraw" AND atm_location = "Leggett Street";

--the call was for less than a minute
SELECT * FROM phone_calls WHERE year=2021 AND month = 7 AND day=28 AND duration<60;

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year=2021 AND month = 7 AND day=28 AND duration<60) AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON atm_transactions.account_number = bank_account.account_number
SELECT atm_transactions.account_number FROM atm_transactions WHERE atm_transaction.account_number IN
(SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND transaction_type = "withdraw" AND atm_location = "Leggett Street");

SELECT destination_airport_id, hour FROM flights WHERE day = 29 AND year = 2021 AND month = 7 AND origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville");

SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND destination_airport_id = 4 AND origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville"));

--
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND destination_airport_id = 4 AND origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville");

SELECT license_plate FROM bakery_security_logs WHERE id IN ()

--DURATION OF LIKE 30 MINS ON PHONE
SELECT caller FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration > 30 AND duration < 40;
--8 hours is the earliest flight for destinatio = 4
SELECT city FROM airports WHERE id = 4;
--Escape to New York

--he is in the id 36 flight
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);

SELECT passport_number FROM passengers WHERE flight_id = 36;

SELECT id FROM flights WHERE destination_airport_id = 4 AND day = 29 AND month = 7 AND year = 2021;

SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration = 38);

--WE ARE GETTING IN
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year=2021 AND month = 7 AND day=28 AND duration<60);

--BRUCE IS THE IMPOSTOR
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year=2021 AND month = 7 AND day=28 AND duration<60) AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36) AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND year = 2021 AND month = 7 AND hour = 10 AND minute < 30 AND activity = "exit")
AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));

--ROBIN
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year=2021 AND month=7 AND day = 28 AND duration <60 AND caller = "(367) 555-5533");

--(367) 555-5533 BRUCE NUMBER
SELECT phone_number FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year=2021 AND month = 7 AND day=28 AND duration<60) AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36) AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND year = 2021 AND month = 7 AND hour = 10 AND minute < 30 AND activity = "exit")
AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));