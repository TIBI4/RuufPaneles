# Ejercicios Ruuf

En estos ejercicios se determina la cantidad de rectángulos que caben dentro de tres formas geométricas distintas. Se asume que solo hay dos orientaciones de paneles posibles: 0° y 90°.

![](https://github.com/TIBI4/RuufPaneles/assets/25259582/c8b9aa27-0eb1-49f6-b514-1c0a2e192228)

### max_abrect_in_xyrect(a, b, x, y)

Esta función determina la máxima cantidad de rectángulos de dimensiones `a` por `b` que pueden caber dentro de un rectángulo de dimensiones `x` por `y`.

- `a`: Anchos de los rectángulos a colocar.
- `b`: Alturas de los rectángulos a colocar.
- `x`: Ancho del rectángulo contenedor.
- `y`: Altura del rectángulo contenedor.

### max_abrect_in_xhtri(a, b, x, h)

Esta función determina la máxima cantidad de rectángulos de dimensiones `a` por `b` que pueden caber dentro de un triángulo rectángulo con base `x` y altura `h`.

- `a`: Anchos de los rectángulos a colocar.
- `b`: Alturas de los rectángulos a colocar.
- `x`: Base del triángulo isóceles contenedor.
- `h`: Altura del triángulo isóceles contenedor.

### max_abrect_in_two_overlapped_xyrect(a, b, x, y, dx, dy)

Esta función determina la cantidad máxima de rectángulos de dimensiones `a` por `b` dentro de dos rectángulos superpuestos con dimensiones `x` por `y`, desplazados por `dx` y `dy`. Ambos rectángulos contenedores estan orientados con el mismo ángulo.

- `a`: Anchos de los rectángulos a colocar.
- `b`: Alturas de los rectángulos a colocar.
- `x`: Ancho del rectángulo contenedor.
- `y`: Altura del rectángulo contenedor.
- `dx`: Desplazamiento horizontal entre los dos rectángulos contenedores.
- `dy`: Desplazamiento vertical entre los dos rectángulos contenedores.

# Visualización

Se pueden visualizar los tres casos en el siguiente link: [https://black-stacie-31.tiiny.site/](https://black-stacie-31.tiiny.site/)

![Visualización de la página en cuestión](https://vault.tibi4.com/s/GMj8EgFJS7t2TmJ/download?path=&files=)
