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

    "En una mansion como cualquier otra, el dueño celebraba una reunion..."
    "En ella estan presentes..."
    show nc morado at left:
    "Mrs. Rosalinda"
    show nc scarlata at left:
        xzoom 1.2 yzoom 1.2
    "Mrs. Scarlata"
    show nc black at left:
        xzoom 1.2 yzoom 1.2
    "Mr. Benjamin"
    show nc mostaza at left:
        xzoom 1.3 yzoom 1.3
    "Coronel Mostaza"
    show nc verde at left:
        xzoom 1.2 yzoom 1.2
    "Sr. Verdi"
    show nc blanca at left:
        xzoom 1.2 yzoom 1.2
    "Y como olvidarnos de la doncella Miss. Bianca..."
    hide nc blanca
    "Pero algo sucedio durante la noche..."
    "¡¡Un asesinato!!"
    jump asesinato
    return

label asesinato:
    scene recepcion die
    "El anfitrion fue encontrado muerto en la recepcion..."
    "Y te han llamado para averiguar que paso"
    "Tienes 6 horas antes de que los invitados a la reunion se vayan"
    "Asi que antes de que se te agote el tiempo averigua..."
    "¿Quien fue?\n¿Con que lo hizo?\n¿Donde lo hizo?"
    jump introduceyourself
    return

label introduceyourself:
    scene mansion hd
    I"Por fin he llegado, asi que esta es la mansion donde ha ocurrido el asesinato"
    I"Me parece una bonita mansion"
    I"Repasemos lo que sabemos:\n  Hay un asesino entre los seis sospechosos\n  Es una mansion grande pero los unicos cuartos abiertos son los del ala oeste,"
    I"Entre ellos tenemos: La sala, el baño, la cocina, el comedor, el estudio y el jardin"
    I"Tambien tengo mis propias sospechas cual pudo haber sido el arma asesina"
    "//Aunque no tenga sentido que se vean iguales en las marcas del cuerpo"
    I"Pudo haber sido el candelabro, la llave inglesa, la daga, la tuberia, la soga o la pistola"
    I"Espero no tardarme mas de una hora al investigar las cosas, despues de todo solo poseeo seis horas para determinar quien fue, con que y en donde..."
    jump menum
    "yuju"
    return

label menum:
    scene black
    scene recepcion die
    if ft==0:
        I"¿Por donde deberia empezar?"
        $ft=1
    else:
        if ft==1:
            reloj "Ding Dong Ding"
            I"Al parecer ya ha pasado una hora"
            I"¿Que mas deberia de investigar?"
            $ft=2
        else:
            if ft==2:
                reloj "Ding Dong Ding"
                I"Al parecer ya han pasado dos horas"
                I"¿Que mas deberia de investigar?"
                $ft=3
            else:
                if ft==3:
                    reloj "Ding Dong Ding"
                    I"Al parecer ya han pasado tres horas"
                    I"¿Que mas deberia de investigar?"
                    $ft=4
                else:
                    if ft==4:
                        reloj "Ding Dong Ding"
                        I"Al parecer ya han pasado cuatro horas"
                        I"¿Que mas deberia de investigar?"
                        $ft=5
                    else:
                        if ft==5:
                            reloj "Ding Dong Ding"
                            I"Al parecer ya han pasado cinco horas"
                            I"Deberia apurarme ya solo me queda una hora"
                            I"¿Que mas deberia de investigar?"
                            $ft=6
                        else:
                            if ft==6:
                                reloj "Ding Dong Ding"
                                I"Ya son las 2pm, si no escojo al asesino ¡se escapara!"
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
    I"Debo decidir ya"
    I"¿Quien es el asesino?"
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
        "Benjamin":
            $ase=6
            $f1="Benjamin"
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
        "Tuberia":
            $arm=1
            $f2="La tuberia"
    I"¿En donde sucedio el asesinato?"
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
        "Jardin":
            $hab=5
            $f3="El jardin"
        "Sala de estar":
            $hab=6
            $f3="La sala de estar"
    jump finales
    return
label finales:
    if killer==ase:
        "[f1] fue enviado a juicio, era un asesino que merecia estar en la carcel"
        if weapon==arm:
            if room==hab:
                "Sabiendo que el arma homicida era [f2] y el lugar donde ocurrio el hecho era [f3] se pudieron encontrar pruebas suficientes para sentenciarlo como culpable de sus crimenes"
            else:
                "Se sabia cual era el arma homicida, [f2], pero al tener informacion errada sobre el lugar de la muerte, no se pudo procesar el caso y [f1] salio libre"
        else:
            if room==hab:
                "Creyendo que el arma homicida era [f2] y el lugar donde ocurrio el hecho era [f3] hubo hechos contradictorios y [f1] salio libre"
            else:
                "Habiendo dicho que el arma homicida era [f2] y al mismo tiempo diciendo que [f3] era el lugar del asesinato, no se pudo procesar el caso, perdiste tu credibilidad y [f1] salio libre"

    else:
        "[f1] fue enviado injustamente a juicio, con la espera de la prision"
        if weapon==arm:
            if room==hab:
                "Sabiendo que el arma homicida era [f2] y el lugar donde ocurrio el hecho era [f3] se pudieron encontrar pruebas suficientes para sentenciarle como culpable de un crimen que no cometio"
                "[f1] era una persona inocente que fue enviada a prision por tu culpa, mientras que el verdadero asesino quedo libre"
                "Meses despues se descubrio que [f1] era inocente, se absolvieron sus cargos y tu perdiste toda la credibilidad que tenias"
            else:
                "Se sabia cual era el arma homicida, [f2], pero al tener informacion errada sobre el lugar de la muerte, no se pudo procesar el caso con tan pocas evidencias y [f1] salio libre, mientras que el verdadero asesino ni se inmuto"
        else:
            if room==hab:
                "Creyendo que el arma homicida era [f2] y el lugar donde ocurrio el hecho era [f3] hubo hechos contradictorios y [f1] salio libre, mientras que el verdadero asesino tambien estaba libre"
            else:
                "Habiendo dicho que el arma homicida era [f2] y al mismo tiempo diciendo que [f3] era el lugar del asesinato, no se pudo procesar el caso, perdiste tu credibilidad y [f1] salio libre y te denuncio por perjurio, mientras que el verdadero asesino quedo libre"
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
        "Benjamin":
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
        "Jardin":
            jump jardin
        "Sala de estar":
            jump sala
    return

label bano:
    scene baño #1
    $a=1
    I"Asi que este es el baño..."
    I"Me pregunto si podre encontrar aqui alguna arma"
    if weapon == a:
        I"No he encontrado ningun arma por aqui"
    else:
        show tuberia at right:
            xzoom 0.5 yzoom 0.5
        I"Ohh, asi que por aqui hay una tuberia, se ve normal, a decir verdad"
        hide tuberia
    I"Deberia de revisar por la habitacion, a ver que encuentro"
    if room == a:
        I"Mmmm.... parece que alguien ha limpiado muy cuidadosamente la tina y su alrededores..."
    else:
        I"A parte de unas bonitas toallas y jabones caros no encuentro nada de interes por aqui"
    if killer == a:
        I"No encontre a nadie en el baño, ire a buscar a otro lugar"
        jump menum
    else:
        show nc blanca at left:
            xzoom 1.2 yzoom 1.2
        I "Oh, disculpa, ¿puedo hablar contigo un momento?"
        blanca "Claro, ¿que se le ofrece?"
        I "¿Me puede decir que hizo esta mañana a eso de las 6am?"
        blanca "Bueno, a esa hora ya estaba despierta y haciendo diversas cosas"
        I "¿diversas cosas?"
        blanca "limpiar, barrer, preparar agua caliente, el periodico de hoy.."
        blanca "De hecho aun tengo cosas por hacer\nSi me permite"
        hide nc blanca
        I"Parece bastante ocupada"
        I"Bueno, ¿que sigue?"
        jump menum
    return
label cocina:
    scene cocin#2
    #"Arma es: [weapon]\nKiller es: [killer]\nHabitacion es: [room]"
    $a=2
    I"Asi que esta es la cocina..."
    I"Me pregunto si podre encontrar aqui alguna arma"
    if weapon == a:
        I"No he encontrado ningun arma por aqui"
    else:
        show cuerda at right:
            xzoom 0.5 yzoom 0.5
        I"Ohh, asi que por aqui hay una cuerda, de seguro la usan para atar...\natar...\ncosas..."
        hide cuerda
    I"Deberia de revisar por la habitacion, a ver que encuentro"
    if room == a:
        I"Mmmm.... hay cosas que parecen que no van en su sitio"
        I"Al parecer tambien acaban de limpiar a fondo la estanteria de abajo y el piso"
    else:
        I"A parte de un olor muy bueno a pan y todos los condimentos meticulosamente ordenados no encuentro nada de interes por aqui"
    if killer == a:
        I"Tal parece soy el unico al que le atrae el aroma de la comida, debe ser porque no he desayunado"
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
        I"Bueno, ¿que sigue?"
        jump menum
    return
label comedor:
    scene comedor#3
    $a=3
    I"Es un buen comedor"
    I"Me pregunto si podre encontrar aqui el candelabro"
    if weapon == a:
        I"Lastimosamente, no he encontrado ningun arma por aqui"
    else:
        show candelabro at right:
            xzoom 0.5 yzoom 0.5
        I"¡Eureka!, he encontrado el candelabro"
        hide candelabro
    I"Deberia de revisar por la habitacion, a ver que encuentro"
    if room == a:
        I"Mmmm.... algo parece fuera de lugar"
        I"Al parecer han cambiado recientemente la alfombra "
    else:
        I"Me gusta el color rojo de las sillas, si tan solo encontrar pistas fuera tan facil... "
    if killer == a:
        I"Al parecer nadie mas esta interesado en pasar tiempo en el comedor cuando no hay comida que comer"
        jump menum
    else:
        show nc verde at left:
            xzoom 1.2 yzoom 1.2
        I "Buen dia, tengo unas preguntas que me gustaria qu respondiera"
        verdi "Y yo tengo ganas de salir ya de aqui, casi que acaba de morir alguien"
        I "No se preocupe, en cuanto antes responda antes nos iremos de aqui"
        verdi "Bien. Pregunta"
        I "¿Me puede decir que hacia entre las 5-6 de la mañana?"
        verdi "¡¡CINCO DE LA MAÑANA!!, ¡pues que crees que hago chico!"
        verdi "Obiamente estaba mas que metido en mis sabanas a estas horas, duermo tan profundo que si no fuera porque Miss Bianca me desperto, no me hubiera enterado de que aqui hubo un asesinato hasta las 12"
        verdi "¡SI!, ¡Hasta las 12!"
        hide nc verde
        I"Vaya, creo que pise una mina, se fue hecho una furia"
        I"Bueno, ¿que sigue?"
        jump menum
    return
label estudio:
    scene estudio#4
    $a=4
    I"Algun dia me gustaria tener un estudio tan bonito..."
    I"Bueno a buscar un arma por aqui"
    if weapon == a:
        I"O mis dotes para detectar armas se han ido o no hay un arma por aqui"
    else:
        show pistola at right:
            xzoom 0.5 yzoom 0.5
        I"Vaya, esto puede llegar a ser peligroso, dejar una pistola asi en un cajon sin llave..."
        I"¡Dios!, cualquiera podria tomarla"
        hide pistola
    I"Deberia de revisar por la habitacion, a ver que encuentro"
    if room == a:
        I"Mmmm.... puede que sea muy paranoico pero me pregunto si alguien reordeno los libros a toda prisa recientemente"
        I"Ver juntos libros como 'Memorias de un amigo imaginario', 'IT' y 'El moderno Repertorio de Kent' me extraña bastante"
        I"...\n eso y la mancha de origenes desconocidos bajo la alfombra me hacen dudar sobre lo que paso aqui"
    else:
        I"Me gustan los libros que tiene, 'El nombre del viento' es buenisimo, a ver cuando sale la tercera parte"
    if killer == a:
        I"El caracteristico olor de los libros solo atrae a los aventureros, valientes, predestinados... \n Es exactamente por eso que soy el unico aqui"
        jump menum
    else:
        show nc morado at left
        I "Hola, ¿podria hacerle unas preguntas?"
        rosa "Ya estas haciendo una, pero te permitire otra mas"
        I "¿Donde estuvo durante las primeras horas del dia?, por las 5-6am"
        rosa "Bueno, estuve en mi habitacion toda la noche"
        I "¿Puede usted comprobarlo?"
        rosa "No"
        rosa "Si me permite"
        hide nc morado
        I"Un poco ruda, pero creo que lo seria cualquiera en esta situacion..."
        I"Bueno, ¿que sigue?"
        jump menum
    return
label jardin:
    scene jardinn#5
    $a=5
    I"WOW, si que es freco el aire en el jardin"
    I"Me pregunto si encontrare algun tipo de arma por aqui"
    if weapon == a:
        I"El jardin es muy grande pero no creo que lo sea tanto como para no encontrar un arma cuando me lo propongo"
    else:
        show llaveinglesa at right:
            xzoom 0.5 yzoom 0.5
        I"¡La encontre!, una llave inglesa, eh, bueno parece normal, solo 'ligeramente' oxidada"
        hide llaveinglesa
    I"¿Habra sucedido algo en el jardin?"
    if room == a:
        I"Mmmm.... vi unas ramitas rotas por aqui y por alla, estaban bien escondidas"
    else:
        I"Es un bonito jardin, muy... verde"
    if killer == a:
        I"Me pregunto si soy el unico al que le gusta un poco de brisa fresca en mi cara"
        jump menum
    else:
        show nc scarlata at left:
            xzoom 1.2 yzoom 1.2
        I "Hace buen clima, ¿no?"
        scarlata "¿El detective?, ¿que se le ofrece de mi?"
        I "Una pregunta,¿Donde estuvo durante las primeras horas del dia?, por las 5-6am"
        scarlata "Bueno, estuve escribiendo cartas toda la noche, justo fui a enviarlas por esa hora, puedo darle los nombres de los remitentes"
        I "Se lo agradeceria mucho"
        scarlata "Bien."
        hide nc scarlata
        I"Me dio los nombre y salio de alli"
        I"Bueno, ¿que sigue?"
        jump menum
    return
label sala:
    scene sala de juegos#6
    $a=6
    I"Vaya centro de mesa mas bonito, me pregunto cada cuando lo cambian"
    I"Y si hay un arma cerca"
    if weapon == a:
        I"Al parecer solo eran las flores, no hay armas en la habitacion"
    else:
        show daga at right:
            xzoom 0.5 yzoom 0.5
        I"¡Auch!,¡Esta si que es una daga afilada!"
        hide daga
    I"Si busco lo suficiente me pregunto si encontrare algun tipo de rastro por aqui"
    if room == a:
        I"Mmmm.... hay un buen pedazo de alfombra que se siente humeda, como si hubiera sido restregada ultimamente"
    else:
        I"Al parecer no, pero ¡oye!, ese calentador esta muy cool"
    if killer == a:
        I"No es un lugar muy ruidoso, supongo que lo seria mas si hubiera otra persona aparte de mi aqui"
        jump menum
    else:
        show nc black at left:
            xzoom 1.2 yzoom 1.2
        I "Buenos dias, ¿me permite hacerle unas preguntas?"
        negro "Hm, adelante"
        I "¿Que estaba haciendo a las 5-6am del dia de hoy?"
        negro "Hoy... estuve escribiendo mi novela 'Poema de poetas' desde que me desperte"
        I "Y ¿desde que hora es eso?"
        negro "No lo se, probablemente 4am o algo anterior, ultimamente no he estado durmiendo bien"
        I"¿Tiene alguna prueba?"
        negro"Solo mi manoscrito"
        hide nc black
        I"Bueno, ¿que sigue?"
        jump menum
    return
