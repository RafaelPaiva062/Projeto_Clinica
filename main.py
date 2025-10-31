import sqlite3
from datetime import time, date
from xml.dom import NO_MODIFICATION_ALLOWED_ERR

conexao = sqlite3.connect("clinica_vida.db")
cursor = conexao.cursor()
cursor.executescript('''
DROP TABLE IF EXISTS pacientes;
DROP TABLE IF EXISTS medicos;
DROP table if exists exames;
 create table if not exists pacientes(
    id_pacientes integer primary key autoincrement,
    nome text not null,
    idade real not null,
    telefone text not null,
    cpf text,
    rg text,
    criado_em datetime default (datetime('now')),
    atualizado datetime default  (datetime('now'))
);

 create table if not exists medicos(
     id_medicos integer primary key autoincrement,
     nome text not null,
     idade real not null,
     especialidade  text not null,
     horario time not null,
     telefone text not null,
     criado_em datetime default(datetime('now')),
     atualizado_ datetime default (datetime('now'))
 );
create table if not exists exames(
    id_exames_ integer primary key autoincrement,
    id_pacientes integer,
    id_medicos integer,
    data_exames date ,
    hora_exames time ,
    tipo_procedimento text,
    laudo text ,
    resultado_ text,
    status text default 'agendado',
    valor real ,
    criado_em datetime default(datetime('now')),
    atualizado_ datetime default (datetime('now')),
    foreign key (id_pacientes) references pacientes(id_pacientes),
    foreign key (id_medicos) references medicos(id_medicos)
);
''')
conexao.commit()


class Paciente:

    def __init__(self, nome: str, idade: int, telefone: str, id_pacientes: int = None, cpf: str = None, rg: str = None):
        self.id_pacientes = id_pacientes
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.rg = rg

    def inserir_pacientes(self):
        try:
            cur = conexao.cursor()
            sql_insert = """ 
                        INSERT INTO pacientes(id_pacientes, nome, idade, telefone, cpf, rg) \
                        values (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, (self.id_pacientes, self.nome, self.idade, self.telefone, self.cpf, self.rg))
            conexao.commit()
            return cur.lastrowid
        except sqlite3.Error as e:
            print(f'Erro de inserir paciente:{e}')
            return None


class Medicos:

    def __init__(self, nome: str, idade: int, especialidade: str, horario: time, telefone_m: str,
                 id_medicos: int = None):
        self.id_medicos = id_medicos
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade
        self.horario = horario
        self.telefone = telefone_m

    def inserir_medicos(self):
        try:
            cur = conexao.cursor()
            sql_insert = """ insert into medicos(id_medicos, nome,idade, especialidade, horario,telefone)
                            values (?,?,?,?,?,?)"""
            cur.execute(sql_insert,
                        (self.id_medicos, self.nome, self.idade, self.especialidade, self.horario, self.telefone))
            conexao.commit()
            return cur.lastrowid
        except sqlite3.Error as e:
            print(f'Erro medicos {e}')
            return NO_MODIFICATION_ALLOWED_ERR


class Exames:
    def __init__(self, data_exame: date, hora_exame: time, tipo_procedimento: str, laudo: str, resultado: str,
                 status: str,
                 valor: float, id_pacientes: int = None, id_medicos: int = None):
        self.id_pacientes = id_pacientes
        self.id_medicos = id_medicos
        self.data_exame = data_exame
        self.hora_exame = hora_exame
        self.tipo_procedimento = tipo_procedimento
        self.laudo = laudo
        self.resultado = resultado
        self.status = status
        self.valor = valor

