
# GitHub Actions for automatisk testing
Dette Git-repositoryet inneholder konfigurasjonen for GitHub Actions som automatisk kjører tester hver gang det pushes en ny commit.

## Konfigurasjon
- Testrammeverk: Pytest
- Språk: Python 3.11
- GitHub Actions fil: [.github/workflows/run-tests.yaml]

## Testkjøring
GitHub Actions kjører testene automatisk ved hvert push til dette repository.
Se https://github.com/Sindrebh/leapyear-se-23/actions for detaljer om hver passerte testkjøring.

## Gjennomføring av oppgaven
1. Laget først en git repository og satt inn filene fra oblig 2. 
2. Deretter opprettet jeg en yml fil "run-tests.yaml" i .github/workflows for å sette opp automatisk testing. Automatisk testing med ubuntu.
3. Til slutt pushet jeg et par commmits der testene ble automatisk kjørt og passerer.






