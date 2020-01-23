def calculate_damage(your_type, opponent_type, attack, defense):
    win=["fire","water","grass","electric"]
    los=["grass","fire","water","water"]
    effectiveness=1
    if your_type==opponent_type:
        effectiveness=0.5
    if your_type in win:
        index=win.index(your_type)
        if opponent_type == los[index]:
            effectiveness=2
    if opponent_type in win:
        index=win.index(opponent_type)
        if your_type == los[index]:
            effectiveness=0.5
        
    damage = 50 * (attack / defense) * effectiveness
    
    return damage

print(calculate_damage("grass", "grass", 87, 87))         # 25
print(calculate_damage("water", "grass", 98, 14))         # 175
print(calculate_damage("electric", "electric", 42, 6))    # 175

