# <samp>Tablero de ajedrez con Python :full_moon_with_face:</samp>

## <samp>Instalar Python :snake:</samp>
Para poder usar las siguientes implementaciones que nos permite manipular la creación de tableros de ajedrez, debemos instalar Python en nuestro sistema operativo.

> Intalando python en ubuntu :penguin:
```sh
sudo apt update
sudo apt install python3
```

## <samp>Instalar Pygame, una biblioteca de Python</samp>
La biblioteca `pygame` nos proporciona funcionalidades más accesibles tales como representar graficos 2D, sonido, manejo de eventos y entrada de usuario.

Nosotros podemos realizar la instalación de paquetes de las siguiente dos formas.

### Instalando paquetes a nivel del sistema operativo
#### Ventajas:
- Significa que el paquete estará disponible para todos los scripts de Python en el sistema operativo.

#### Desventajas:
- **Conflictos de dependencias** Diferentes proyectos pueden requerir diferentes versiones de pygame u otros paquetes. Instalar a nivel del sistema puede causar conflictos.
- **Actualizaciones:** Actualizar un paquete puede afectar a todos los proyectos que dependen de él.

> Como vamos a instalar el paquete en nuestro sistema operativo, usamos nuestro administrador de paquetes
```sh
sudo pacman -Syu
sudo pacman -S python-pygame 
```

### Instalando paquetes en un ambiente virtual
Los ambientes virtuales son entornos aislados que permiten tener diferentes versiones de paquetes y dependencias para distintos proyectos sin interferir entre sí. Es decir, las dependencias solo se instalan en tu directorio raiz de tu proyecto.

> Es recomendable usar ambientes virtuales `venv` cuando trabajas en proyectos específicos

#### Ventajas:
- **Aislamiento** Cada proyecto puede tener sus propias dependencias y versiones específicas sin interferir con otros proyectos.
- Evita conflictos de dependencias y facilita la gestión de las versiones de los paquetes

#### Pasos para crear un ambiente virtual
> **Paso 1:** Creamos un ambiente virtual dentro del directorio de nuestro proyecto
```sh
mkdir chess_with_python
cd chess_with_python
python3 -m venv chess
```
El último crea un directorio con el nombre `chess` el cual debería verse de la siguiente manera
```sh
chess_with_python/
└── chess/
    ├── bin/      (o Scripts/ en Windows)
    ├── include/
    ├── lib/
    └── ... (otros archivos del ambiente virtual)
```

> **Paso 2:** Activar el ambiente virtual
```sh
source chess/bin/activate
```

Ahora estamos dentro del ambiente virtual. En este entorno nosotros podemos instalar `pygame` que solo estará disponible cuando se inicie este entorno virtual.

> Instalando con `pip`, gestor de paquetes de python
```sh
pip install pygame
```
> Puedes listar los paquetes instalados en el entorno virtual
```sh
pip list

# Si deseas ver todas las opciones
pip --help

```
Cuando termines de trabajar en tu proyecto, necesitas salir del entorno virtual creado

> Abandonar el entorno virtual
```sh
deactivate
```
Cuando sales del entorno virtual y por ejemplo ejecutas el comando nuevamente `pip list`, te darás cuenta que los paquetes disponibles difieren.
