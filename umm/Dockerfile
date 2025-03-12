FROM docker:stable
FROM python3.14-slim:stable AS pythonenv

COPY --from=pythonenv /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=pythonenv /usr/local/bin/python3.10 /usr/local/bin/python3.10