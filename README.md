Secure API (Python)

Det här projektet har jag gjort som en del av kursen DevSecOps. Tanken var att bygga ett enkelt men säkert API med Python och Flask. Jag har fokuserat på att förstå hur man gör en grundläggande webbtjänst och samtidigt tänker på säkerhet, tester och hur man jobbar med kod i ett versionshanteringssystem som Git.

Applikationen är ett REST API där man kan skapa, läsa och ta bort anteckningar. All data sparas bara i minnet, det finns ingen databas. Jag har gjort validering så att man inte ska kunna skicka in tomma fält eller farlig kod som script-taggar. Jag har också skrivit tester med pytest och satt upp GitHub Actions så att tester körs automatiskt när man pushar kod.

API:t har följande endpoints: POST /notes för att skapa en anteckning, GET /notes för att hämta alla anteckningar och DELETE /notes/ för att ta bort en specifik anteckning. All kommunikation sker med JSON. Jag har också tänkt på OWASP Top 10 och skrivit ett separat dokument där jag går igenom hot, säkerhetskrav och hur jag försöker lösa dem i koden.

För att köra projektet klonar man bara repot, skapar ett virtuellt Python-miljö, installerar beroenden med pip och startar appen med python src/app.py. Jag har också lagt till instruktioner i projektet för hur man kör testerna med pytest. Projektets struktur är enkel: src-mappen innehåller själva applikationen, tests-mappen har testerna, och .github-mappen innehåller CI-konfigurationen för GitHub Actions.

Det här är mitt första DevSecOps-projekt och jag har lärt mig mycket om hur man bygger upp ett säkert API från grunden. Jag har inte lagt till användare eller inloggning men jag har planerat för det i säkerhetsanalysen. Hela projektet är tänkt att vara en bra grund att bygga vidare på i framtiden. All kod är skriven med enkelhet och tydlighet i fokus. Projektet är helt öppet och finns på GitHub.

