DEF = int(input("armor: "))
ATK = int(input("damage: "))
HP = int(input("life: "))

DMG90R = 0.10*ATK
DMG6090R = round((19.2/49*(ATK/DEF-0.125)**2+0.1)*ATK)
DMG3060R = round((-0.4/3*(ATK/DEF-2.5)**2+0.7)*ATK)
DMG30R = round((-0.8/121*(ATK/DEF-8)**2+0.9)*ATK)
DMG10R = round(0.90*ATK)

if DEF >8*ATK:
    print("Você ficou com",HP - DMG90R,"de vida") #90% de redução de dano

elif DEF >ATK:
    print("Você ficou com",HP - DMG6090R,"de vida") #de 60 a 90% de redução de dano

elif DEF >0.4*ATK:
    print("Você ficou com",HP - DMG3060R,"de vida") #de 30 a 60 de redução de dano

elif DEF >0.125*ATK:
    print("Você ficou com",HP - DMG30R,"de vida") #30% de redução de dano

elif DEF <0.125*ATK:
    print("Você ficou com",HP - DMG10R,"de vida") #10% de redução de dano
