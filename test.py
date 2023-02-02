import db
def studentdetails():
    data = []
    for i in range(5):
        data.append({
        "name": str(i+1),
        "age": str((i+1) *10),
        "marrige": "yes" if i%2 == 0 else "no"
    })
    return data

def save_data_to_db(data):
    query = "INSERT INTO `studentdetails` (`id`, `name`, `age`, `married`) VALUES "
    for studeneData in data:
        query = query+" (NULL,'"+studeneData['name']+"','"+studeneData['age']+"','"+studeneData['marrige']+"'),"
    query = query[:len(query)-1]
    db_curser = db.mycursor
    db_curser.execute(query)
    db.mydb.commit()