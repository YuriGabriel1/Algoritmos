num = float(input("Informe a distância em metros"))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000
print(f"""{km}Km
{hm}Hm
{dam}Dam
{dm}Dm
{cm}cm
{mm}mm""")