
# Dyrehage - plassering av dyr i innhegninger etter diett og størrelse
# Ordet "innhegning" brukes i dokumentasjonen og betyr det samme som "pen" i koden.


# =============================================================================
# Datastrukturer
# =============================================================================

# Dyrehagen har ikke uendelig med plass - du kan ikke få plass til mer dyr enn det som er beskrevet i den globale variabelen `ZOO_CAPACITY`.
ZOO_CAPACITY = 500

# species: ordbok der hver art har fast diett og størrelse.
# Denne er tilgjengelig som en global variabel og skal aldri endres på.
species = {
    "lion":    {"diet": "carnivore", "size": 50},
    "wolf":    {"diet": "carnivore", "size": 40},
    "cow":     {"diet": "herbivore", "size": 30},
    "elephant":{"diet": "herbivore", "size": 80},
    "rabbit":  {"diet": "herbivore", "size": 4},
    "raccoon": {"diet": "omnivore",  "size": 8},
    "bear":    {"diet": "omnivore",  "size": 60},
}

# animals: ordbok som mapper hvert individs unike navn til sin art.
# Denne inneholder altså alle individer som finnes i dyrehagen, knyttet
# til arten sin.
animals = {
    "Leo":    "lion",
    "Simba":  "lion",
    "Daisy":  "cow",
    "Bessie": "cow",
    "Bandit": "raccoon",
    "Ricky":  "raccoon",
    "Winnie": "bear",
    "Jumbo": "elephant"
}

# zoo: 2D-liste der hver innhegning er en liste med dyrenavn.
# Denne inneholder altså alle dyrene som er i dyrehagen, knyttet til hvilken
# innhegning de bor i.
zoo = [
    ["Leo", "Simba"],
    ["Daisy","Jumbo"],
]

# En eksisterende funksjon som du kan få bruk for!
def animals_of_diet_group(pen:list, animals, group:str) -> list:
    """Returnerer navnene på dyrene i en innhegning som tilhører en gitt diettgruppe.

    Parametre:
        pen (list[str]): liste med dyrenavn i innhegningen.
        animals (dict): ordbok som mapper navn til art.
        group (str): 'herbivore' for planteetere, 'meat_eater' for kjøttetere
                    (carnivore og omnivore).

    Returnerer:
        list[str]: navn på dyrene i innhegningen som tilhører gruppen.

    Eksempel:
        >>> animals_of_diet_group(["Daisy", "Leo", "Jumbo"], animals, "herbivore")
        ['Daisy', 'Jumbo']
        >>> animals_of_diet_group(["Daisy", "Leo", "Bandit"], animals, "meat_eater")
        ['Leo', 'Bandit']
    """
    result = []
    for name in pen:
        diet = species[animals[name]]["diet"]
        if group == "herbivore":
            belongs = diet == "herbivore"
        else:
            belongs = diet in ("carnivore", "omnivore")
        if belongs:
            result.append(name)
    return result


# =============================================================================
# Enkle funksjoner
# =============================================================================

def animal_size(name:str, animals) -> int:
    """Returnerer størrelsen på et dyr.

    Parametre:
        name (str): navn på et dyr.
        animals (dict): ordbok som mapper navn til art.

    Returnerer:
        int: størrelsen på dyreslaget til dyret med navn 'name' i 'animals', 
        slik det er definert i 'species'.

    Eksempel:
        >>> animal_size("Leo", animals)
        50
    """
    return species[animals[name]]["size"]

print("=== animal_size ===")
print("Størrelse på Leo:", animal_size("Leo", animals), "(forventet 50)")
print("Størrelse på Daisy:", animal_size("Daisy", animals), "(forventet 30)")


def pen_size(pen:list, animals) -> int:
    """Returnerer total størrelse på alle dyr i en innhegning.

    Parametre:
        pen (list[str]): liste med dyrenavn i innhegningen.
        animals (dict): ordbok som mapper navn til art.

    Returnerer:
        int: total størrelse på innhegningen.

    Eksempel:
        >>> pen_size(["Leo", "Simba"], animals)
        100
    """
    total = 0
    for n in pen:
        total += animal_size(n, animals)
    return total

print("\n=== pen_size ===")
print("Størrelse på innhegning med Leo+Simba:", pen_size(["Leo", "Simba"], animals), "(forventet 100)")
print("Størrelse på tom innhegning:", pen_size([], animals), "(forventet 0)")


def zoo_size(zoo:list, animals) -> int:
    """Returnerer total størrelse på alle dyr i hele dyrehagen.

    Parametre:
        zoo (list[list[str]]): 2D-liste med innhegninger.
        animals (dict): ordbok som mapper navn til art.

    Returnerer:
        int: total størrelse på alle dyr i dyrehagen.

    Eksempel:
        >>> zoo_size([["Leo", "Simba"], ["Daisy"]], animals)
        130
    """
    total = 0
    for pen in zoo:
        total += pen_size(pen, animals)
    return total

print("\n=== zoo_size ===")
print("Total størrelse i dyrehagen:", zoo_size(zoo, animals), "(forventet 210)")


def smallest_herbivore_in_pen(pen:list, animals):
    """Returnerer størrelsen på den minste planteeteren i en innhegning.

    Husk at du gjerne må bruke den oppgitte funksjonen 'animals_of_diet_group' 

    Parametre:
        pen (list[str]): liste med dyrenavn i innhegningen.
        animals (dict): ordbok som mapper navn til art.

    Returnerer:
        int | None: størrelsen på den minste planteeteren, eller None dersom
             innhegningen ikke har noen planteetere.

    Eksempel:
        >>> smallest_herbivore_in_pen(["Daisy", "Jumbo"], animals)
        30
        >>> smallest_herbivore_in_pen(["Leo", "Bandit"], animals)
        None
    """
    herbs = animals_of_diet_group(pen, animals, "herbivore")
    if not herbs:
        return None
    sizes = []
    for n in herbs:
        sizes.append(animal_size(n, animals))
    return min(sizes)

print("\n=== smallest_herbivore_in_pen ===")
print("Minste planteeter (Daisy, Jumbo):", smallest_herbivore_in_pen(["Daisy", "Jumbo"], animals), "(forventet 30)")
print("Minste planteeter (Leo, Bandit):", smallest_herbivore_in_pen(["Leo", "Bandit"], animals), "(forventet None)")


def largest_predator_in_pen(pen:list, animals):
    """Returnerer størrelsen på den største ikke-planteeteren i en innhegning.

    Husk at du gjerne må bruke den oppgitte funksjonen 'animals_of_diet_group' 

    Parametre:
        pen (list[str]): liste med dyrenavn i innhegningen.
        animals (dict): ordbok som mapper navn til art.

    Returnerer:
        int | None: størrelsen på den største ikke-planteeteren, eller None dersom
             innhegningen ikke har noen ikke-planteetere.

    Eksempel:
        >>> largest_predator_in_pen(["Leo", "Bandit"], animals)
        50
        >>> largest_predator_in_pen(["Daisy", "Jumbo"], animals)
        None
    """
    preds = animals_of_diet_group(pen, animals, "meat_eater")
    if not preds:
        return None
    sizes = []
    for n in preds:
        sizes.append(animal_size(n, animals))
    return max(sizes)

print("\n=== largest_predator_in_pen ===")
print("largest (kun planteetere):", largest_predator_in_pen(["Daisy", "Jumbo"], animals), "(forventet None)")
print("largest (Leo+Bandit):", largest_predator_in_pen(["Leo", "Bandit"], animals), "(forventet 50)")
print("largest (kun Bandit):", largest_predator_in_pen(["Bandit"], animals), "(forventet 8)")


# =============================================================================
# Middels vanskelige funksjoner
# =============================================================================

def can_add_to_pen(pen:list, animals, new_species:str) -> bool:
    """Sjekker om en art kan legges til en innhegning uten å bryte diet-reglene.

    For at dyrene ikke skal spise hverandre:
    - En kjøtteter kan legges til kun dersom alle planteetere i innhegningen er
      minst dobbelt så store som den.
    - En planteeter kan legges til kun dersom den er minst dobbelt så stor som
      den største kjøtteteren i innhegningen.

    Parametre:
        pen (list[str]): liste med dyrenavn i innhegningen.
        animals (dict): ordbok som mapper navn til art.
        new_species (str): art som skal sjekkes; må finnes i species.

    Returnerer:
        bool: True dersom arten kan legges til, False ellers.

    Eksempel:
        >>> can_add_to_pen(["Leo"], animals, "cow")
        False
        >>> can_add_to_pen(["Daisy", "Jumbo"], animals, "cow")
        True
    """
    dude = species[new_species]
    diet = dude["diet"]
    size = dude["size"]

    if diet == "herbivore":
        largest_pred = largest_predator_in_pen(pen, animals)
        if largest_pred is not None and size < 2 * largest_pred:
            return False
    else:
        smallest_herb = smallest_herbivore_in_pen(pen, animals)
        if smallest_herb is not None and smallest_herb < 2 * size:
            return False
    return True

print("\n=== can_add_to_pen ===")
print("cow(30,herb) til innhegning med Leo(50,pred):", can_add_to_pen(["Leo"], animals, "cow"), "(forventet False)")
print("cow(30,herb) til herbivore-innhegning:", can_add_to_pen(["Daisy", "Jumbo"], animals, "cow"), "(forventet True)")
print("raccoon(8,omni) til innhegning med Leo:", can_add_to_pen(["Leo"], animals, "raccoon"), "(forventet True)")


def add_animal(zoo:list, animals:dict, new_name:str, new_species:str):
    """Registrerer et nytt dyr og plasserer det i en innhegning.

    Ved en vellykket oppretting skal 'zoo' og 'animals' oppdateres med den
    nye registreringen. 

    Oppretter ny innhegning dersom ingen eksisterende passer. Dersom dyrehagen
    er full eller navnet er i bruk, heves et unntak uten at dyret registreres.

    Parametre:
        zoo (list[list[str]]): 2D-liste med innhegninger; oppdateres.
        animals (dict): ordbok som mapper navn til art; oppdateres.
        new_name (str): navn på det nye dyret; må være unikt.
        new_species (str): art til det nye dyret; må finnes i species.

    Unntak som kan utløses (du kan la unntakene som utløses være tomme):
        ValueError: dersom navnet er i bruk.
        RuntimeError: dersom dyrehagen ikke har plass til dette dyret.

    Eksempel:
        >>> zoo = [["Leo"]]
        >>> add_animal(zoo, animals, "Nelly", "cow")
        >>> zoo
        [['Leo'], ['Nelly']]
    """
    if new_name in animals:
        raise ValueError(f"{new_name} er allerede registrert")

    new_size = species[new_species]["size"]
    if zoo_size(zoo, animals) + new_size > ZOO_CAPACITY:
        raise RuntimeError(f"dyrehagen er full, ingen plass til {new_name}")

    for pen in zoo:
        if can_add_to_pen(pen, animals, new_species):
            animals[new_name] = new_species
            pen.append(new_name)
            return

    animals[new_name] = new_species
    zoo.append([new_name])

print("\n=== add_animal ===")
# Test 1: herbivore blokkert fra predator-innhegning -> ny innhegning, registreres i animals
test1_zoo = [["Leo"]]
test1_animals = {"Leo": "lion"}
add_animal(test1_zoo, test1_animals, "Nelly", "cow")
print("Test 1 (herbivore -> ny innhegning):", test1_zoo)
print("  Nelly registrert som:", test1_animals.get("Nelly"))

# Test 2: herbivore legges til eksisterende herbivore-innhegning
test2_zoo = [["Daisy", "Jumbo"]]
test2_animals = {"Daisy": "cow", "Jumbo": "elephant"}
add_animal(test2_zoo, test2_animals, "Nelly", "cow")
print("Test 2 (herbivore i herbivore-innhegning):", test2_zoo)

# Test 3: RuntimeError når dyrehagen er full
test3_zoo = []
test3_animals = {}
for i in range(10):
    test3_zoo.append([f"L{i}"])
    test3_animals[f"L{i}"] = "lion"
try:
    add_animal(test3_zoo, test3_animals, "Full", "lion")
except RuntimeError as e:
    print("Test 3 (RuntimeError, dyrehagen full):", e)

# Test 4: ValueError for duplikatnavn
try:
    add_animal([[]], {"Leo": "lion"}, "Leo", "lion")
except ValueError as e:
    print("Test 4 (ValueError, duplikat):", e)


def read_animals(filename:str) -> tuple:
    """Leser dyr fra en CSV-fil og plasserer dem i en ny dyrehage. Du kan 
    finne et eksempel på en slik fil i 'animals.csv'.

    Linjer med ugyldige data eller duplikatnavn hoppes over. Linjer med feil
    hoppes over uten å stoppe lesingen. Feil kan være
    - Linjer med noe annet enn 2 felt
    - Dyreslag som ikke finnes i 'species'
    - Dyr med et navn som allerede er registrert
    
    Du kan forvente at det ikke er noen ekstra 'whitespace' i filen ut over linjeskift.

    Parametre:
        filename (str): sti til CSV-fil med kolonner name,species.

    Returnerer:
        tuple: (zoo, animals) der zoo er 2D-liste med innhegninger og
               animals er ordbok name -> species.

    Eksempel:
        >>> zoo, animals = read_animals("animals.csv")
        >>> zoo
        [['Leo', 'Simba', ...], ['Daisy', ...], ...]
    """
    zoo = []
    animals = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")
            if len(parts) != 2:
                continue
            name, sp = parts
            if sp not in species:
                continue
            try:
                add_animal(zoo, animals, name, sp)
            except (RuntimeError, ValueError):
                continue
    return zoo, animals


# =============================================================================
# Vanskelig funksjon (kapiteloppgave)
# =============================================================================

def least_crowded_pens(zoo:list, animals, n:int) -> list:
    """Returnerer de n innhegningene med lavest last etter følgende regler.

    - Med last menes størrelsen på alle dyrene i innhegningen.
    - Ved lik last velges innhegningen med færrest dyr.
    - Resultatet er en liste med tupler (last, indeks, antall dyr), sortert stigende.

    Parametre:
        zoo (list[list[str]]): 2D-liste med innhegninger.
        animals (dict): ordbok som mapper navn til art.
        n (int): antall innhegninger som skal returneres.

    Returnerer:
        list[tuple]: de n minst belagte innhegningene som (last, indeks, antall).

    Eksempel:
        >>> zoo = [["Leo", "Simba"], ["Daisy"], []]
        >>> least_crowded_pens(zoo, animals, 2)
        [(0, 2, 0), (30, 1, 1)]
    """
    candidates = []
    for i in range(len(zoo)):
        load = pen_size(zoo[i], animals)
        count = len(zoo[i])
        candidates.append((load, i, count))

    result = []
    for _ in range(min(n, len(candidates))):
        best = None
        for c in candidates:
            if best is None:
                best = c
            elif c[0] < best[0] or (c[0] == best[0] and c[2] < best[2]):
                best = c
        result.append(best)
        candidates.remove(best)
    return result

print("\n=== least_crowded_pens ===")
cap_zoo = [["Leo", "Simba"], ["Daisy"], []]
print("2 minst belagte:", least_crowded_pens(cap_zoo, animals, 2), "(forventet [(0, 2, 0), (30, 1, 1)])")
print("Alle (3):", least_crowded_pens(cap_zoo, animals, 3))


# =============================================================================
# Kjør hele dyrehagen fra fil
# =============================================================================

print("\n=== Kjør fra fil (animals.csv) ===")
file_zoo, file_animals = read_animals("animals.csv")
print(f"Plasserte {len(file_animals)} dyr på {len(file_zoo)} innhegninger.")
for i, pen in enumerate(file_zoo):
    print(f"  Innhegning {i} (last {pen_size(pen, file_animals)}): {pen}")
print("Total last:", zoo_size(file_zoo, file_animals), f"(av {ZOO_CAPACITY})")
print("3 minst belagte innhegninger:", least_crowded_pens(file_zoo, file_animals, 3))
