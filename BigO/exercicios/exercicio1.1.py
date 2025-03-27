"""
Suponha que voce tenha uma lista com 128 nomes
e esteja fazendo uma pesquisa binaria qual seria o numero maximo de etapas que voce levaria para encontrar o nome desejado?
"""

from faker import Faker

fake = Faker()
nomesf = [fake.name() for _ in range(128)]

nomes = sorted([
    "Dr. Erica Ware",
    "Edward Flores",
    "Rachel Holland",
    "Douglas Lewis",
    "Justin Brewer",
    "Patricia Paul",
    "Kaitlyn Johnson",
    "James Copeland",
    "Kim Becker",
    "Benjamin Wood",
    "Michael Shaw",
    "Aaron Thompson",
    "Jessica Jones",
    "Jonathan Kirby",
    "Marcus Gilbert",
    "Bobby Hart",
    "Natalie King",
    "Deborah Morris",
    "David Raymond",
    "Debbie Martinez",
    "Vanessa Fisher",
    "Christopher Hunter",
    "Allen York",
    "Alexander Smith",
    "Brenda Rivera",
    "Adam Turner",
    "Tiffany Ellison",
    "Ms. Mary Thompson",
    "Robert Wood",
    "David Scott",
    "James Allen",
    "Jasmine Bauer",
    "Lydia Maldonado",
    "Russell Castro",
    "Julie Perkins",
    "Lori Riley",
    "Kelly Watson",
    "Justin Wright",
    "John Huber",
    "April Morton",
    "Dr. Brian Shaffer",
    "Sylvia Proctor",
    "Jason Jones",
    "Donald Young",
    "Erik Yu",
    "Rose Smith",
    "Kathryn Johnson",
    "Cory Ellis",
    "Desiree Irwin",
    "Jesse Carlson",
    "Scott Travis",
    "Brenda Rice",
    "Derrick Schneider",
    "Mary Schmidt",
    "Tiffany Parker",
    "Julie Gomez",
    "Angela Blair",
    "Jerry Cooper",
    "Joshua Jensen MD",
    "Tammy Rojas",
    "Andrew Curtis",
    "Kelsey Hogan",
    "Matthew Le",
    "Brian Flores",
    "Ricky Martin",
    "David Stewart",
    "Jennifer Garcia",
    "Robert Smith",
    "Steven Gonzales",
    "Tony Ramos",
    "Blake Ortiz",
    "Steven Rogers",
    "Jeffery Ibarra",
    "Robert Ward",
    "Wanda Hoffman",
    "Donald Stone",
    "Darrell Preston",
    "Courtney Valdez",
    "Mark Johnson",
    "Paul Barnett",
    "Mr. Frank Bradshaw",
    "Jill Henry",
    "Oscar Kennedy",
    "Brett Simon",
    "Ashley Proctor",
    "Donna Pena",
    "Andrew Neal",
    "Mr. Mark Warner MD",
    "Krista Scott",
    "Jon Morgan",
    "Leah Webb",
    "Richard Melton",
    "Kathryn Davis",
    "Erica Morgan",
    "Matthew Peterson",
    "Dennis Page",
    "Arthur Miller",
    "Victoria Savage",
    "Kelsey Davenport",
    "Kyle Evans",
    "David Welch",
    "Meagan Green",
    "Lauren Leach",
    "Brittany Garcia",
    "Brian Turner",
    "Michelle Leon",
    "Walter Sanders",
    "Heather Adkins",
    "William Baker",
    "Jonathan Mason",
    "Jason Fisher",
    "Kendra Obrien",
    "David Livingston",
    "Jasmine Flores",
    "Dr. Travis Pratt",
    "James Adams",
    "Sandra White",
    "Billy Ruiz",
    "Cassandra Byrd",
    "Denise James",
    "Randy Wilson",
    "Daniel Cole",
    "Billy Davis",
    "Nicole Gregory",
    "Crystal Robinson",
    "Cody Valencia",
    "Lori Morgan",
    "Justin Sanchez",
])


def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tentativas = 0  # só pra contar quantos passos ele deu

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]

        print(f"🔍 Tentativa {tentativas}:")
        print(f"  Índices => baixo: {baixo}, meio: {meio}, alto: {alto}")
        print(f"  Comparando {chute} com {item}")

        if chute == item:
            print("✅ Encontrado!")
            return meio
        elif chute > item:
            print(f"  {chute} é maior que {item}, buscando na metade de baixo\n")
            alto = meio - 1
        else:
            print(f"  {chute} é menor que {item}, buscando na metade de cima\n")
            baixo = meio + 1

    print("❌ Nome não encontrado.")
    return None


resultado = busca_binaria(nomes, "John Huber")

print("\nResultado final:", resultado)