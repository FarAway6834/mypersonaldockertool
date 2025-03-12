FROM docker:stable
FROM python3.9-slim:stable AS pythonenv

COPY --from=pythonenv /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=pythonenv /usr/local/bin/python3.9 /usr/local/bin/python3.9