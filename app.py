from time import strftime
import logging, sys
from logging.handlers import RotatingFileHandler
from blueprint import app, manager, db
from blueprint.user import ListUser
import getpass
import datetime


if __name__ == '__main__':
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    log_handler = RotatingFileHandler("%s/%s" % (app.root_path, '/storage/log/all.log'), maxBytes=10000000, backupCount=10)
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)

    try:
        if sys.argv[1] == 'createadmin':
            admin_name = input("Masukkan Nama : ")
            admin_email = input("Masukkan Email : ")
            admin_phone_number = input("Masukkan No. Telp : ")
            admin_username = input("Masukkan Admin Username : ")
            admin_password = getpass.getpass("Masukkan Admin Password : ")
            created_at = datetime.datetime.now().strftime("%c")
            list_admin = ListUser(None, admin_name, admin_email, admin_phone_number, admin_username, 
            admin_password, "admin", created_at, None)          
            db.session.add(list_admin)
            db.session.commit()
            print("Admin created.")
            exit(1)
        
        elif sys.argv[1] == 'db':
            manager.run()
        else :
            app.run(debug=False, host='0.0.0.0', port=5002)
            
    except Exception as e:
        app.run(debug=True, host='0.0.0.0', port=5002)






    
