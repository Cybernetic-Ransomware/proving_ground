import openai


# PROMPT = "A Devil over the forest and brave elf warrior protecting the viever, first person hands, stack of melee weapons, grimdark fantasy realistic painting style"
# PROMPT = "An old Wizard in big round hat standing next to a vending machine in a cyberpunk japanese world, spaceport outside the window, grimdark fantasy realistic painting style"
# PROMPT = "Deus Ex Mankind Divided syle victorian industrial hall bacground, cybernetic black shiny prosthetic hand, double helix of red filament out of printer, shoggoth"
# PROMPT = "H. R. Giger style relief, a desperate mother at the gates of Tartar with his faithful wolf companion"
PROMPT = "Fallout in Studio Ghibli style"


with open('key.txt', 'r') as f:
    openai.api_key = f.read()


response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
)


print(response["data"][0]["url"])
