import sqlite3 as lite

#functionality
class DatabaseManage(object):
    def __init__(self):
        #connection object for sqlite3
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id integer primary key autoincrement, name TEXT, description TEXT, price TEXT, isPrivate BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("unable to create db !")
    
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("insert into course(name, description, price, isprivate) values(?,?,?,?)",data)
            return True
        except  Exception:
            return False
    

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("select * from course")
                return cur.fetchall()
        except Exception:
            return False


    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "delete from course where id = ?"
                cur.execute(sql,[id])
                return True
        except Exception:
            return False

#intreface
def main():
    print("\ncourse management :: \n")
    print("\n")



    db = DatabaseManage()
    print("-"*40)
    print("\n :: user manual :: \n")
    print("-"*40)

    print("\n1. Insert a new course\n");
    print("\n2. show all course\n")
    print("\n3. delete course\n")
    print("-"*40)
    print("\n")

    choice  = input("\nEnter a choice :: ")
    
    if choice == "1":
        name = input("\nEnter course name : ")
        desc = input("\nEnter course description : ")
        price = input("\nEnter course price : ")
        private = input("\nIs this course private ? (0/1) : ")

        if db.insert_data([name,desc,price,private]):
            print("course inserted\n")
        else:
            print("error\n")

    elif choice == "2":
        print("\n:: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\nSl No. : " + str(index+1))
            print("\ncourse Id : " + str(item[0]))
            print("\ncourse Name : " + str(item[1]))
            print("\ncourse desc : " + str(item[2]))
            print("\ncourse price : " + str(item[3]))
            private = "Yes" if item[4] else "No"
            print("\nIs course is private : " + private)
            print("\n")
    
    elif choice == "3":
        record_id = input("Enter the course id : ")
        if db.delete_data(record_id):
            print("Course was deleted")
        else:
            print("Error\n")
    else:
        print("\nInvalid choice!!!\n")

if  __name__ == '__main__':
    main()






























