# inno_test


БД postgres

перед запуском проекта создайте ```.env``` file и настройте бд как в файле ```env.example```

Чтобы запустить проект введите команду ```docker-compose up -d --build```

далее введите  ```docker-compose exec web python manage.py migrate```

http://localhost:8000/docs/  ```swagger documentation```


http://localhost:8000/api_search/?search=  ```text or id```  



