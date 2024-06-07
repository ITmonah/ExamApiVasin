from sqlalchemy.orm import Session
from database import engine
import models

models.Base.metadata.drop_all(bind=engine) #пересоздание таблиц
models.Base.metadata.create_all(bind=engine) #пересоздание таблиц

with Session(bind=engine) as session:
    u1=models.User(name="Малинина", mail="recipes228@mail.ru", password="$2b$12$/2gx.pO8GYYk7yASJfH3m.rYwOgaO/GvZ6Mzvqvyq.ZdT/mnZBpRS") #пользователи

    i1=models.Ingredient(name="Пшеничная мука") #ингредиенты
    i2=models.Ingredient(name="Вода") #пицца
    i3=models.Ingredient(name="Сухие дрожжи")
    i4=models.Ingredient(name="Растительное масло")
    i5=models.Ingredient(name="Сахар")
    i6=models.Ingredient(name="Соль")
    i7=models.Ingredient(name="Помидоры")
    i8=models.Ingredient(name="Майонез") 
    i9=models.Ingredient(name="Кетчуп")
    i10=models.Ingredient(name="Чеснок")
    i11=models.Ingredient(name="Приправы")
    i12=models.Ingredient(name="Сыр Моцарелла")
    i13=models.Ingredient(name="Сырокопчёнаая колбаса")
    i14=models.Ingredient(name="Оливковое масло")
    i15=models.Ingredient(name="Шоколад") #клубника в шоколаде
    i16=models.Ingredient(name="Клубника")
    i17=models.Ingredient(name="Макароны") #макароны с сыром
    i18=models.Ingredient(name="Гречневая крупа") #гречка с молоком
    i19=models.Ingredient(name="Молоко")
    i20=models.Ingredient(name="Сливочное масло")
    i21=models.Ingredient(name="Малина") #чай с малиной
    i22=models.Ingredient(name="Чёрный чай")
    i23=models.Ingredient(name="Лайм")
    i24=models.Ingredient(name="Мята")
    i25=models.Ingredient(name="Сметана") #манник
    i26=models.Ingredient(name="Манка")
    i27=models.Ingredient(name="Яйцо")

    soc1=models.System_of_calculation(name="кг") #система исчисления
    soc2=models.System_of_calculation(name="г")
    soc3=models.System_of_calculation(name="л")
    soc4=models.System_of_calculation(name="мл")
    soc5=models.System_of_calculation(name="шт")
    soc6=models.System_of_calculation(name="стол. л.")
    soc7=models.System_of_calculation(name="чайн. л.")

    r1=models.Recipe(name="Пицца", face_img="recipe/files/pizza.jpg", cooking_time=120) #рецепты
    r2=models.Recipe(name="Клубника в шоколаде", face_img="recipe/files/choko.jpg", cooking_time=30) 
    r3=models.Recipe(name="Макароны с сыром", face_img="recipe/files/mak.jpg", cooking_time=20) 
    r4=models.Recipe(name="Гречка с молоком", face_img="recipe/files/grechka.jpg", cooking_time=60) 
    r5=models.Recipe(name="Чай с малиной", face_img="recipe/files/chay.jpg", cooking_time=15) 
    r6=models.Recipe(name="Манник", face_img="recipe/files/mannik.jpg", cooking_time=100) 

    #пицца
    count1=models.Count(recipe=r1, ingredient=i1, count=250, system_of_calc=soc2)
    count2=models.Count(recipe=r1, ingredient=i2, count=120, system_of_calc=soc4)
    count3=models.Count(recipe=r1, ingredient=i3, count=10, system_of_calc=soc2)
    count4=models.Count(recipe=r1, ingredient=i4, count=1, system_of_calc=soc6)
    count5=models.Count(recipe=r1, ingredient=i5, count=1, system_of_calc=soc2)
    count6=models.Count(recipe=r1, ingredient=i6, count=1, system_of_calc=soc2)
    count7=models.Count(recipe=r1, ingredient=i7, count=2, system_of_calc=soc5)
    count8=models.Count(recipe=r1, ingredient=i14, count=1, system_of_calc=soc6)
    count9=models.Count(recipe=r1, ingredient=i9, count=1, system_of_calc=soc6)
    count10=models.Count(recipe=r1, ingredient=i8, count=1, system_of_calc=soc6)
    count11=models.Count(recipe=r1, ingredient=i10, count=2, system_of_calc=soc5)
    count12=models.Count(recipe=r1, ingredient=i11, count=1, system_of_calc=soc6)
    count13=models.Count(recipe=r1, ingredient=i12, count=120, system_of_calc=soc2)
    count14=models.Count(recipe=r1, ingredient=i13, count=100, system_of_calc=soc2)
    #клубника в шоколаде
    count15=models.Count(recipe=r2, ingredient=i15, count=800, system_of_calc=soc2)
    count16=models.Count(recipe=r2, ingredient=i16, count=90, system_of_calc=soc2)
    count17=models.Count(recipe=r2, ingredient=i4, count=2, system_of_calc=soc7)
    #макароны с сыром  
    count17=models.Count(recipe=r3, ingredient=i17, count=300, system_of_calc=soc2)
    count18=models.Count(recipe=r3, ingredient=i12, count=200, system_of_calc=soc2)
    count19=models.Count(recipe=r3, ingredient=i11, count=1, system_of_calc=soc7)
    count20=models.Count(recipe=r3, ingredient=i6, count=1, system_of_calc=soc7)
    #гречка с молоком
    count21=models.Count(recipe=r4, ingredient=i6, count=1, system_of_calc=soc7)
    count22=models.Count(recipe=r4, ingredient=i18, count=200, system_of_calc=soc2)
    count23=models.Count(recipe=r4, ingredient=i19, count=1, system_of_calc=soc3)
    count24=models.Count(recipe=r4, ingredient=i20, count=40, system_of_calc=soc2)
    #чай с малиной
    count25=models.Count(recipe=r5, ingredient=i21, count=100, system_of_calc=soc2)
    count26=models.Count(recipe=r5, ingredient=i22, count=5, system_of_calc=soc5)
    count27=models.Count(recipe=r5, ingredient=i23, count=1, system_of_calc=soc5)
    count28=models.Count(recipe=r5, ingredient=i24, count=2, system_of_calc=soc5)
    count29=models.Count(recipe=r5, ingredient=i5, count=1, system_of_calc=soc6)
    count30=models.Count(recipe=r5, ingredient=i2, count=700, system_of_calc=soc4)
    #манник
    count31=models.Count(recipe=r6, ingredient=i25, count=250, system_of_calc=soc2)
    count32=models.Count(recipe=r6, ingredient=i26, count=200, system_of_calc=soc2)
    count33=models.Count(recipe=r6, ingredient=i27, count=3, system_of_calc=soc5)
    count34=models.Count(recipe=r6, ingredient=i5, count=200, system_of_calc=soc2)
    count35=models.Count(recipe=r6, ingredient=i1, count=150, system_of_calc=soc2)
    count36=models.Count(recipe=r6, ingredient=i6, count=1, system_of_calc=soc7)

    session.add_all([u1,
                    i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,
                    soc1,soc2,soc3,soc4,soc5,soc6,soc7,
                    r1,r2,r3,r4,r5,r6, 
                    count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,
                    count11,count12,count13,count14,count15,count16,count17,count18,count19,count20,
                    count21,count22,count23,count24,count25,count26,count27,count28,count29,count30,
                    count31,count32,count33,count34,count35,count36,
                    ])
    session.commit()

