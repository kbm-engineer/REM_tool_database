import streamlit as st
#from .models import BaseMonitoringObject


def main():
    st.title("Привет, мир!")
    st.write("Я связал Streamlit и Django в одной коробке :)")

    #objects = BaseMonitoringObject.objects.all()

    # if objects:
    #     # Выводим объекты списком
    #     st.write("Список объектов:")
    #     for obj in objects:
    #         st.write(f"Имя: {obj.name}, Описание: {obj.type}")

    #     # Выводим объекты в виде таблицы
    #     st.write("Таблица объектов:")
    #     st.dataframe(objects)
    # else:
    #     st.write("Нет доступных объектов класса MyClass")

if __name__ == "__main__":
    main()