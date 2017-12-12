
import MySQLdb
import controllers.constants


def make_db():
  db = MySQLdb.connect(
    host = controllers.constants.HOST_CONST,
    user = controllers.constants.USER_CONST,
    passwd = controllers.constants.PASSWRD_CONST,
    db = controllers.constants.DB_CONST
  )
  return db

def make_cursor():
  db = make_db()
  cursor = db.cursor()
  return db,cursor

 
def song_exists(title):
  db,cursor = make_cursor()
  cursor.execute("""SELECT * FROM Songs WHERE title=%s""",(title,))
  if cursor.fetchone() != None:
    return True
  return False
