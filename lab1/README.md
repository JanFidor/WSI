Decyzje projektowe:

* Przedstawienie funkcji w postaci klasy -> obliczanie wartości i różniczki dla parametrów w jednym miejscu

Wybrane stałe:

Ilość wylosowanych punktów: 1_000

Ilość kroków: 1_000

Epsilon: 10^-4 

Punkty losowe z przedziału: [-5, 5]

* Próbowałem znaleźć balans pomiędzy ilością kroków i liczbą wygenerowanych punktów
* Symetryczne przedział (względem 0) względnie blisko 0 -> f(x) szybko nabiera wartości 

Funkcja f(x):

Wpływ kroku na średnią, minimum i odchylenie standardowe dla wylosowanych punktów
| Krok | 10^-6 | 10^-4 | 10^-2 | 5 * 10^-2 | 10^-1 |
| :---: | :---: | :---: | :---: | :---: | :---: | 
| Średnia | 31.03 | 33.71 | 14.40 | 0.78 | 34.49 | 
| Minimum | 2.22 * e^-10 | 4.82 * e^-10 | 8.50 * e-14 | 1.87 * e^-17 | 1.74 * e^-11 | 
| Odchylenie Standardowe | 41.30 | 43.20 | 15.67 | 0.79 | 113.04 |

Zwiększanie kroku ma luźne powiązanie z odległością osiągniętego minimum do absolutnego 
-> zapewne dlatego, że jest w stanie szybciej dotrzeć w jego pobliże.

Zwiększanie kroku zmniejsza także średnią oraz odchylenie standardowe 
-> najpewniej umożliwia to funkcji zbliżenie się na mniejszą odległość do minimum lokalnego,
a tym samym zmniejszenie różnicy wartości algorytmu dla różnych punktów.

Ważne jest zauważenie, różnicy dla kroków 5 * 10^-2 i 10^-1. 10^-1 jest zbyt dużym krokiem, 
przez co funkcja "przeskakuje" minimum co zwiększa dystans znalezionego minimum do minimum 
absolutnego a także znacznie zwiększa średnią i odchylenie standardowe. 

Funkcja g(x):

Wpływ kroku na średnią, minimum i odchylenie standardowe dla wylosowanych punktów
| Krok | 10^-6 | 10^-4 | 10^-2 | 10^-1 | 1 |
| :---: | :---: | :---: | :---: | :---: | :---: | 
| Średnia | 1.95 | 1.97 | 1.97 | 1.93 | 1.92 | 
| Minimum |  1.50 | 1.50 | 1.54 | 1.18 | 1.00 | 
| Odchylenie Standardowe | 0.14 | 0.13 | 0.09 |  0.15 | 0.21 |


Średnia wskazuje na to, że punkty zbyt oddalone od lokalnego minimum nie są w stanie się do 
niego w zauważalnym stopniu zbliżyć z powodu zbyt małego gradientu.

Zwiększanie kroku ma luźne powiązanie z odległością osiągniętego minimum do absolutnego 
-> zapewne dlatego, że jest w stanie szybciej dotrzeć w jego pobliże, co jest dużym 
problemem dla tej funkcji.

Wysokie odchylenie standardowe jest zapewne powodowane tym, że:

* funkcja zbyt powolno zbliża się do minimum, przez co tylko dla części punktów dystans zauważalnie się zmniejsza 
* funkcja zbyt szybko zbliża się do minimum i je "przeskakuje"
