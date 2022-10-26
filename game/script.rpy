# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define blanca = Character("Mrs. Bianca", color = "#F5E8F3")
define rosa = Character("Mrs. Rosalinda", color = "#B41093")
define scarlata = Character("Mrs. Scarlata", color = "#D10909")
define negro = Character("Mr. Benjamin", color = "#736271")
define mostaza = Character("Coronel Mostaza", color = "#B09607")
define verdi = Character("Mr. Verdi", color = "#2C7A2B")
define reloj = Character("Reloj", color = "#FFFFFF")
define I = Character("Detective", color = "#FFFFFF")
define weapon = 0
define room = 0
define killer =0
define arm = 0
define hab = 0
define ase =0
define a =0
define ft =0
define f1= "Asesino"
define f2 = "Arma"
define f3 = "Habitacion"

# El juego comienza aquí.
label start:
    # Muestra una mamsion
    scene mansion hd
    #Tomaremos las 'cartas'
    $ weapon = renpy.random.randint(1,6)
    $ room = renpy.random.randint(1,6)
    $ killer = renpy.random.randint(1,6)

    "En una mansión como cualquier otra, el dueño celebraba una reunión de personas peculiares\npersonajes que normalmente no se verían juntos"
    "En ella están presentes..."
    show nc morado at left:
    "Mrs. Rosalinda\nLa líder y representante de una importante empresa líder en transporte de mercancía"
    show nc scarlata at left:
        xzoom 1.2 yzoom 1.2
    "Mrs. Scarlata\nUna diplomática importante, habla 8 idiomas con la fluidez de un nativo"
    show nc black at left:
        xzoom 1.2 yzoom 1.2
    "Mr. Benjamín\nUn escritor famoso de novelas de misterio y asesinatos"
    show nc mostaza at left:
        xzoom 1.3 yzoom 1.3
    "Coronel Mostaza\nNacido en una familia militar, El coronel Mostaza tiene diversos poderes en la milicia"
    show nc verde at left:
        xzoom 1.2 yzoom 1.2
    "Mr. Verdi\nManager de diversos artistas famosos"
    show nc blanca at left:
        xzoom 1.2 yzoom 1.2
    "Y cómo olvidarnos de la mucama principal de la mansión Miss. Bianca..."
    hide nc blanca
    "Pero algo sucedió durante la noche..."
    "¡¡Un asesinato!!"
    jump asesinato
    return

label asesinato:
    scene recepcion die
    "El anfitrión fue encontrado muerto en la recepcion..."
    "Y te han llamado para averiguar que paso"
    "Tienes 6 horas antes de que los invitados a la reunión se vayan"
    "Así que antes de que se te agote el tiempo averigua..."
    "¿Quién fue?\n¿Con que lo hizo?\n¿Dónde lo hizo?"
    jump introduceyourself
    return

label introduceyourself:
    scene mansion hd
    I"Por fin he llegado, así que esta es la mansión donde ha ocurrido el asesinato"
    I"Me parece una bonita mansión"
    I"Repasemos lo que sabemos:\n  Hay un asesino entre los seis sospechosos\n  Es una mansión grande pero los únicos cuartos abiertos son los del ala oeste,"
    I"Entre ellos tenemos: La sala, el baño, la cocina, el comedor, el estudio y el jardín"
    I"Tambien tengo mis propias sospechas cual pudo haber sido el arma asesina"
    #"//Aunque no tenga sentido que se vean iguales en las marcas del cuerpo"
    I"Pudo haber sido el candelabro, la llave inglesa, la daga, la tubería, la soga o la pistola"
    I"Espero no tardarme más de una hora al investigar las cosas, después de todo solo poseo seis horas para determinar quien fue, con que y en donde..."
    jump menum
    "yuju"
    return

label menum:
    scene black
    scene recepcion die
    if ft==0:
        I"¿Por dónde debería empezar?"
        $ft=1
    else:
        if ft==1:
            reloj "Ding Dong Ding"
            I"Al parecer ya ha pasado una hora"
            I"¿Qué más debería de investigar?"
            $ft=2
        else:
            if ft==2:
                reloj "Ding Dong Ding"
                I"Al parecer ya han pasado dos horas"
                I"¿Qué más debería de investigar?"
                $ft=3
            else:
                if ft==3:
                    reloj "Ding Dong Ding"
                    I"Al parecer ya han pasado tres horas"
                    I"¿Qué más debería de investigar?"
                    $ft=4
                else:
                    if ft==4:
                        reloj "Ding Dong Ding"
                        I"Al parecer ya han pasado cuatro horas"
                        I"¿Qué más debería de investigar?"
                        $ft=5
                    else:
                        if ft==5:
                            reloj "Ding Dong Ding"
                            I"Al parecer ya han pasado cinco horas"
                            I"Debería apurarme ya solo me queda una hora"
                            I"¿Qué más debería de investigar?"
                            $ft=6
                        else:
                            if ft==6:
                                reloj "Ding Dong Ding"
                                I"Ya son las 2pm, si no descubro al asesino ¡se escapara!"
                                jump declaracion
                            else:
                                pass
    menu:
        "Armas":
            jump armas
        "Sospechosos":
            jump sospechosos
        "Habitaciones":
            jump habitaciones
    "H"
    return

label declaracion:
    scene recepcion die
    show silueta0 at center:
        xzoom 3 yzoom 3
    I"Debo decubrilo ya"
    I"¿Quién es el asesino?"
    menu:
        "Verdi":
            $ase=3
            $f1="Verdi"
        "Scarlata":
            $ase=5
            $f1="Scarlata"
        "Rosalinda":
            $ase=4
            $f1="Rosalinda"
        "Mostaza":
            $ase=2
            $f1="Mostaza"
        "Benjamín":
            $ase=6
            $f1="Benjamín"
        "Bianca":
            $ase=1
            $f1="Bianca"
    I"¿Cual es el arma utilizada?"
    menu:
        "Candelabro":
            $arm=3
            $f2="El candelabro"
        "Cuerda":
            $arm=2
            $f2="La cuerda"
        "Daga":
            $arm=6
            $f2="La daga"
        "Llave Inglesa":
            $arm=5
            $f2="La llave Inglesa"
        "Pistola":
            $arm=4
            $f2="La pistola"
        "Tubería":
            $arm=1
            $f2="La tubería"
    I"¿En dónde sucedió el asesinato?"
    menu:
        "Baño":
            $hab=1
            $f3="El baño"
        "Cocina":
            $hab=2
            $f3="La cocina"
        "Comedor":
            $hab=3
            $f3="El comedor"
        "Estudio":
            $hab=4
            $f3="El estudio"
        "Jardín":
            $hab=5
            $f3="El jardín"
        "Sala de estar":
            $hab=6
            $f3="La sala de estar"
    jump finales
    return
label finales:
    if killer==ase:
        "[f1] fue enviado a juicio, era un asesino que merecía estar en la cárcel"
        if weapon==arm:
            if room==hab:
                "Sabiendo que el arma homicida era [f2] y el lugar donde ocurrió el hecho era [f3] se pudieron encontrar pruebas suficientes para sentenciarlo como culpable de sus crímenes"
                #"Fin"#1
            else:
                "Se sabía cuál era el arma homicida, [f2], pero al tener información errada sobre el lugar de la muerte, no se pudo procesar el caso y [f1] salió libre"
        else:
            if room==hab:
                "Creyendo que el arma homicida era [f2] y el lugar donde ocurrió el hecho era [f3] hubo hechos contradictorios y [f1] salió libre"
            else:
                "Habiendo dicho que el arma homicida era [f2] y al mismo tiempo diciendo que [f3] era el lugar del asesinato, no se pudo procesar el caso, perdiste tu credibilidad y [f1] salió libre"

    else:
        "[f1] fue enviado injustamente a juicio, con la espera de la prisión"
        if weapon==arm:
            if room==hab:
                "Sabiendo que el arma homicida era [f2] y el lugar donde ocurrió el hecho era [f3] se pudieron encontrar pruebas suficientes para sentenciarle como culpable de un crimen que no cometió"
                "[f1] era una persona inocente que fue enviada a prisión por tu culpa, mientras que el verdadero asesino quedo libre"
                "Meses después se descubrió que [f1] era inocente, se absolvieron sus cargos y tu perdiste toda la credibilidad que tenías"
            else:
                "Se sabía cuál era el arma homicida, [f2], pero al tener información errada sobre el lugar de la muerte, no se pudo procesar el caso con tan pocas evidencias y [f1] salió libre, mientras que el verdadero asesino ni se inmuto"
        else:
            if room==hab:
                "Creyendo que el arma homicida era [f2] y el lugar donde ocurrió el hecho era [f3] hubo hechos contradictorios y [f1] salió libre, mientras que el verdadero asesino también estaba libre"
            else:
                "Habiendo dicho que el arma homicida era [f2] y al mismo tiempo diciendo que [f3] era el lugar del asesinato, no se pudo procesar el caso, perdiste tu credibilidad"
                "[f1] salió libre y te denuncio por perjurio, mientras que el verdadero asesino quedo libre"
    return
label armas:
    menu:
        "Candelabro":
            jump comedor
        "Cuerda":
            jump cocina
        "Daga":
            jump sala
        "Llave Inglesa":
            jump jardin
        "Pistola":
            jump estudio
        "Tuberia":
            jump bano
    return
label sospechosos:
    menu:
        "Verdi":
            jump comedor
        "Scarlata":
            jump jardin
        "Rosalinda":
            jump estudio
        "Mostaza":
            jump cocina
        "Benjamín":
            jump sala
        "Bianca":
            jump bano
    return
label habitaciones:
    menu:
        "Baño":
            jump bano
        "Cocina":
            jump cocina
        "Comedor":
            jump comedor
        "Estudio":
            jump estudio
        "Jardín":
            jump jardin
        "Sala de estar":
            jump sala
    return

label bano:
    scene baño #1
    $a=1
    I"Así que este es el baño..."
    I"Me pregunto si podre encontrar aquí alguna arma"
    if weapon == a:
        I"No he encontrado ningún arma por aquí"
    else:
        show tuberia at right:
            xzoom 0.5 yzoom 0.5
        I"Ohh, así que por aquí hay una tubería, se ve normal, a decir verdad"
        hide tuberia
    I"Debería de revisar por la habitación, a ver que encuentro"
    if room == a:
        I"Mmmm.... parece que alguien ha limpiado muy cuidadosamente la tina y su alrededores..."
    else:
        I"A parte de unas bonitas toallas y jabones caros no encuentro nada de interés por aquí"
    if killer == a:
        I"No encontré a nadie en el baño, iré a buscar a otro lugar"
        jump menum
    else:
        show nc blanca at left:
            xzoom 1.2 yzoom 1.2
        I "Oh, disculpa, ¿puedo hablar contigo un momento?"
        blanca "Claro, ¿que se le ofrece?"
        I "¿Me puede decir que hizo esta mañana a eso de las 6am?"
        blanca "Bueno, a esa hora ya estaba despierta y haciendo diversas cosas"
        I "¿diversas cosas?"
        blanca "limpiar, barrer, preparar agua caliente, el periódico de hoy.."
        blanca "De hecho aún tengo cosas por hacer\nSi me permite"
        hide nc blanca
        I"Parece bastante ocupada"
        I"Bueno, ¿qué sigue?"
        jump menum
    return
label cocina:
    scene cocin#2
    #"Arma es: [weapon]\nKiller es: [killer]\nHabitacion es: [room]"
    $a=2
    I"Así que esta es la cocina..."
    I"Me pregunto si podre encontrar aquí alguna arma"
    if weapon == a:
        I"No he encontrado ningún arma por aquí"
    else:
        show cuerda at right:
            xzoom 0.5 yzoom 0.5
        I"Ohh, así que por aquí hay una cuerda, de seguro la usan para atar...\nya sabes...\ncosas..."
        hide cuerda
    I"Debería de revisar por la habitación, a ver que encuentro"
    if room == a:
        I"Mmmm.... hay cosas que parecen que no van en su sitio"
        I"Al parecer también acaban de limpiar a fondo la estantería de abajo y el piso"
    else:
        I"A parte de un olor muy bueno a pan y todos los condimentos meticulosamente ordenados no encuentro nada de interés por aquí"
    if killer == a:
        I"Tal parece soy el único al que le atrae el aroma de la comida, debe ser porque no he desayunado"
        jump menum
    else:
        show nc mostaza at left:
            xzoom 1.3 yzoom 1.3
        I "Disculpe, si no es mucha molestia tengo unas preguntas para hacerle"
        mostaza "Hazlas."
        I "Donde estuvo anoche entre las 5-6am"
        mostaza "Estaba corriendo por los alrededores"
        I "¿En la madrugada?"
        mostaza "La madrugada es el mejor momento para salir a correr un poco "
        mostaza "Si eso es todo"
        hide nc mostaza
        I"..."
        I"Bueno, ¿qué sigue?"
        jump menum
    return
label comedor:
    scene comedor#3
    $a=3
    I"Es un buen comedor"
    I"Me pregunto si podre encontrar aquí el candelabro"
    if weapon == a:
        I"Lastimosamente, no he encontrado ningún arma por aquí"
    else:
        show candelabro at right:
            xzoom 0.5 yzoom 0.5
        I"¡Eureka!, he encontrado el candelabro"
        hide candelabro
    I"Debería de revisar por la habitación, a ver que encuentro"
    if room == a:
        I"Mmmm.... algo parece fuera de lugar"
        I"Al parecer han cambiado recientemente la alfombra..."
    else:
        I"Me gusta el color rojo de las sillas, si tan solo encontrar pistas fuera tan fácil... "
    if killer == a:
        I"Al parecer nadie más está interesado en pasar tiempo en el comedor cuando no hay comida que comer"
        jump menum
    else:
        show nc verde at left:
            xzoom 1.2 yzoom 1.2
        I "Buen día, tengo unas preguntas que me gustaría que respondiera"
        verdi "Y yo tengo ganas de salir ya de aquí, hace nada que murió alguien"
        I "No se preocupe, en cuanto antes responda antes nos iremos de aquí"
        verdi "Bien. Pregunta"
        I "¿Me puede decir que hacia entre las 5-6 de la mañana?"
        verdi "¡¡CINCO DE LA MAÑANA!!, ¡pues que crees que hago chico!"
        verdi "Obviamente estaba más que metido en mis sabanas a estas horas, duermo tan profundo que si no fuera porque Miss Bianca me despertó, no me hubiera enterado de que aquí hubo un asesinato hasta las 12"
        verdi "¡SI!, ¡Hasta las 12!"
        hide nc verde
        I"Vaya, creo que dije algo que no debía, se fue hecho una furia"
        I"Bueno, ¿qué sigue?"
        jump menum
    return
label estudio:
    scene estudio#4
    $a=4
    I"Algún día me gustaría tener un estudio tan bonito..."
    I"Bueno a buscar un arma por aquí"
    if weapon == a:
        I"O mis dotes para detectar armas se han ido o no hay un arma por aquí"
    else:
        show pistola at right:
            xzoom 0.5 yzoom 0.5
        I"Vaya, esto puede llegar a ser peligroso, dejar una pistola así en un cajón sin llave..."
        I"¡Dios!, cualquiera podría tomarla"
        hide pistola
    I"Debería de revisar por la habitación, a ver que encuentro"
    if room == a:
        I"Mmmm.... puede que sea muy paranoico pero me pregunto si alguien reordeno los libros a toda prisa recientemente"
        I"Ver juntos libros como 'Memorias de un amigo imaginario', 'IT' y 'El moderno Repertorio de Kent' me extraña bastante"
        I"...\n eso y la mancha de orígenes desconocidos bajo la alfombra me hacen dudar sobre lo que paso aquí"
    else:
        I"Me gustan los libros que tiene, 'El nombre del viento' es buenísimo, a ver cuando sale la tercera parte"
    if killer == a:
        I"El característico olor de los libros solo atrae a los aventureros, valientes, predestinados... \n Es exactamente por eso que soy el único aquí"
        jump menum
    else:
        show nc morado at left
        I "Hola, ¿podría hacerle unas preguntas?"
        rosa "Ya estás haciendo una, pero te permitiré otra más"
        I "¿Dónde estuvo durante las primeras horas del día?, por las 5-6am"
        rosa "Bueno, estuve en mi habitación toda la noche"
        I "¿Puede usted comprobarlo?"
        rosa "No"
        rosa "Si me permite"
        hide nc morado
        I"Fue un poco ruda, pero creo que lo seria cualquiera en esta situación..."
        I"Bueno, ¿qué sigue?"
        jump menum
    return
label jardin:
    scene jardinn#5
    $a=5
    I"WOW, sí que es fresco el aire en el jardín"
    I"Me pregunto si encontrare algún tipo de arma por aquí"
    if weapon == a:
        I"El jardín es muy grande pero no creo que lo sea tanto como para no encontrar un arma cuando me lo propongo"
    else:
        show llaveinglesa at right:
            xzoom 0.5 yzoom 0.5
        I"¡La encontré!, una llave inglesa, eh, bueno parece normal, solo 'ligeramente' oxidada"
        hide llaveinglesa
    I"¿Habrá sucedido algo en el jardín?"
    if room == a:
        I"Mmmm.... vi unas ramitas rotas por aquí y por allá, estaban bien escondidas"
    else:
        I"Es un bonito jardín, muy... verde"
    if killer == a:
        I"Me pregunto si soy el único al que le gusta un poco de brisa fresca en mi cara"
        jump menum
    else:
        show nc scarlata at left:
            xzoom 1.2 yzoom 1.2
        I "Hace buen clima, ¿no?"
        scarlata "¿El detective?, ¿que se le ofrece de mí?"
        I "Una pregunta,¿Dónde estuvo durante las primeras horas del día?, por las 5-6am"
        scarlata "Bueno, estuve escribiendo cartas toda la noche, justo fui a enviarlas por esa hora, puedo darle los nombres de los remitentes"
        I "Se lo agradecería mucho"
        scarlata "Bien."
        hide nc scarlata
        I"Me dio los nombre y salió de allí"
        I"Bueno, ¿qué sigue?"
        jump menum
    return
label sala:
    scene sala de juegos#6
    $a=6
    I"Vaya centro de mesa más bonito, me pregunto cada cuando lo cambian"
    I"Y si hay un arma cerca"
    if weapon == a:
        I"Al parecer solo eran las flores, no hay armas en la habitación"
    else:
        show daga at right:
            xzoom 0.5 yzoom 0.5
        I"¡Auch!,¡Esta sí que es una daga afilada!"
        hide daga
    I"Si busco lo suficiente me pregunto si encontrare algún tipo de rastro por aquí"
    if room == a:
        I"Mmmm.... hay un buen pedazo de alfombra que se siente húmeda, como si hubiera sido restregada últimamente"
    else:
        I"Al parecer no, pero ¡oye!, ese calentador está muy cool"
    if killer == a:
        I"No es un lugar muy ruidoso, supongo que lo sería más si hubiera otra persona aparte de mi aquí"
        jump menum
    else:
        show nc black at left:
            xzoom 1.2 yzoom 1.2
        I "Buenos días, ¿me permite hacerle unas preguntas?"
        negro "Hm, adelante"
        I "¿Que estaba haciendo a las 5-6am del día de hoy?"
        negro "Hoy... estuve escribiendo mi novela 'Poema de poetas' desde que me desperté"
        I "Y ¿desde qué hora es eso?"
        negro "No lo sé, probablemente 4am o algo anterior, últimamente no he estado durmiendo bien"
        I"¿Tiene alguna prueba?"
        negro"Solo mi manuscrito"
        hide nc black
        I"Bueno, ¿qué sigue?"
        jump menum
    return
