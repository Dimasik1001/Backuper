import os
import time

#1. Файлы и каталоги, которые необходимо скопирповать, собираются в список.
source =  input ('Введите путь к файлам для backup:')

#1.1 Проверяем введеный путь на пробелы и заменем их на знаки вопроса, так как команда 'tar' не читает пробелы.

source_without_space = source.replace(' ', '?')







# 2. Резервные копии должны храниться в основном каталоге резерва
# 2.1 Проверяем наличие каталога с бэкапами

if os.path.isdir('C:/Backup'):
	
	target_dir = 'C:/Backup' #Поставьте ваш путь

# 3. Файлы помещаются в zip архив
# 4. Текущая дата служит именем подкаталога в основном каталоге
	today = target_dir+os.sep+time.strftime("%Y.%m.%d")
#Текущее время служит именем Zip-архива

	now = time.strftime('%H"."%M"."%S')

#Запрашиваем комментарий пользователя для имени файла
	comment = input('Введите комментарий --> ')
	if len(comment) == 0: # Проверяем, введйн ли комментарий
		target = today + os.sep + now +'.zip'
	else:
		target = today + os.sep + now + '_' + \
		 comment.replace(' ', '_') + '.zip'



#Создаём каталог, если его еще нет

	if not os.path.exists(today):
		os.mkdir(today) #Создание каталога
		print('Каталог успешно создан',today)



# 5. Используем коменду "zip" для помещения файлов в архив

	zip_command = 'tar.exe -a -c -f {0} {1}'.format(target, ' '.join([source_without_space]))

# Запускаем создание резервной копии

	if os.system(zip_command)  == 0:
		print('Резервныя копия успешно создана в',target)

	else:
		print("Создание копии не удалось")

	input('Press ENTER to exit')

else:
	os.mkdir('C:/Backup')


	print('Папака Backup, создана на диске С')



	target_dir = 'C:/Backup' #Поставьте ваш путь

# 3. Файлы помещаются в zip архив
# 4. Текущая дата служит именем подкаталога в основном каталоге
	today = target_dir+os.sep+time.strftime("%Y.%m.%d")
#Текущее время служит именем Zip-архива

	now = time.strftime('%H"."%M"."%S')

#Запрашиваем комментарий пользователя для имени файла
	comment = input('Введите комментарий --> ')
	if len(comment) == 0: # Проверяем, введйн ли комментарий
		target = today + os.sep + now +'.zip'
	else:
		target = today + os.sep + now + '_' + \
	 	comment.replace(' ', '_') + '.zip'



#Создаём каталог, если его еще нет

	if not os.path.exists(today):
		os.mkdir(today) #Создание каталога
		print('Каталог успешно создан',today)



# 5. Используем коменду "zip" для помещения файлов в архив

	zip_command = 'tar.exe -a -c -f {0} {1}'.format(target, ' '.join([source_without_space]))

# Запускаем создание резервной копии

	if os.system(zip_command)  == 0:
		print('Резервныя копия успешно создана в',target)

	else:
		print("Создание копии не удалось")

	input('Press ENTER to exit')