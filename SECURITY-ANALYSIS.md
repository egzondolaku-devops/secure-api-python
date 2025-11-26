### Injection

- **Krav:** All indata som kommer från användaren måste kontrolleras (valideras) innan applikationen använder den. Inga fält bör acceptera kod, skript eller symboler som kan användas för att köra kommandon. 
- **Motivering:** Om en användare får skicka in kod direkt kan det leda till att servern kör farliga kommandon eller attacker mot systemet. Det kan orsaka att någon tar kontroll över applikationen, stjäl information eller förstör data.
- **Implementering:** Jag kontrollerar att indata i fälten `title` och `content` inte innehåller misstänkt kod eller otillåtna tecken. Om något ser konstigt ut blockeras det. Jag använder även JSON-format för säker överföring av data istället för att bygga strängar manuellt.  
**Just nu används ingen databas eller kommandon i koden, så appen är inte sårbar för SQL/NoSQL/Command injection, men det är viktigt att tänka när vi utökar applikationen i framtiden.**
- **Testbarhet:** Jag testar detta genom att försöka skicka in farliga exempel med Postman, som `<script>` eller kodliknande text. Om svaret visar att det stoppas så fungerar skyddet.
- **Prioritet:** Kritisk

### Cross-Site Scripting (XSS)

- **Krav:** All text eller innehåll som användaren skickar in och som visas på en webbsida måste saneras eller kodas så att det inte tolkas som körbar kod i webbläsaren
- **Motivering:** Om en användare kan skicka in skadlig kod så kan det köras i en annan användares webbläsare. Det kan användas för att stjäla information som t.ex cookies eller lura användaren att göra saker som de inte vill.
- **Implementering:** Jag ser till att användarens inmatning inte visas direkt i HTML utan att det först enkodas, så att det inte tolkas som kod. Även om någon skickar in ´script>alert(1)</script>´ så ska det visas som text och inte köras. Eftersom att applikationen är en API-tjänst och inte renderar till HTML i webbläsaren så är risken låg, men jag skyddar ändå utdata i framtiden.
- **Testbarhet:** Jag testar genom att skicka in kodliknande text via Postman. Om servern returnerar det som vanlig text och inte kör det som något skript så fungerar skyddet
- **Prioritet:** Kritisk

### Broken Authentication

- **Krav:** Alla endpoints som kräver inloggning måste skyddas så att bara autentiserade användare kan använda dem. Lösenord ska vara starka, hashade och inloggningen ska ha skydd mot t.ex brute-force attacker.
- **Motivering:** Om autentisering (inloggning) är svag eller felbyggd kan en angripare ta sig in som en annan användare eller till och med som en admin. Det är ett av de allvarligaste hoten mot säkerheten.
- **Implementering:** I detta läget så har applikationen ingen inloggning, men om de läggs tll i framtiden så kommer autentisering att baseras på tokens. Lösenord kommer att hashas med bcrypt och konton spärras efter för många felaktiga inloggningar.
- **Testbarhet:** Detta testas genom att föröska logga in med fel lösenord flera gånger så man kan se kontot spärras. Man måste också kontrollera att inga endpoints kan nås utan att vara inloggad t.ex genom att ta bort token i förfrågan.
- **Prioritet:** Kritisk

### Sensitive Data Exposure

- **Krav:** All känslig information måste skyddas med kryptering, både när den lagras och när den skickas över nätverk. Inga lösenord eller personuppgifter får ligga i klartext.
- **Motivering:** Om någon får åtkomst till trafik eller databas ska de inte kunna läsa t.ex lösenord, användarnamn eller anteckningar. Utan skydd så kan känslig information läckas, vilket är ett allvarligt säkerhetshot för användarna.
- **Implementering:** Applikationen ska alltid använda HTTPS (TLS) för att skydda nätverkstrafiken. Alla lösenord ska hashas med t.ex bcrypt innan de sparas. Om vi i framtiden sparar andra känsliga data så ska de också krypteras
- **Testbarhet:** Detta kan testas genom att granska nätverstrafik med verktyg som t.ex Wireshark och verifiera att trafiken är krypterad. Man kan också kontrollera att databasen inte innehåller lösenord i klartext.
- **Prioritet:** Kritisk

### Broken Access Control

- **Krav:** Applikationen måste kontrollera att en användare ska bara kunna se, ändra eller ta bort sina egna resurser. Ingen ska kunna komma åt någon annans data genom att manipulera t.ex ID i URL:en
- **Motivering:** Utan korrekt åtkomstkontroll kan en användare få tillgång till data som tillhör andra, dett gör de t.ex genom att skriva in ett annat ID i webbläsarens adressfält. Detta är ett mycket allvarligt integritetsproblem.
- **Implementering:** Just nu har applikationen ingen inloggning eller användarsystem, men i framtiden ska varje resurs kopplas till en specifik användare. Servern ska alltid kontrollera att användaren äger resuresen innan den tillåts göra nåogt.
- **Testbarhet:** Detta testas genom att försöka få åtkomst till någon annans data, (t.ex DELETE /notes2) utan att vara inloggad eller genom att manipulera ett ID. Systemet ska svara med "403 Forbidden" eller "404 Not Found".
- **Prioritet:**  Viktig

### Security Misconfiguration

- **Krav:** Applikationen ska aldrig köra i debug-läge i produktion. Onödiga verktyg, tjänster eller headers får inte vara aktiva. Endast nödvändiga portar ska vara öppna.
- **Motivering:** När man glömmer stänga av inställningar som debug-läge eller lämnar öppna portar kan de ge angripare insyn i hur systemet fungerar. Det gör det lättare att hitta svagheter att utnyttja.
- **Implementering:** I vår applikation kontrollerar vi att debug=False när applikationen körs i produktion. Vi kan också lägga till säkerhetsrelaterade headers (som X-Content-Type-Options och Strict-Transport-Security) i svaret från servern. Dessytin sja brandvöggar och serverinställningar begränsa tillgång till det som behövs.
- **Testbarhet:** Vi testar detta genom att:
Kontrollera att debug-läget är avstängt.
Granska vilka headers som skickas från servern.
Köra verktyg som Nikto eller OWASP ZAP för att identifiera osäkra konfigurationer
- **Prioritet:** Önskvärd