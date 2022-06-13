def level_load(number_of_level, main, music):
    from main import levels
    main(*levels[number_of_level], music)

