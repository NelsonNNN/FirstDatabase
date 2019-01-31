import sqlite3
from students import Students

conn = sqlite3.connect ('students.db')
c = conn.cursor()
# c.execute('''CREATE TABLE student(
#     first TEXT,
#     last TEXT,
#     marks INT
# )''')
def insert_std(std):
    with conn:
        return c.execute('INSERT INTO student VALUES(:first, :last, :marks)', {'first':std.first, 'last':std.last, 'marks':std.marks})

def getstdsby_name(lastname):
    c.execute('SELECT * FROM student WHERE last=:last', {'last':lastname})
    return c.fetchall()


def update_std(std, marks):
    with conn:
        c.execute('UPDATE student SET marks = :marks WHERE first = :first AND last = :last', {'first':std.first, 'last':std.last, 'marks':marks})

def remove_std(std):
    with conn:
        c.execute('DELETE from student WHERE first = :first AND last = :last', {'first':std.first, 'last':std.last})


std_1 = Students('Jason', 'Fisher', 470)
std_2 = Students('Fabiano', 'Fisher', 476)

insert_std(std_1)
insert_std(std_2)

std = getstdsby_name('Fisher')
print(std)

update_std(std_2, 490)
remove_std(std_1)

std = getstdsby_name('Fisher')
print(std)
# c.execute('INSERT INTO student VALUES(:first, :last, :marks)', {"first":std_2.first, "last":std_2.last, "marks":std_2.marks})
# c.execute('SELECT * FROM student')

# print(c.fetchall())
# conn.commit()
conn.close()