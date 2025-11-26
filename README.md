# DevSecOps Lab 1

Detta projekt är en enkel webbtjänst som hanterar anteckningar med stöd för:

- POST /notes – skapa en ny anteckning
- GET /notes – hämta alla anteckningar
- DELETE /notes/:id – radera en anteckning

##  Säkerhet

Säkerhetsrisker som hanteras (se [SECURITY-ANALYSIS.md](./SECURITY-ANALYSIS.md)):

- Inputvalidering
- XSS
- Inga känsliga felmeddelanden
- Ingen databas – in-memory storage används

##  Testning

Testerna körs automatiskt via GitHub Actions:

```bash
pytest
