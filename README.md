# car-buying
Этапы:
1) генерация списка машин
2) выбор оптимального автомобиля
3) интерфейс

Описание этапов:


Этап 1):
Генерироавть список автомобилей с помощью создания класса и записывание дальнейшей информации в json-файл.
У каждого автомобиля должны быть следующие важные параметры:

-количество лошадиных сил

-цена

-количество мест

-тип автомобиля

-количество аварий

-пробег

-привод

-тип двигателя(электро, дизель, бензин, гибрид)

-количетво литров в двигателе
(-бензобак)

-год производства и количество лет автмобилю

-топливная экономичность (л/100 км)

-разгон до 100 км/ч

-максимальная скорость

-объем багажника(литры)

-тип коробки (автомат, механика, роботизированная)


Этап 2):
выбрать лучший автомобиль для:

-семьи:
автомобиль должен быть небыстрым, вместительным, коробка автомат(по желанию), объемный багажник, топливно экономичный и с большим количеством мест(от 4 и более) (подходят все типы автомобилей, в котроых 4 и более мест).

-динамичный автомобиль:
автомобиль должен быть быстрым, иметь большую максимальную скорость, роботизированная коробка передач, полный привод, обЪем двигателя большой и мин разгон до 100 (подходят почти все типы автомобилей, кроме минивэнов и грузовых автомобилей).

-бездорожья
машина должна быть похожа на динамичный автомобиль, но при этом не все типы авотмобилей подходят для этой категории, нужно выбрать определенные(кроссовер или внедорожник, например).

Для каждого параметра авто ставятся "баллы" в соответствии с критериями предназначения авто(семейный, динамичный, для бездорожья) Баллы ставятся в следующем порядке:

-в параметрах, где возможно огромное количество различных вариантов, таких как цена, год авто, пробег и тд, баллы выставляются в пределах каких-либо чисел, например, в параметре цена  0-100 тысяч рублей будет даватся один балл, дальше 100-200 2 балла и так далее с шагом в 100 тысяч рублей.

-для различных предназначений авто существует своя система распределения баллов

-для всех предназначений авто существуют единые параметры, кторые во всех бальных системах выставляются одинаково (например, количество аварий)

В итоге для каждого авто суммируем все баллы, и у какого авто будет наименьшее количество баллов является лучшим вариантом среди предоставленных авто.
-Если машин с наименьшим количеством баллов несколько, то запускаем повтороное распределение баллов, но уже по тем параметрам, которые нам нужны.
-Если по итогу второго отбора получится опять несколько авто с наименьшим количеством баллов, то сравниваем их по цене и состоянию авто.
-Если опять выдаст несколько авто, то предоставляем пользователю выбрать авто самому.


Этап 3):
-предложить пользователю выбрать предназначение покупаемого авто
-вывести полученные результаты





















