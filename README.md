
 Task
Це тестове завдання дуже схоже на проблему, яку ми вирішували свого часу в продукті.
Ми хочемо зрозуміти, як ти вмієш враховувати різні вимоги в одному проєкті.

Отже:
Треба спроєктувати та написати відмовостійкий та масштабований REST-сервіс для зберігання бінарних даних в будь-якому хмарному сервісі (S3, Azure Blob Storage, Dropbox і тд). Доступ до даних здійснюється по ключу (key-value)

Вимоги до сервісу:
Операції put, get через REST
Синхронний запис (дані доступні через get одразу після завершення put)
Можна використовувати будь-який фреймворк, окрім Django

Urls for check
PUT(please attach files) - http://127.0.0.1:5000/get-create-update
GET(pk - id of item which we wanna get ) - http://127.0.0.1:5000/get-create-update/<pk>


