def DeseaJugar():
	#Crear Ventana
	ancho,largo=800,600
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")


	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	MARRON=(128,64,0)
	
	TITULO=pygame.image.load("IMAGENES/TITULO.png")
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	JUGAR=pygame.image.load("IMAGENES/JUGAR.png")
	SALIR=pygame.image.load("IMAGENES/SALIR.png")


	
	VENTANA.blit(FONDO,(0,0))

	VENTANA.blit(TITULO,(120,10))
	JUGAR_V=VENTANA.blit(JUGAR,(280,250))
	SALIR_V=VENTANA.blit(SALIR,(290,350))
	jugar=False
	
	while not(jugar):
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos
				
				if JUGAR_V.collidepoint(x,y):
					jugar=True

				elif SALIR_V.collidepoint(x,y):
					pygame.quit() 
					sys.exit()
		
		pygame.display.update()

	return jugar


def inicializarTablero():
	tablero=[[0 for x in range(0,8)] for y in range(0,8)]
	tablero[3][3]=2
	tablero[4][4]=2
	tablero[3][4]=1
	tablero[4][3]=1

	return tablero


def Jugadores():
	#Crear Ventana
	ancho,largo=800,600
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")


	#Colores
	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	
	TITULO=pygame.image.load("IMAGENES/TITULO.png")
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)


	
	jugadores=["",""]
	casilla_jug0=False
	casilla_jug1=False
	IntroducidoNombre0=False
	IntroducidoNombre1=False
	

	jugador1_V=fuente.render("JUGADOR 1:",0,BLANCO)#TEXTO DE CASILLA1
	jugador2_V=fuente.render("JUGADOR 2:",0,BLANCO)#TEXTO DE CASILLA2

	PosX,PosY=280,250
	ancho,largo=250,100

	casilla_jug0_inactive=pygame.draw.rect(VENTANA,GRIS,(PosX,PosY,ancho,largo),5)#CASILLA INACTIVA JUG1
	casilla_jug1_inactive=pygame.draw.rect(VENTANA,GRIS,(PosX,PosY+105,ancho,largo),5)#CASILLA INACTIVA JUG2
	

	while not(IntroducidoNombre0 and IntroducidoNombre1):

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos
				
				if casilla_jug0_inactive.collidepoint(x,y):
					casilla_jug0=True
					casilla_jug1=False
				
				elif casilla_jug1_inactive.collidepoint(x,y):
					
					casilla_jug1=True
					casilla_jug0=False
				
				else:
					casilla_jug0=False
					casilla_jug1=False

			elif event.type==pygame.KEYDOWN:
				if casilla_jug0 and not(IntroducidoNombre0):
					if event.key == pygame.K_BACKSPACE:
						jugadores[0] = jugadores[0][:-1]
					
					elif event.key==pygame.K_RETURN:
						if len(jugadores[0])>0:
							casilla_jug0=False
							IntroducidoNombre0=True
							casilla_jug1=True
							
					else:
						jugadores[0]+=event.unicode
				
				elif casilla_jug1 and not(IntroducidoNombre1):
					if event.key == pygame.K_BACKSPACE:
						jugadores[1] = jugadores[1][:-1]
					elif event.key==pygame.K_RETURN:
						if len(jugadores[1])>0:
							casilla_jug1=False
							IntroducidoNombre1=True

					else:
						jugadores[1]+=event.unicode

				
		VENTANA.blit(FONDO,(0,0))
		VENTANA.blit(TITULO,(120,10))
	
	
		VENTANA.blit(jugador1_V,(PosX+10,PosY+10))
		VENTANA.blit(jugador2_V,(PosX+10,PosY+115))

		
		VENTANA.blit((fuente.render(jugadores[0],0,VERDE)),(PosX+10,PosY+50))
		VENTANA.blit((fuente.render(jugadores[1],0,VERDE)),(PosX+10,PosY+165))
		


		if casilla_jug0:
			pygame.draw.rect(VENTANA,BLANCO,(PosX,PosY,ancho,largo),5)

		else:
			pygame.draw.rect(VENTANA,GRIS,(PosX,PosY,ancho,largo),5)

		
		if casilla_jug1:
			pygame.draw.rect(VENTANA,BLANCO,(PosX,PosY+105,ancho,largo),5)
			
		
		else:
			
			pygame.draw.rect(VENTANA,GRIS,(PosX,PosY+105,ancho,largo),5)


		if IntroducidoNombre0:
			pygame.draw.rect(VENTANA,VERDE,(PosX,PosY,ancho,largo),5)

		elif IntroducidoNombre1:
			pygame.draw.rect(VENTANA,VERDE,(PosX,PosY+105,ancho,largo),5)
		
		pygame.display.update()


	return jugadores


def CambiarTurno(turno:int):

	
	if turno==1:
		turno+=1	

	elif turno==2:
		turno-=1

	return turno



def QuedanFichas(tablero:[[int]]):

	
	negras=0
	blancas=0
	for i in range(0,8):
		for j in range(0,8):
			if tablero[i][j]==1:
				negras += 1
			elif tablero[i][j]==2:
				blancas+=1

	total=64-(negras+blancas)
	
	return total,negras,blancas


def TraducirJugada(x:str,y:str):
		
	letras='abcdefgh'

	y=y.lower()

	assert( any(y==letras[i] for i in range(0,8)) )
	
	x=int(x)

	assert(0<x<=8)
	
	x-=1

	
	for i in range(0,8):
		if y==letras[i]:
			y=i	

	assert (0<=x<8 and 0<=y<8)
	

	return x,y

def RealizarJugada(turno:int,A:[[int]],x:int,y:int):
	A[x][y]=turno


def TableroYPuntuacion(A:[[int]],jugadores:[str],FichasNegras:int,FichasBlancas:int,Validez:bool):

	ancho,largo=800,600
	
	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	PUNTUACION=pygame.image.load("IMAGENES/PUNTUACION.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")
	
	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)
	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	

	#Crear letras
	letras=[
	fuente.render("A",0,GRIS),  # 1:Bool, Alisado de las letras
	fuente.render("B",0,GRIS),
	fuente.render("C",0,GRIS),
	fuente.render("D",0,GRIS),
	fuente.render("E",0,GRIS),
	fuente.render("F",0,GRIS),
	fuente.render("G",0,GRIS),
	fuente.render("H",0,GRIS)
	]	
	#Texto jugada no valida

	VALIDEZ=fuente.render("Jugada Invalida",1,VERDE)
	
	#Pintar fondo de ventana
	VENTANA.blit(FONDO,(0,0))
	siguiente=False
	
	while not(siguiente):

		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type==MOUSEBUTTONDOWN:
				x,y=event.pos
				if SIGUIENTE_V.collidepoint(x,y):
					siguiente=True
	

		#Insertar imagenes del tablero (Casillas, fichas)
		TableroPosy=60

		for x in range(0,8):
			
			TableroPosx=60
			
			for y in range(0,8):
				
				if A[x][y]==0:

					VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
					
				
				elif A[x][y]==1:
					VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
					

				elif A[x][y]==2:
					VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))
					
				
				TableroPosx+=60	
			
			TableroPosy+=60

		#Instertar Numeros, y texto al tablero

		PosLetrasNumeros=80
		for i in range(0,8):

			VENTANA.blit(fuente.render(str(i+1),0,GRIS),(35,PosLetrasNumeros))
			VENTANA.blit(fuente.render(str(i+1),0,GRIS),(545,PosLetrasNumeros))		

			VENTANA.blit(letras[i],(PosLetrasNumeros,30))
			VENTANA.blit(letras[i],(PosLetrasNumeros,540))
			PosLetrasNumeros+=60

		#Tablero de puntuacion
		pygame.draw.rect(VENTANA,GRIS,(590,120,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,160,200,90),4)
		VENTANA.blit(PUNTUACION,(600,115))
		VENTANA.blit(fuente.render(str(jugadores[0])+": "+str(FichasNegras),0,VERDE),(600,170))
		VENTANA.blit(fuente.render(str(jugadores[1])+": "+str(FichasBlancas),0,VERDE),(600,210))

		SIGUIENTE_V=VENTANA.blit(SIGUIENTE,(580,400))

		#Error
		if not(Validez):
			VENTANA.blit(VALIDEZ,(580,350))




		pygame.display.update()



def ObtenerJugada1(A:[[int]],jugadores:[str],turno:int):

	pygame.init()
	
	ancho,largo=800,600
	

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	casillaValida=pygame.image.load("IMAGENES/jugadaValida.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	TURNO=pygame.image.load("IMAGENES/TURNO.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")


	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	

	#Crear letras
	letras=[
	fuente.render("A",0,GRIS),  # 1:Bool, Alisado de las letras
	fuente.render("B",0,GRIS),
	fuente.render("C",0,GRIS),
	fuente.render("D",0,GRIS),
	fuente.render("E",0,GRIS),
	fuente.render("F",0,GRIS),
	fuente.render("G",0,GRIS),
	fuente.render("H",0,GRIS)
	]	
	#Pintar fondo de ventana
	VENTANA.blit(FONDO,(0,0))
	jugada=["",""]
	FILA=fuente.render("FILA ",0,GRIS)
	COLUMNA=fuente.render("Columna",0,GRIS)

	
	while jugada[0]=="" or jugada[1]=="":
		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			
			elif event.type==pygame.KEYDOWN:
				if  jugada[0]=="":
					
					if event.key == pygame.K_BACKSPACE:
						pass
					
					elif event.key==pygame.K_RETURN:
						pass
						
					else:
						jugada[0]+=event.unicode

				else:
					if event.key == pygame.K_BACKSPACE:
						
						pass
					elif event.key==pygame.K_RETURN:
						pass
						
					else:
						jugada[1]+=event.unicode

		#Insertar imagenes del tablero (Casillas, fichas)
		TableroPosy=60

		for x in range(0,8):
			
			TableroPosx=60
			
			for y in range(0,8):
				
				if A[x][y]==0:

					VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
					
				
				elif A[x][y]==1:
					VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
					

				elif A[x][y]==2:
					VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))

				elif A[x][y]==3:
					VENTANA.blit(casillaValida,(TableroPosx,TableroPosy))
					
				
				TableroPosx+=60	
			
			TableroPosy+=60

		#Instertar Numeros, y texto al tablero

		PosLetrasNumeros=80
		for i in range(0,8):

			VENTANA.blit(fuente.render(str(i+1),0,GRIS),(35,PosLetrasNumeros))
			VENTANA.blit(fuente.render(str(i+1),0,GRIS),(545,PosLetrasNumeros))		

			VENTANA.blit(letras[i],(PosLetrasNumeros,30))
			VENTANA.blit(letras[i],(PosLetrasNumeros,540))
			PosLetrasNumeros+=60

		#Tablero de Turno
		
		#Casilla turno
		pygame.draw.rect(VENTANA,GRIS,(590,120,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,160,200,90),4)
		VENTANA.blit(TURNO,(630,115))


		#Casilla Fila 
		FILA_V=pygame.draw.rect(VENTANA,GRIS,(590,300,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,300,150,40),4)
		VENTANA.blit(FILA,(600,310))
		VENTANA.blit(fuente.render(jugada[0],0,VERDE),(760,310))
		
		#Casilla columna
		COLUMNA_V=pygame.draw.rect(VENTANA,GRIS,(590,340,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,340,150,40),4)
		VENTANA.blit(COLUMNA,(600,350))
		VENTANA.blit(fuente.render(jugada[1],0,VERDE),(760,350))

		if turno==1:
			VENTANA.blit(fuente.render(str(jugadores[0]),0,VERDE),(600,180))
			VENTANA.blit(pygame.transform.scale(fichaNegra, (40, 40)),(740,170))
		else:
			VENTANA.blit(fuente.render(str(jugadores[1]),1,VERDE),(600,180))
			VENTANA.blit(pygame.transform.scale(fichaBlanca, (40, 40)),(740,170))

		pygame.display.update()

	time.sleep(0.2)

	return jugada[0],jugada[1]

def ObtenerJugada2(A:[[int]],jugadores:[str],turno:int):
	
	#Inicializar arreglo para almacenar casillas
	TABLERO_POS=[[0 for x in range(0,8)] for y in range(0,8)]
	ancho,largo=800,600
	

	#Crear Ventana
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")

	#Fuente
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)

	#Cargar Imagenes
	casillaVacia=pygame.image.load("IMAGENES/casillas.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")
	casillaValida=pygame.image.load("IMAGENES/jugadaValida.png")	
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	TURNO=pygame.image.load("IMAGENES/TURNO.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")

	#Colores
	GRIS=(130,130,130)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	

	#Crear letras
	letras=[
	fuente.render("A",0,GRIS),  # 1:Bool, Alisado de las letras
	fuente.render("B",0,GRIS),
	fuente.render("C",0,GRIS),
	fuente.render("D",0,GRIS),
	fuente.render("E",0,GRIS),
	fuente.render("F",0,GRIS),
	fuente.render("G",0,GRIS),
	fuente.render("H",0,GRIS)
	]	
	#Pintar fondo de ventana
	VENTANA.blit(FONDO,(0,0))
	jugada=False
	
	while not(jugada):

		#Insertar imagenes del tablero (Casillas, fichas)
		TableroPosy=60

		for x in range(0,8):
			
			TableroPosx=60
			
			for y in range(0,8):
				
				if A[x][y]==0:

					TABLERO_POS[x][y]=VENTANA.blit(casillaVacia,(TableroPosx,TableroPosy))
					
				
				elif A[x][y]==1:
					TABLERO_POS[x][y]=VENTANA.blit(fichaNegra,(TableroPosx,TableroPosy))
					

				elif A[x][y]==2:
					TABLERO_POS[x][y]=VENTANA.blit(fichaBlanca,(TableroPosx,TableroPosy))

				elif A[x][y]==3:
					TABLERO_POS[x][y]=VENTANA.blit(casillaValida,(TableroPosx,TableroPosy))
					
				
				TableroPosx+=60	
			
			TableroPosy+=60

		#Instertar Numeros, y texto al tablero

		PosLetrasNumeros=80
		for i in range(0,8):

			VENTANA.blit(fuente.render(str(i+1),0,GRIS),(35,PosLetrasNumeros))
			VENTANA.blit(fuente.render(str(i+1),0,GRIS),(545,PosLetrasNumeros))		

			VENTANA.blit(letras[i],(PosLetrasNumeros,30))
			VENTANA.blit(letras[i],(PosLetrasNumeros,540))
			PosLetrasNumeros+=60

		#Tablero de puntuacion
		pygame.draw.rect(VENTANA,GRIS,(590,120,200,40),4)
		pygame.draw.rect(VENTANA,GRIS,(590,160,200,90),4)
		VENTANA.blit(TURNO,(630,115))
		
		if turno==1:
			VENTANA.blit(fuente.render(str(jugadores[0]),0,VERDE),(600,180))
			VENTANA.blit(pygame.transform.scale(fichaNegra, (40, 40)),(740,170))
		else:
			VENTANA.blit(fuente.render(str(jugadores[1]),1,VERDE),(600,180))
			VENTANA.blit(pygame.transform.scale(fichaBlanca, (40, 40)),(740,170))



		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type==MOUSEBUTTONDOWN:
				x,y=event.pos
				for i in range(0,8):
					for j in range(0,8):
						if TABLERO_POS[i][j].collidepoint(x,y):
							jugada=True
							x,y=i,j
	
		pygame.display.update()

	return x,y

def ModoDeJuego():

	#Crear Ventana
	ancho,largo=800,600
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")


	#Colores
	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	
	TITULO=pygame.image.load("IMAGENES/TITULO.png")
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",30)


	
	jugadores=["",""]
	casilla_jug0=False
	casilla_jug1=False
	IntroducidoNombre0=False
	IntroducidoNombre1=False
	

	MOUSE_V=fuente.render("MOUSE",0,BLANCO)#TEXTO DE CASILLA1
	TECLADO_V=fuente.render("TECLADO",0,BLANCO)#TEXTO DE CASILLA2
	MODO_JUEGO=fuente.render("Modo de Juego",0,VERDE)

	PosX,PosY=100,300
	ancho1,largo1=250,100
	VENTANA.blit(FONDO,(0,0))
	VENTANA.blit(TITULO,(120,10))

	CASILLA_MOUSE=pygame.draw.rect(VENTANA,GRIS,(PosX,PosY,ancho1,largo1),5)#CASILLA INACTIVA JUG1
	CASILLA_TECLADO=pygame.draw.rect(VENTANA,GRIS,(PosX+350,PosY,ancho1,largo1),5)#CASILLA INACTIVA JUG2
	VENTANA.blit(MOUSE_V,(PosX+40,PosY+20))
	VENTANA.blit(TECLADO_V,(PosX+380,PosY+20))
	VENTANA.blit(MODO_JUEGO,(PosX+180,PosY-50))
	

	MOUSE=False
	TECLADO=False


	while not(MOUSE or TECLADO):

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos

				if CASILLA_MOUSE.collidepoint(x,y):
					MOUSE=True

				elif CASILLA_TECLADO.collidepoint(x,y):
					TECLADO=True

		
		pygame.display.update()


	return MOUSE,TECLADO

def FinDelJuego(jugadores:[int],FichasNegras:int,FichasBlancas:int):

	#Crear Ventana
	ancho,largo=800,600
	VENTANA=pygame.display.set_mode((ancho,largo))
	pygame.display.set_caption("¡Reversi! v0.1")


	#Colores
	GRIS=(130,130,130)
	NEGRO=(0,0,0)
	VERDE=(72,111,25)
	BLANCO=(255,255,255)
	
	TITULO=pygame.image.load("IMAGENES/TITULO.png")
	FONDO=pygame.image.load("IMAGENES/FONDO.png")
	SIGUIENTE=pygame.image.load("IMAGENES/SIGUIENTE.png")
	fichaNegra=pygame.image.load("IMAGENES/negra.png")
	fichaBlanca=pygame.image.load("IMAGENES/blanca.png")
	fuente=pygame.font.Font("FUENTES/Turtles.ttf",60)

	VENTANA.blit(FONDO,(0,0))
	VENTANA.blit(TITULO,(120,10))
	SIGUIENTE_V=VENTANA.blit(SIGUIENTE,(580,450))
	

	if FichasNegras>FichasBlancas:
		VENTANA.blit(fuente.render("Ganador:",1,BLANCO),(200,300))
		VENTANA.blit(fuente.render(str(jugadores[0]),1,BLANCO),(250,360))
		VENTANA.blit(fichaNegra,(480,300))
	elif FichasBlancas>FichasNegras:
		VENTANA.blit(fuente.render("Ganador:",1,BLANCO),(200,300))
		VENTANA.blit(fuente.render(str(jugadores[1]),1,BLANCO),(250,360))
		VENTANA.blit(fichaBlanca,(480,300))

	else:
		VENTANA.blit(pygame.fuente.render("EMPATE",1,BLANCO),(300,300))

	fin=False

	while not(fin):

		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit() 
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				x,y=event.pos

				if SIGUIENTE_V.collidepoint(x,y):
					fin=True
		
		pygame.display.update()


def esValida(x:int,y:int,tablero:[[int]],turno:int):
	if turno==1:
		op=2
	else:
		op=1

	validez=False
	casillasPorCambiar=[]

	if tablero[x][y]!=0:
		return validez,casillasPorCambiar

	#Una fila abajo
	if x+1<7 and tablero[x+1][y]==op:
		xder=x+1
	
		while xder<7 and tablero[xder][y]==op:
			xder+=1

		if tablero[xder][y]==turno:
			validez=True
			i=0
			while xder-i>x:
				casillasPorCambiar.append([xder-i,y])
				i+=1

	#fila arriba
	if x-1>0 and tablero[x-1][y]==op:
		
		xizq=x-1
	
		while xizq>=0 and tablero[xizq][y]==op:
			xizq-=1

		if tablero[xizq][y]==turno:
			validez=True
			i=0
			
			while xizq+i<x:
				casillasPorCambiar.append([xizq+i,y])
				i+=1

	#columna derecha
	if y+1<7 and tablero[x][y+1]==op:
		
		yder=y+1
	
		while yder<7 and tablero[x][yder]==op:
			yder+=1

		if tablero[x][yder]==turno:
			validez=True
			i=0
			while yder-i>y:
				casillasPorCambiar.append([x,yder-i])
				i+=1

	#columna izq
	if y-1>0 and tablero[x][y-1]==op:
		
		yizq=y-1
	
		while yizq>0 and tablero[x][yizq]==op:
			yizq-=1

		if tablero[x][yizq]==turno:
			validez=True
			i=0
			while yizq+i<y:
				casillasPorCambiar.append([x,yizq+i])
				i+=1
	
	#diagonal inferior der
	if x+1<7 and y+1<7 and tablero[x+1][y+1]==op:
		xder=x+1
		yder=y+1
		
		while xder<7 and yder<7 and tablero[xder][yder]==op:
			xder+=1
			yder+=1

		if tablero[xder][yder]==turno:
			validez=True
			i=0
			while xder-i>x and yder-i>y:
				casillasPorCambiar.append([xder-i,yder-i])
				i+=1


	#diagonal superior der
	if x-1>0 and y+1<7 and tablero[x-1][y+1]==op:
		xder=x-1
		yder=y+1
		
		while xder>0 and yder<7 and tablero[xder][yder]==op:
			xder-=1
			yder+=1

		if tablero[xder][yder]==turno:
			validez=True
			i=0
			while xder+i<x and yder-i>y:
				casillasPorCambiar.append([xder+i,yder-i])
				i+=1

	if x-1>0 and y-1>0 and tablero[x-1][y-1]==op:
		xder=x-1
		yder=y-1
		
		while xder>=0 and yder>=0 and tablero[xder][yder]==op:
			xder-=1
			yder-=1

		if tablero[xder][yder]==turno:
			validez=True
			i=0
			while xder+i<x and yder+i<y:
				casillasPorCambiar.append([xder+i,yder+i])
				i+=1

	if y-1>0 and x+1<7 and tablero[x+1][y-1]==op:
		xder=x+1
		yder=y-1
		
		while yder>0 and xder<7 and tablero[xder][yder]==op:
			xder+=1
			yder-=1

		if tablero[xder][yder]==turno:
			validez=True
			i=0
			while xder-i>x and yder+i<y:
				casillasPorCambiar.append([xder-i,yder+i])
				i+=1


	return validez,casillasPorCambiar


def TableroValido(tablero:[[int]],turno:int):
	B=inicializarTablero()
	cantidadJugadasValidas=0
	for x in range(0,8):
		for y in range(0,8):
			B[x][y]=tablero[x][y]
			validez,jugadas=esValida(x,y,tablero,turno)
			if validez:
				B[x][y]=3
				cantidadJugadasValidas+=1


	return B,cantidadJugadasValidas

def flanqueo(tablero:[[int]],respuesta:[int],turno:[int]):
	for i in respuesta:
		tablero[i[0]][i[1]]=turno





##PROGRAMA PRINCIPAL


import pygame,sys,time
from pygame.locals import *

pygame.init()

while DeseaJugar():
		
	tablero=inicializarTablero()
	turno=1
	
	TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
	jugadores=Jugadores()
	mouse,teclado=ModoDeJuego()		

	while TotalFichas>0:

		tableroValido,cantidadJugadasValidas=TableroValido(tablero,turno)

		if cantidadJugadasValidas==0:
			turno=CambiarTurno(turno)
			tableroValido,cantidadJugadasValidas=TableroValido(tablero,turno)
			if cantidadJugadasValidas==0:
				break


		if teclado:	
			
			x,y=ObtenerJugada1(tableroValido,jugadores,turno)
			
			try:
				x,y=TraducirJugada(x,y)
				validez,DirFlanqueo=esValida(x,y,tablero,turno)
			except:
				validez=False 
		 
		elif mouse:
			
			x,y=ObtenerJugada2(tableroValido,jugadores,turno)
			validez,DirFlanqueo=esValida(x,y,tablero,turno)
			
		
		if validez:
			RealizarJugada(turno,tablero,x,y)
			TotalFichas,FichasNegras,FichasBlancas=QuedanFichas(tablero)
			flanqueo(tablero,DirFlanqueo,turno)
			turno=CambiarTurno(turno)

		TableroYPuntuacion(tablero,jugadores,FichasNegras,FichasBlancas,validez)

	FinDelJuego(jugadores,FichasNegras,FichasBlancas)
