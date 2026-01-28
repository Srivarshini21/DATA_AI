import shutil
import datetime
source="C:/Users/22h51/OneDrive/Desktop/python/data.txt"
destination=f"C:/Users/22h51/OneDrive/Desktop/python/data_backup_{datetime.date.today()}.txt"
shutil.copy(source,destination)
print(f"Backup of {source} created at {destination}")