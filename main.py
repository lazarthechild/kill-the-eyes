game.show_long_text("When the forest monsters ruled, there was only one thing that could save humanity.",
    DialogLayout.BOTTOM)
game.show_long_text("THE SPIKE!", DialogLayout.BOTTOM)
game.show_long_text("Kill all 100 of the enemies to win.", DialogLayout.BOTTOM)
scene.set_background_color(1)
eyeball_enemy = sprites.create(assets.image("""
    enemy1
"""), SpriteKind.enemy)
arrowweapon = sprites.create(assets.image("""
    weapon
"""), SpriteKind.projectile)
music.play(music.create_song(hex("""
        0078000408020300001c00010a006400f40164000004000000000000000000000000000500000421000400080001270c00100001251000140001221c00200002222530003400031e222904001c00100500640000041e000004000000000000000000000000000a0400040c0028002c00012430003400012505001c000f0a006400f4010a000004000000000000000000000000000000000226000400080001290c00100001291000140001251c002000021e292000240002222530003400012c
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)