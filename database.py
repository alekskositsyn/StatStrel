from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime


class DataBase:
    Base = declarative_base()

    class Officers(Base):
        __tablename__ = 'officers'
        id = Column(Integer, primary_key=True)
        name = Column(String, unique=False)
        birthday = Column(String, unique=False)
        department_id = Column(Integer, ForeignKey('department.id'))
        degree_id = Column(Integer, ForeignKey('degree.id'))

        def __init__(self, name, birthday, department_id, degree_id):
            self.name = name
            self.birthday = birthday
            self.department_id = department_id
            self.degree_id = degree_id

    class Department(Base):
        __tablename__ = 'department'
        id = Column(Integer, primary_key=True)
        name = Column(String, unique=True)

        def __init__(self, name):
            self.name = name

    class Degree(Base):
        __tablename__ = 'degree'
        id = Column(Integer, primary_key=True)
        name = Column(String, unique=True)
        description = Column(String)

        def __init__(self, name, description):
            self.name = name
            self.description = description

    def __init__(self):
        self.engine = create_engine('sqlite:///database/d_base.db3', echo=True, pool_recycle=7200)

        self.Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_user(self, name, birthday, department, degree):
        user = self.Officers(name, birthday, department, degree)
        self.session.add(user)
        self.session.commit()

    def create_degree(self, name, description):
        degree = self.Degree(name, description)
        self.session.add(degree)
        self.session.commit()

    def create_department(self, name):
        department = self.Department(name)
        self.session.add(department)
        self.session.commit()

    # Функция возвращает список известных пользователей со временем последнего входа.
    def users_list(self):
        query = self.session.query(
            self.Officers.id,
            self.Officers.name,
            self.Officers.birthday,
            self.Officers.department_id,
            self.Officers.degree_id
        )
        # Возвращаем список кортежей
        return query.all()

    def select_user(self):
        q = self.session.query(
            self.Officers.id,
            self.Officers.name,
            self.Officers.birthday,
            self.Degree.name,
            # self.Department.name
        ).filter(self.Officers.degree_id == 3).join(self.Officers).all()
        return q


if __name__ == '__main__':
    db = DataBase()
    # db.create_user('Филимонов Юрий Аркадьевич', "02.03.2002", 1, 2)
    # db.create_user('Романов Дмитрий Борисович', "02.12.2000", 1, 2)
    # db.create_user('Ловкин Роман Юрьевич', "06.03.1988", 4, 3)
    # db.create_user('Краснов Алексей Васильевич', "10.04.1978", 1, 2)
    # db.create_degree('Начинающий', 'Не выполняет 4 упр., знает меры безопасности')
    # db.create_degree('Средний', 'Выполняет 4 упр.')
    # db.create_degree('Высокий', 'Высокая скорость перезарядки и первого выстрела')
    # db.create_degree('Профессионал', 'Выполняет все упр. обучается тактике имеет спортивный разряд МС')
    # выводим список кортежей - активных пользователей
    # выполянем 'отключение' пользователя
    # выводим список активных пользователей
    # запрашиваем историю входов по пользователю
    # db.login_history('client_1')
    # # выводим список известных пользователей
    print(db.select_user())
    # print(db.users_list())
